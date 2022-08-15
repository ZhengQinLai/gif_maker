import Catcher
import CatchWindow
import keyboard
import winsound
import time


window = CatchWindow.CatchWindow()

while(1):
    time.sleep(0.1)
    if(keyboard.is_pressed('ctrl+space')):
        
        window.create('gif')    
        window.top()
        window.catch()
        x1, x2, y1, y2 =window.get_loc()
        keyboard.wait(57)
        winsound.Beep(600,500)
        c = Catcher.Catcher(x1, x2, y1, y2)
        c.catch()
        