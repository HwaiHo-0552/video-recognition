#!/usr/python/bin
#-*- coding:UTF-8 -*-

################################################ 此代码将给定的frames #################################################
######################################## 制作成UCF101视频、帧图像的可训练格式 #########################################

import os
import cv2

V_Type = '.avi'
V_size = (320, 240)
frames_path = 'V:\\Coding\\timesformer\\video_proc\\video_result\\Lie'                                #待保持为视频的frame图像
save_video = 'V:\\Coding\\timesformer\\video_proc\\video_result'                                      #保存output结果视频的path

class processing:
    def __init__(self, frames_pth, v_type, save_pth, video_size):
        self.frames_pth = frames_pth
        self.v_type = v_type
        self.save_pth = save_pth
        self.video_size = video_size

    def make_video(self):
        v_fps = 25                                                                                         #FPS
        width = self.video_size[0]                                                                    
        height = self.video_size[1]                                                                   
        self.resize_img(width, height)
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

        for i in os.listdir(self.frames_pth):
            video_name = i+self.v_type
            save_v_pth = os.path.join(self.save_pth, video_name)
            video_writer = cv2.VideoWriter(save_v_pth, fourcc, v_fps, (int(width), int(height)))           #待保存视频的数据格式
            frames = os.path.join(self.frames_pth, i)
            frame_list = os.listdir(frames)
            frame_list.sort(key = lambda x : int(x.split('.')[0][4:]))
            for i in frame_list:
                i_path = os.path.join(frames, i)
                frame = cv2.imread(i_path)
                video_writer.write(frame)
            video_writer.release()

    def resize_img(self, re_width, re_height):                                                             #将帧图像的size进行修改
        for root, folders, files in os.walk(self.frames_pth):
            for f in files:
                img_pth = os.path.join(root, f)
                source_img = cv2.imread(img_pth)
                re_img = cv2.resize(source_img, (re_width, re_height), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(img_pth, re_img)

def main():
    work = processing(frames_path, V_Type, save_video, V_size)
    work.make_video()

if __name__ == '__main__':
    main()
