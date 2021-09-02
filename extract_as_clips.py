#!/usr/bin/python
#-*- coding:UTF-8 -*-
##########################################此代码功能是找到对应预测类别的frame###############################################
#################################然后以找到的这张frame为基，按时间轴向上取10帧frames########################################

import os
import shutil

preds_path = 'V:\\Coding\\timesformer\\video_proc\\video_result\\exp8\\labels'    #存放yolo预测的结果图path
source_path = 'V:\\Coding\\timesformer\\video_proc\\frames\\chute02_cam1'         #存放源图frames的path
save_path = 'V:\\Coding\\timesformer\\video_proc\\video_result\\training_data'    #待存的数据path

class extracting:
    def __init__(self, preds_frames, source_pth, save_pth):
        self.preds_frames = preds_frames
        self.source_pth = source_pth
        self.save_pth = save_pth

    def get_frames(self):
        list_frame = []
        for fm in os.listdir(self.preds_frames):           
            ab_pth = os.path.join(self.preds_frames, fm)
            with open(ab_pth, 'r', encoding='UTF-8') as f:
                lines = f.readlines()

            for c in lines:
                cls = c.strip().split(' ')[0]
                if cls == '1':
                    img_num = os.path.splitext(fm)[0]                            #判断此张frame是否包含筛选出来的类别
                    list_frame.append(img_num)
                    break
        return list_frame

    def proc_2_clips(self, list_fms):
        for fm in list_fms:
            save_folder = os.path.join(self.save_pth, fm)
            if os.path.exists(save_folder):
                shutil.rmtree(save_folder)
            os.mkdir(save_folder)
            num = fm.split('frame')[-1]
            for i in range(1, 101):
                f_n = int(num)-int(i)
                img = os.path.join(self.source_pth, ('frame'+str(f_n)+'.jpg'))
                shutil.copy(img, save_folder)                

def main():
    work = extracting(preds_path, source_path, save_path)
    list_frame = work.get_frames()
    work.proc_2_clips(list_frame)

if __name__ == '__main__':
    main()