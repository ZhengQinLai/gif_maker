'''
透明窗口类：
首先创建透明窗口，然后全屏；（第一个函数）
鼠标点击时获取坐标，创建方形区域；
传出区域
'''
import cv2
import numpy as np
import tkinter as tk

class TrancolorWindow:
    locate = (0, 0, 0, 0,)
    height = None
    width = None
    def __init__(self) -> None:
        root = tk.Tk()
        self.height=root.winfo_screenheight()
        self.width=root.winfo_screenwidth()
        root.destroy()
        pass

    def create(self):
        img = np.ones((self.height, self.width, 4)) * (255, 255, 255, 100)
        out_win = "output_style_full_screen"
        cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(out_win, img)

if __name__ == "__main__":
        window = TrancolorWindow()
        window.create()