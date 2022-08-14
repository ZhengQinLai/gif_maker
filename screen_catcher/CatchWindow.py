'''
捕获窗口类
'''
import cv2
import pyautogui
import numpy as np
import tkinter as tk
import copy

class CatchWindow:
    #窗口名称
    name = None
    #当前分辨率
    height = None
    width = None
    #截屏
    img = None
    img_gray = None
    #鼠标起始位置
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    #是否退出
    stop = None

    def __init__(self) -> None:
        root = tk.Tk()
        self.height=root.winfo_screenheight()
        self.width=root.winfo_screenwidth()
        root.destroy()
        pass
    '''
    创建一个窗口，其内容为当前屏幕，全屏，并且将屏幕以及其灰度图像存储
    @param name:窗口名称，缺省为 window
    @return 无
    '''
    def create(self, name = 'window'):
        self.name = name
        img = pyautogui.screenshot()
        img = np.array(img)
        cv2.namedWindow(self.name, cv2.WND_PROP_FULLSCREEN)
        #cv2.moveWindow(self.name, self.width - 1, self.height - 1)
        cv2.moveWindow(self.name, 2719, 1950)
        cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Convert RGB to BGR,opencv read image as BGR,but Pillow is RGB
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.img = img
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img_gray = cv2.cvtColor(img_gray, cv2.COLOR_RGB2BGR)
        self.img_gray = img_gray
    '''
    渲染灰度图像，捕捉鼠标起始位置，在起始位置围框中渲染彩色图像
    @param 无
    @return 无
    '''
    def catch(self):
        cv2.setMouseCallback(self.name, click_record, self)
        while True:
            tmp_gray = copy.deepcopy(self.img_gray)
            if self.x1!=None and self.x2 !=None:
                x1 = self.x1 if self.x1 <self.x2 else self.x2
                x2 = self.x2 if self.x1 <self.x2 else self.x1
                y1 = self.y1 if self.y1 <self.y2 else self.y2
                y2 = self.y2 if self.y1 <self.y2 else self.y1
                tmp_gray[y1:y2,x1:x2] = self.img[y1:y2,x1:x2]
                tmp_gray[y1:y2,x1]=(0, 0, 255)
                tmp_gray[y1:y2,x2]=(0, 0, 255)
                tmp_gray[y1,x1:x2]=(0, 0, 255)
                tmp_gray[y2,x1:x2]=(0, 0, 255)
            cv2.imshow(self.name,tmp_gray)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            if self.stop:
                break
    '''
    返回截取的四个位置
    @param 无
    @return 四元组
    '''
    def get_loc(self):
        return self.x1, self.x2, self.y1, self.y2

'''
辅助函数，用于cv2模块中的鼠标回调
'''
def click_record(event,x,y,flags,self): 
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x1, self.y1 = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            self.x2, self.y2 = x, y
            self.stop = True
        if flags == cv2.EVENT_FLAG_LBUTTON and event == cv2.EVENT_MOUSEMOVE:
            self.x2, self.y2 = x, y

        
if __name__ == "__main__":
        window = CatchWindow()
        window.create('gif')
        window.catch()

        