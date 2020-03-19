# import wx
#
#
# def delayed():
#     print('I was delayed')
#
#
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title='Hello World')
#         wx.CallLater(4000, delayed)
#         self.Show()
#
#
# if __name__ == '__main__':
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Pressione Aqui')
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()