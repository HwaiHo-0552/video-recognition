#!/usr/python/bin
#-*- coding:UTF-8 -*-
import os
import cv2
import sys
import time
from tqdm import tqdm

root_path = 'V:\\Coding\\timesformer\\video_proc\\dataset'
save_path = 'V:\\Coding\\timesformer\\video_proc\\frames'

class get_frame:
    def __init__(self, root_pth, save_pth):
        self.root_pth = root_pth
        self.save_pth = save_pth

    def getting(self, v_pth):
        counter = 0

        cap = cv2.VideoCapture(v_pth)                                               #获取视频数据
        v_fps = cap.get(cv2.CAP_PROP_FPS)                                           #获取video_fps
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))                       #获取video的总帧数
        folder = os.path.splitext(v_pth)[0]
        folder_name = folder.split('\\')
        root_folder_pth = os.path.join(self.save_pth, folder_name[-2])
        folder_pth = os.path.join(root_folder_pth, folder_name[-1])
        if not os.path.exists(root_folder_pth):
            os.mkdir(root_folder_pth)
            os.mkdir(folder_pth)
        elif not os.path.exists(folder_pth):
            os.mkdir(folder_pth)

        for i in range(total_frames):        
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret==True:
                    counter += 1
                    part = round((counter/total_frames)*100)
                    if part>0:
                        sys.stdout.write('>>'*20 + '%s%%'%part)
                    prog = str(counter)+'/'+str(total_frames)
                    sys.stdout.write('\r'+'[%s]'%prog)   

                    name = 'frame'+ str(counter) +'.jpg'
                    save_pth = os.path.join(folder_pth, name)
                    img = cv2.imwrite(save_pth, frame)
                else:
                    counter = 0                                                         #置零, 进行下一个视频的帧处理
                    cap.release()
                    break
        print('\nFinish')
        print('-- '*20) 
    
    def get_video(self):
        for root, folders, files in os.walk(self.root_pth):                
            for f in files:
                file_pth = os.path.join(root, f)
                print(str(file_pth))
                self.getting(file_pth)

def main():
    frames = get_frame(root_path, save_path)
    frames.get_video()
#    frames.getting()

if __name__ == '__main__':
    main()