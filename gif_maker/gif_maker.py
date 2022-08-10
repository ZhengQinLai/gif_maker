"""
分为两个过程，先从整体视频转变为局部视频，再从局部视频转换为gif（240*240）
"""
from moviepy.editor import VideoFileClip
import cv2
import imageio
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

FPS = 8


class Video:
    t_begin = (0, 0, 0)
    t_end = (0, 0, 0)
    s_begin = (0, 0)
    s_end = (0, 0)
    filepath = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def begin_end_time(self, begin, end):
        self.t_begin = begin
        self.t_end = end

    # begin和end为区域左上角和右下角的位置
    def begin_end_space(self, begin, end):
        self.s_begin = begin
        self.s_end = end

    def cut_time(self):
        clip = VideoFileClip(self.filepath, audio=False, target_resolution=(240, None)).subclip(self.t_begin,
                                                                                                self.t_end)
        clip.write_images_sequence(
            nameformat=r'frame\frame%03d.png', fps=FPS)

    def cut_space(self):
        n = -((self.t_begin[0] - self.t_end[0]) * 60 + self.t_begin[1] - self.t_end[1]) * FPS
        for i in range(n):
            if i < 10:
                file = r'frame\frame00' + str(i)+'.png'
            elif i < 100:
                file = r'frame\frame0' + str(i)+'.png'
            elif i < 1000:
                file = r'frame\frame' + str(i)+'.png'
            else:
                file = None
            img = cv2.imread(file)
            cv2.imwrite(file, img[self.s_begin[0]:self.s_end[0], self.s_begin[1]:self.s_end[1]])

    def reunion(self):
        n = -((self.t_begin[0] - self.t_end[0]) * 60 + self.t_begin[1] - self.t_end[1]) * FPS
        gif_img=[]
        for i in range(n):
            if i < 10:
                file = r'frame\frame00' + str(i) + '.png'
            elif i < 100:
                file = r'frame\frame0' + str(i) + '.png'
            elif i < 1000:
                file = r'frame\frame' + str(i) + '.png'
            else:
                file = None
            gif_img.append(file)
        clip = ImageSequenceClip(gif_img,fps=FPS)
        clip.write_gif("expression.gif",fps=FPS)

    def cut(self):
        self.cut_time()
        self.cut_space()
        self.reunion()

if __name__ == "__main__":
    v = Video(r'.\baby.mp4')
    v.begin_end_time((0, 2), (0, 5))
    v.begin_end_space((100, 20), (200, 80))
    v.cut()
