import pyautogui
from PIL import Image
import time
import keyboard
import winsound

class Catcher:

    x1 = None
    x2 = None
    y1 = None
    y2 = None
    stop = False

    def __init__(self,x1,x2,y1,y2) -> None:
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def spacekey(self,key):
        #a = keyboard.KeyboardEvent('down', 28, 'enter')
        #if key.event_type == 'down' and key.name == a.name:
        self.stop = True
        
    def catch(self):
        frame=[]
        t1=time.time()
        while(~self.stop):
        #while(time.time()-t1<5):

            t_=time.time()
            img = pyautogui.screenshot(region=(self.x1+1, self.y1+1, self.x2-self.x1-1, self.y2-self.y1-1))
            print((self.x1, self.y1, self.x2, self.y2))
            t_=time.time()-t_
            time.sleep(0.125-t_)

            frame.append(img)
            if(keyboard.is_pressed(57)):
                winsound.Beep(600,500)
                self.stop = True
                break

        gif_name=str(str(time.time())+'.gif')
        print(len(frame))
        frame[0].save(gif_name,save_all=True,append_images=frame[1:],transparency=255,duration=125,loop=0,disposal=0)

if __name__ == "__main__":
    c = Catcher(0, 100, 0, 100)
    c.catch()