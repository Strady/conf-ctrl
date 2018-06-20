import threading
import addrNip
import paramiko
import socket

def get_addresses(panel):
    addresses = []
    for rec in panel.chb_9dpd:
        if rec.GetValue():
            for cell in panel.chb_9k434[1:]:
                if cell.GetValue():
                    addresses.append({'main IP': addrNip.calcIP(rec.Label, cell.Label, 'a1')[0],
                                      'res IP': addrNip.calcIP(rec.Label, cell.Label, 'a1')[1],
                                      'MKTU addr': addrNip.calcAddr(rec.Label, cell.Label, 'a1'),
                                      'cfg file': addrNip.calcCfgFname('a1')})
            for cell in panel.chb_415[1:]:
                if cell.GetValue():
                    addresses.append({'main IP': addrNip.calcIP(rec.Label, cell.Label, 'a2')[0],
                                      'res IP': addrNip.calcIP(rec.Label, cell.Label, 'a2')[1],
                                      'MKTU addr': addrNip.calcAddr(rec.Label, cell.Label, 'a2'),
                                      'cfg file': addrNip.calcCfgFname('a2')})
            for cell in panel.chb_146[1:]:
                if cell.GetValue():
                    addresses.append({'main IP': addrNip.calcIP(rec.Label, cell.Label, 'a3')[0],
                                      'res IP': addrNip.calcIP(rec.Label, cell.Label, 'a3')[1],
                                      'MKTU addr': addrNip.calcAddr(rec.Label, cell.Label, 'a3'),
                                      'cfg file': addrNip.calcCfgFname('a3')})
            for cell in panel.chb_434[1:]:
                if cell.GetValue():
                    addresses.append({'main IP': addrNip.calcIP(rec.Label, cell.Label, 'a4')[0],
                                      'res IP': addrNip.calcIP(rec.Label, cell.Label, 'a4')[1],
                                      'MKTU addr': addrNip.calcAddr(rec.Label, cell.Label, 'a4'),
                                      'cfg file': addrNip.calcCfgFname('a4')})
    return addresses

def set_ssh_connection(addrs):
    """
    :param addrs: словарь {'main IP': IP адрес в основной сети,
                            'res IP': IP адрес в резервной сети,
                            'MKTU addr': МКТУ_2 адрес,
                            'cfg file': название конфигурационного файла}
    :return: открытая ssh сессия
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=addrs['main IP'], username='root', password='root', port=22, timeout=15)
    return client

class ConfigurationThread(threading.Thread):
    """
    Поток для редактирования файлов конфигурации. Запускается по кнопке "Конфигурировать"
    """
    def __init__(self, panel):

        super().__init__()
        self.panel = panel

    def run(self):

        self.panel.set_buttons_enabled(False)

        for addrs in get_addresses(self.panel):
            fname = addrs['cfg file']
            self.panel.print_to_log(f"connecting to {addrs['main IP']}...")
            try:
                client = set_ssh_connection(addrs)
                sftp = client.open_sftp()
                sftp.file('/root/' + fname, 'w').write(open('cfg/' + fname, 'r').read().replace('0:0:0:0:0:0', addrs['MKTU addr']))
                self.panel.print_to_log('cfg file updated')
                client.close()
            except socket.timeout as e:
                print(e, addrs['MKTU addr'], addrs['main IP'])
                self.panel.print_to_log('no connection to ' + addrs['main IP'] + '\n')
            except paramiko.SSHException as e:
                print(e, addrs['MKTU addr'], addrs['main IP'])
                self.panel.print_to_log('no connection to ' + addrs['main IP'] + '\n')

        self.panel.set_buttons_enabled(True)


class SendCommandThread(threading.Thread):
    """
    Потом для отправления команды на ячейки. Запускается по кнопкам "Запустить ФПО",
    "Остановить ФПО", "Перезапустить ФПО", "Перезапустить ОС", "Выполнить"
    """
    def __init__(self, panel, command):
        super().__init__()
        self.panel = panel
        self.command = command
    def run(self):
        self.panel.set_buttons_enabled(False)
        for addrs in get_addresses(self.panel):
            self.panel.print_to_log(f"connecting to {addrs['main IP']}...")
            try:
                client = set_ssh_connection(addrs)
                self.panel.print_to_log(f'executing command \'{self.command}\'...')
                if client.exec_command(self.command):
                    self.panel.print_to_log('command executed')
            except socket.timeout as e:
                print(e)
                self.panel.print_to_log(f"no connection to {addrs['main IP']}...")
            except paramiko.SSHException as e:
                print(e)
                self.panel.print_to_log(f"no connection to {addrs['main IP']}...")
        self.panel.set_buttons_enabled(True)