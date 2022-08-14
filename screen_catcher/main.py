import Catcher
import CatchWindow
import keyboard
import time

window = CatchWindow.CatchWindow()
window.create('gif')
window.catch()
x1, x2, y1, y2 =window.get_loc()
#time.sleep(3)
c = Catcher.Catcher(x1, x2, y1, y2)
c.catch()
