#!/usr/bin/python
#-*- coding:UTF-8 -*-
##################################制作coco数据集------train val文件夹############################################
#                                 通过train.txt和val.txt划分好的数据文件                                         #
#           分别读取文件名, 制作存放images和labels的train\val文件夹 for detection training读取数据               #
#root_path\  根路径
#          ->images文件夹，存放所有图像
#          ->annotations文件夹，存放所有json的GT信息
#          ->labels文件夹，根据json文件，制作对应的txt文件存放GT信息
#          ->train.txt文件，包含随机挑选的train文件
#          ->val.txt文件，包含随机挑选的val文件                                   
#          ->IMGs\
#                 ->train   存放train的images
#                 ->val     存放val的images
#          ->LABELs\
#                 ->train   存放train的txt文件
#                 ->val     存放val的txt文件
#此代码为了制作、并且“￥生成￥”出IMGs和LABELs及下一级folder和file

import os 
import shutil

root_path = 'V:\\Coding\\timesformer\\video_proc\\labels'                                   #根目录
image_path = 'V:\\Coding\\timesformer\\video_proc\\labels\\source_imgs'                     #源图像文件夹
label_path = 'V:\\Coding\\timesformer\\video_proc\\labels\\ground_truth'                    #源GT.json的文件夹
folder_imgs = 'IMGs'                                                                        #预设想定义的folder's name for 存放图像
folder_labels = 'LABELs'                                                                    #预设想定义的folder's name for 存放txt

class make_folder:
    def __init__(self, root_pth, img_pth, lbl_pth, name_I, name_L):
        self.root_pth = root_pth
        self.img_pth = img_pth
        self.lbl_pth = lbl_pth
        self.name_I = name_I
        self.name_L = name_L

    def getting_data(self):
        train_txt = os.path.join(self.root_pth, 'train.txt')
        val_txt = os.path.join(self.root_pth, 'val.txt')

        imgs_folder = os.path.join(self.root_pth, self.name_I)
        labels_folder = os.path.join(self.root_pth, self.name_L)

        train_imgs, val_imgs = self.build_folder(imgs_folder)                                #构建文件夹及子文件夹
        self.copy_file(self.img_pth, train_txt, train_imgs, '.jpg')                          #将得到的train名称文件copy至指定文件夹folder
        self.copy_file(self.img_pth, val_txt, val_imgs, '.jpg')                              #将得到的val名称文件copy至指定文件夹folder

        train_labels, val_labels = self.build_folder(labels_folder)
        self.copy_file(self.lbl_pth, train_txt, train_labels, '.txt')
        self.copy_file(self.lbl_pth, val_txt, val_labels, '.txt')

    def build_folder(self, folder_name):                                                    #构建文件夹folder及子文件夹
        if os.path.exists(folder_name):                                                     #获取path并判断，如果之前构建了，先删除，再构建folder及子folder
            shutil.rmtree(folder_name)
        os.makedirs(folder_name)
        train_pth = os.path.join(folder_name, 'train')
        val_pth = os.path.join(folder_name, 'val')
        os.makedirs(train_pth)
        os.makedirs(val_pth)

        return train_pth, val_pth
    
    def copy_file(self, folder_path, txt_temp, save_pth, type):
        with open(txt_temp, 'r+', encoding='UTF-8') as f:
            lines = f.readlines()
        for i in lines:
            content = i.strip('\n')                                                          #剔除txt中'\n'字符
            file = content.split('/')[-1]                                                    #剔除文件前缀的地址信息
            file_name = file.split('.')[0]+type                                              #获取文件的name+'后缀类型'
            f = os.path.join(folder_path, file_name)                                         #存放源数据的folder
            shutil.copy(f, save_pth)                                                         #copy至指定保存的path

def main():
    work = make_folder(root_path, image_path, label_path, folder_imgs, folder_labels)
    work.getting_data()

if __name__ == '__main__':
    main()