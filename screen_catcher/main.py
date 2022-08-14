import Catcher
import CatchWindow
import keyboard
import winsound
import win32gui
import win32com.client

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and
        win32gui.IsWindowEnabled(hwnd) and
        win32gui.IsWindowVisible(hwnd)):
        hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})
 
window = CatchWindow.CatchWindow()

while(1):
    if(keyboard.is_pressed('ctrl+space')):

        window.create('gif')  

        hwnd_map = {}
        win32gui.EnumWindows(get_all_hwnd, 0) 
        for h, t in hwnd_map.items():
            if t == 'gif':
                # h 为想要放到最前面的窗口句柄
                win32gui.BringWindowToTop(h)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')	
                # 被其他窗口遮挡，调用后放到最前面
                win32gui.SetForegroundWindow(h)

        window.catch()
        x1, x2, y1, y2 =window.get_loc()
        keyboard.wait(57)
        winsound.Beep(600,1000)
        c = Catcher.Catcher(x1, x2, y1, y2)
        c.catch()
        