from cx_Freeze import setup, Executable


executables = [Executable('main.pyw',  # Скрипт, который требуется упаковать в exe файл
                        targetName='main.exe',  # Название создаваемого файла
                        base='Win32GUI',  # Избавляемся от фонового консольного окна
                        icon='res\Py.ico')]

includes = ['addrNip', 'confEditor', 'sshThreads', '_cffi_backend']
excludes = ['email', 'http', 'xml', 'bz2']


include_files = ['cfg', 'res']  # Вкладываем файл

zip_include_packages = ['collections', 'encodings', 'importlib', 'wx']  # Добавление файлов в архив

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'include_files': include_files,
        'build_exe': 'conf&ctrl_exe'  # имя папки, в которую сохранится сборка
    }
}

setup(name='conf&ctrl',
      version='0.0.1',
      description='Удаленное управление ФПО ячеек',
      executables=executables,
      options=options)
