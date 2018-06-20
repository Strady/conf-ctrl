import wx

class EditorPanel(wx.Panel):
    def __init__(self, parent, fname):
        super().__init__(parent)

        self.confFname = fname

        self.txtCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        try:
            self.txtCtrl.SetValue(open(fname, 'r').read())
        except:
            print('Файл %s не найден' % fname)
        self.okBtn = wx.Button(self, label='Ок')
        self.cancelBtn = wx.Button(self, label='Отмена')
        self.defaultBtn = wx.Button(self, label='По умолчанию')

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        editorSizer = wx.BoxSizer(wx.HORIZONTAL)
        editorSizer.Add(self.txtCtrl, 1, wx.EXPAND|wx.ALL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer.AddStretchSpacer()
        buttonSizer.Add(self.okBtn, flag=wx.ALL, border=5)
        buttonSizer.Add(self.cancelBtn, flag=wx.ALL, border=5)
        buttonSizer.Add(self.defaultBtn, flag=wx.ALL, border=5)

        mainSizer.Add(editorSizer, proportion=1, flag=wx.EXPAND)
        mainSizer.Add(buttonSizer, flag=wx.ALIGN_RIGHT)

        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_BUTTON, self.onOkBtn, self.okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancelBtn, self.cancelBtn)
        self.Bind(wx.EVT_BUTTON, self.onDefaultBtn, self.defaultBtn)

    def onOkBtn(self, event):
        with open(self.confFname, 'w') as f:
            f.write(self.txtCtrl.GetValue())
        self.Parent.Destroy()

    def onCancelBtn(self, event):
        self.Parent.Destroy()

    def onDefaultBtn(self, event):
        self.txtCtrl.SetValue(open(self.confFname + '.default', 'r').read())

class EditorFrame(wx.Frame):
    def __init__(self, parent, fname):
        super().__init__(parent, size=(640, 480))

        self.panel = EditorPanel(self, fname)
