#!/usr/python/bin
#-*- coding:UTF-8 -*-
import os
import cv2

root_path = 'V:\\Coding\\timesformer\\flask\\dataset'

class get_frame:
    def __init__(self, root_pth):
        self.root_pth = root_pth

    def getting(self, v_pth):
        counter = 0
        cap = cv2.VideoCapture(v_pth)                                               #获取视频数据
        v_fps = cap.get(cv2.CAP_PROP_FPS)                                           #获取video_fps
        folder_pth = os.path.splitext(v_pth)
        if not os.path.exists(folder_pth[0]):
            os.mkdir(folder_pth[0])
        
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                counter += 1
                name = 'frame'+ str(counter) +'.jpg'
                save_pth = os.path.join(folder_pth[0], name)
                img = cv2.imwrite(save_pth, frame)
            else:
                counter = 0                                                         #置零, 进行下一个视频的帧处理
                cap.release()
                break

    def get_video(self):
        for root, folders, files in os.walk(self.root_pth):
            for f in files:
                file_pth = os.path.join(root, f)
                self.getting(file_pth)
                
def main():
    frames = get_frame(root_path)
    frames.get_video()
#    frames.getting()

if __name__ == '__main__':
    main()