#!/usr/python/bin
#-*- coding:UTF-8 -*-

################################################此代码将获取的帧图像，还原成视频#################################################

import os
import cv2

V_Type = '.avi'
video_path = 'V:\\Coding\\timesformer\\video_proc\\dataset'                   #存放源视频的根路径
frames_path = 'V:\\Coding\\timesformer\\video_proc\\chute01_cam1'             #帧图像文件夹
save_video = 'V:\\Coding\\timesformer\\video_proc\\video_result'              #保存output结果视频的path

class processing:
    def __init__(self, video_pth, frames_pth, v_type, save_pth):
        self.video_pth = video_pth
        self.frames_pth = frames_pth
        self.v_type = v_type
        self.save_pth = save_pth

    def make_video(self):
        video_source =self.get_ino()
        cap = cv2.VideoCapture(video_source)
        v_fps = cap.get(cv2.CAP_PROP_FPS)                                    #获取到对应源视频的FPS
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)                            #获取源视频的宽
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)                          #获取源视频的高

        n_1, n_2= self.get_video_name()
        save_v_name = n_1+'_'+n_2+self.v_type                                #对保存output视频的命名naming
        save_v_pth = os.path.join(self.save_pth, save_v_name)                #保存output视频的路径path 
        
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        video_writer = cv2.VideoWriter(save_v_pth, fourcc, v_fps, (int(width), int(height)))

        for i in os.listdir(self.frames_pth):
            i_path = os.path.join(self.frames_pth, i)
            frame = cv2.imread(i_path)
            video_writer.write(frame)
        video_writer.release()

    def get_ino(self):
        folder_name, cam_name = self.get_video_name()
        video_name = cam_name+self.v_type
        video_source = os.path.join(self.video_pth, folder_name, video_name)
        return video_source
    
    def get_video_name(self):
        root_level = self.frames_pth.split('\\')[-1]
        up_level = root_level.split('_')[0]                                  #得到源视频文件夹的存放cam的上一级目录
        down_level = root_level.split('_')[-1]                               #得到cam视频的name
        return up_level, down_level

def main():
    work = processing(video_path, frames_path, V_Type, save_video)
    work.make_video()

if __name__ == '__main__':
    main()