import wx
import confEditor
import sshThreads

class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


        self.chb_9dpd = [wx.CheckBox(self, label=i) for i in ['a18', 'a19', 'a20']]
        group_9dpd = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label='9ДПД')
        for checkBox in self.chb_9dpd: group_9dpd.Add(checkBox, flag=wx.ALL, border=5)

        self.chb_9k434 = [wx.CheckBox(self, label=i, name=i+'9k434') for i in
                          ['a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12',
                           'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20', 'a21']]
        self.chb_9k434 = [wx.CheckBox(self, label='все', name='все9k434', style=wx.CHK_3STATE)] + self.chb_9k434
        self.editCfgBtn_9k434 = wx.Button(self, label='редактировать cfg')

        group_9k434 = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label='9К-434')
        for checkBox in self.chb_9k434: group_9k434.Add(checkBox, flag=wx.ALL, border=5)
        group_9k434.Add(self.editCfgBtn_9k434, flag=wx.ALL, border=5)

        self.chb_415 = [wx.CheckBox(self, label=i, name=i + '415') for i in
                          ['a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12',
                           'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20', 'a21']]
        self.chb_415 = [wx.CheckBox(self, label='все', name='все415', style=wx.CHK_3STATE)] + self.chb_415
        self.editCfgBtn_415 = wx.Button(self, label='редактировать cfg')

        group_415 = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label='9ДЯ-415')
        for checkBox in self.chb_415: group_415.Add(checkBox,flag=wx.ALL, border=5)
        group_415.Add(self.editCfgBtn_415, flag=wx.ALL, border=5)

        self.chb_146 = [wx.CheckBox(self, label=i, name=i + '146') for i in
                          ['a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12',
                           'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20', 'a21']]
        self.chb_146 = [wx.CheckBox(self, label='все', name='все146', style=wx.CHK_3STATE)] + self.chb_146
        self.editCfgBtn_146 = wx.Button(self, label='редактировать cfg')

        group_146 = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label='9ДЯ-146')
        for checkBox in self.chb_146: group_146.Add(checkBox, flag=wx.ALL, border=5)
        group_146.Add(self.editCfgBtn_146, flag=wx.ALL, border=5)

        self.chb_434 = [wx.CheckBox(self, label=i, name=i + '434') for i in
                          ['a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12',
                           'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20', 'a21']]
        self.chb_434 = [wx.CheckBox(self, label='все', name='все434', style=wx.CHK_3STATE)] + self.chb_434
        self.editCfgBtn_434 = wx.Button(self, label='редактировать cfg')

        group_434 = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label='9ДЯ-434')
        for checkBox in self.chb_434: group_434.Add(checkBox, flag=wx.ALL, border=5)
        group_434.Add(self.editCfgBtn_434, flag=wx.ALL, border=5)

        self.confBtn = wx.Button(self, label='Конфигурировать')
        self.startFPOBtn = wx.Button(self, label='Запустить ФПО')
        self.stopFPOBtn = wx.Button(self, label='Остановить ФПО')
        self.restartFPOBtn = wx.Button(self, label='Перезапустить ФПО')
        self.restartOSBtn = wx.Button(self, label='Перезапустить ОС')
        self.executeBtn = wx.Button(self, label='Выполнить', size=self.confBtn.Size)
        self.executeTextCtrl = wx.TextCtrl(self, size=(505, 24))
        self.logTextCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY, size=(-1, 50))

        ctrlBtnSizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrlBtnSizer.Add(self.confBtn, flag=wx.ALL, border=5)
        ctrlBtnSizer.Add(self.startFPOBtn, flag=wx.ALL, border=5)
        ctrlBtnSizer.Add(self.stopFPOBtn, flag=wx.ALL, border=5)
        ctrlBtnSizer.Add(self.restartFPOBtn, flag=wx.ALL, border=5)
        ctrlBtnSizer.Add(self.restartOSBtn, flag=wx.ALL, border=5)

        executeSizer = wx.BoxSizer(wx.HORIZONTAL)
        executeSizer.Add(self.executeBtn, flag=wx.ALL, border=5)
        executeSizer.Add(self.executeTextCtrl, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, proportion=1, border=5)


        actionsGroup = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label='Действия')
        actionsGroup.Add(ctrlBtnSizer, flag=wx.ALIGN_CENTER)
        actionsGroup.Add(executeSizer, flag=wx.ALIGN_CENTER)


        mainSizer = wx.BoxSizer(wx.VERTICAL)
        rowCell = wx.BoxSizer(wx.HORIZONTAL)
        rowCell.Add(group_9dpd, 1, wx.EXPAND|wx.ALL, 10)
        rowCell.Add(group_9k434, 1, wx.EXPAND |wx.ALL, 10)
        rowCell.Add(group_415, 1, wx.EXPAND|wx.ALL, 10)
        rowCell.Add(group_146, 1, wx.EXPAND|wx.ALL, 10)
        rowCell.Add(group_434, 1, wx.EXPAND|wx.ALL, 10)
        rowLog = wx.BoxSizer(wx.HORIZONTAL)
        rowLog.Add(self.logTextCtrl, 1, wx.RIGHT|wx.LEFT|wx.EXPAND, 5)
        mainSizer.Add(rowCell, flag=wx.ALIGN_CENTER)
        mainSizer.Add(actionsGroup, proportion=1, flag=wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, border=10)
        mainSizer.Add(rowLog, flag=wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, border=5, proportion=1)

        self.SetSizer(mainSizer)

        #Привязки элементов управления к хендлерам
        self.Bind(wx.EVT_CHECKBOX, self.onCheckBox)
        self.Bind(wx.EVT_BUTTON, self.onEditCfgBtn_9k434, self.editCfgBtn_9k434)
        self.Bind(wx.EVT_BUTTON, self.onEditCfgBtn_415, self.editCfgBtn_415)
        self.Bind(wx.EVT_BUTTON, self.onEditCfgBtn_146, self.editCfgBtn_146)
        self.Bind(wx.EVT_BUTTON, self.onEditCfgBtn_434, self.editCfgBtn_434)
        self.Bind(wx.EVT_BUTTON, self.onConfBtn, self.confBtn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onCommandBtn(event, '/etc/init.d/9dpdf11* start'), self.startFPOBtn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onCommandBtn(event, '/etc/init.d/9dpdf11* stop'), self.stopFPOBtn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onCommandBtn(event, '/etc/init.d/9dpdf11* restart'), self.restartFPOBtn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onCommandBtn(event, 'reboot'), self.restartOSBtn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onCommandBtn(event, self.executeTextCtrl.GetValue()), self.executeBtn)


    #Хендлеры
    def onCheckBox(self, event):
        checkBox = event.EventObject
        if checkBox.Name == 'все9k434':
            for cb in self.chb_9k434[1:]:
                cb.Value = checkBox.Value
        elif checkBox.Name == 'все415':
            for cb in self.chb_415[1:]:
                cb.Value = checkBox.Value
        elif checkBox.Name == 'все146':
            for cb in self.chb_146[1:]:
                cb.Value = checkBox.Value
        elif checkBox.Name == 'все434':
            for cb in self.chb_434[1:]:
                cb.Value = checkBox.Value
        elif checkBox in self.chb_9k434:
            if all(cb.Value for cb in self.chb_9k434[1:]):
                self.chb_9k434[0].Set3StateValue(wx.CHK_CHECKED)
            elif any(cb.Value for cb in self.chb_9k434[1:]):
                self.chb_9k434[0].Set3StateValue(wx.CHK_UNDETERMINED)
            else:
                self.chb_9k434[0].Set3StateValue(wx.CHK_UNCHECKED)
        elif checkBox in self.chb_415:
            if all(cb.Value for cb in self.chb_415[1:]):
                self.chb_415[0].Set3StateValue(wx.CHK_CHECKED)
            elif any(cb.Value for cb in self.chb_415[1:]):
                self.chb_415[0].Set3StateValue(wx.CHK_UNDETERMINED)
            else:
                self.chb_415[0].Set3StateValue(wx.CHK_UNCHECKED)
        elif checkBox in self.chb_146:
            if all(cb.Value for cb in self.chb_146[1:]):
                self.chb_146[0].Set3StateValue(wx.CHK_CHECKED)
            elif any(cb.Value for cb in self.chb_146[1:]):
                self.chb_146[0].Set3StateValue(wx.CHK_UNDETERMINED)
            else:
                self.chb_146[0].Set3StateValue(wx.CHK_UNCHECKED)
        elif checkBox in self.chb_434:
            if all(cb.Value for cb in self.chb_434[1:]):
                self.chb_434[0].Set3StateValue(wx.CHK_CHECKED)
            elif any(cb.Value for cb in self.chb_434[1:]):
                self.chb_434[0].Set3StateValue(wx.CHK_UNDETERMINED)
            else:
                self.chb_434[0].Set3StateValue(wx.CHK_UNCHECKED)

    def onEditCfgBtn_9k434(self, event):
        editor = confEditor.EditorFrame(None, 'cfg\\9dpdf11-k9k434.cfg')
        editor.Show()

    def onEditCfgBtn_415(self, event):
        editor = confEditor.EditorFrame(None, 'cfg\\9dpdf11-k415.cfg')
        editor.Show()

    def onEditCfgBtn_146(self, event):
        editor = confEditor.EditorFrame(None, 'cfg\\9dpdf11-k146.cfg')
        editor.Show()

    def onEditCfgBtn_434(self, event):
        editor = confEditor.EditorFrame(None, 'cfg\\9dpdf11-k434.cfg')
        editor.Show()

    def onConfBtn(self, event):
        sshThreads.ConfigurationThread(self).start()

    def onCommandBtn(self, event, command):
        if command:
            sshThreads.SendCommandThread(self, command).start()

    #вспомогательные функции
    def print_to_log(self, text):
        self.logTextCtrl.AppendText(text + '\n')

    def set_buttons_enabled(self, isEnabled):
        for button in [self.confBtn, self.startFPOBtn, self.stopFPOBtn,
                       self.restartFPOBtn, self.restartOSBtn, self.executeBtn]:
            button.Enabled = isEnabled

class MainFrame(wx.Frame):
    def __init__(self, parent, title=''):
        super().__init__(parent, title=title, size=(750, 750), pos=(100, 50))
        self.SetMinSize(wx.Size(750, 750))
        self.SetMaxSize(wx.Size(750, 750))
        self.panel = MainPanel(self)

class ConfCtrlApp(wx.App):
    def __init__(self):
        super().__init__()
        self.mainFrame = MainFrame(None, title='Conf&Ctrl')
        icon = wx.Icon(wx.Bitmap("res\icon.ico", wx.BITMAP_TYPE_ANY))
        self.mainFrame.SetIcon(icon)
        self.mainFrame.Show()

if __name__ == '__main__':
    app = ConfCtrlApp()
    app.MainLoop()