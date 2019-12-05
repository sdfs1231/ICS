import win32clipboard
import win32con
def GetText():
    win32clipboard.OpenClipboard()
    d = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return d
data=GetText()
print(data)