#!/usr/bin/python
#-*- coding:UTF-8 -*-
#####################################  此代码功能是将YOLOV5预测得到的结果文件夹及文件名称 ###############################################
#####################################        重新命名为C3D可训练的数据类型名称            ###############################################
import os

folder_pth = 'V:\\Coding\\timesformer\\video_proc\\video_result\\Lie'
up_name = 'v_Lie_g01_c'
low_name = 'img_'

class proc:
    def __init__(self, fp, folder_name, file_name):
        self.fp = fp
        self.folder_name = folder_name
        self.file_name = file_name

    def modify(self):
        for root, folders, files in os.walk(self.fp):
            for fo in folders:
                folder_path = os.path.join(root, fo)
                name_dict, name_list = self.get_info(folder_path)
                self.rename(folder_path, name_dict, name_list, True)               #修改文件图片的名称

        name_dict, name_list = self.get_info(self.fp)
        self.rename(self.fp, name_dict, name_list, False)                          #修改文件夹的名称
    
    def get_info(self, ab_path):
        name_dict = {}
        name_list = []
        for i in os.listdir(ab_path):
            name = i.split('frame')[-1]
            name_dict[name] = i
            name_list.append(name)
        name_list.sort()

        return name_dict, name_list
    
    def rename(self, ab_pth, ndict, nlist, img):
        for loc, key in enumerate(nlist):
            if img==True:
                new_name = self.file_name + str(int(loc)+1).zfill(4) + '.jpg'
            else:
                new_name = self.folder_name + str(int(loc)+1).zfill(3)
            old_folder_name = os.path.join(ab_pth, ndict[key])
            new_folder_name = os.path.join(ab_pth, new_name)
            os.rename(old_folder_name, new_folder_name)

def main():
    work = proc(folder_pth, up_name,  low_name)
    work.modify()

if __name__ == '__main__':
    main()