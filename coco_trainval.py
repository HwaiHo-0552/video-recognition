#!/usr/bin/python
#-*- coding:UTF-8 -*-

##################################将数据集划分为train和val, 并生成txt文件############################################
#                                 此代码，首先读入所有json文件的name，然后按设置的比例%，                            #
#                                 随机得到val的数量，再计算得到train的数量，都存在各自的list中；再分别写入txt文件    #

import os
import random

data_path = 'V:\\Coding\\timesformer\\video_proc\\labels\\chute01_cam1'      #存放json文件夹的path
proportion = float(0.25)

class make_txt:
    def __init__(self, root_pth, propor):
        self.root_pth = root_pth
        self.propor = propor
    
    def getting_data(self):
        train_list = []
        counter = 0
        ds_list = os.listdir(self.root_pth)
        ds_total = len(ds_list)                                       #数据集总量
        val_total = int(ds_total*self.propor)                         #按比例计算后，验证集的总量
        val_list = random.sample(ds_list, val_total)                  #在总数据集中，随机得到val数量的文件
        for name in ds_list:
            for v_n in val_list:
                if name == v_n:
                    counter +=1
            if counter==0:
                train_list.append(name)
            counter=0
        
        root_txt = os.path.split(self.root_pth)[0]                   #获取json文件夹上一级目录path
        
        train_txt = os.path.join(root_txt, 'train.txt')
        self.write_2_txt(train_txt, train_list, './images/train/')   #得到train.txt文件

        val_txt = os.path.join(root_txt, 'val.txt')
        self.write_2_txt(val_txt, val_list, './images/val/')         #得到val.txt文件

    def write_2_txt(self, txt_pth, list_temp, pth):
        with open(txt_pth, 'w+', encoding='UTF-8') as f:
            for i in list_temp:
                img_name = i.split('.')[0]
                content = os.path.join(pth, img_name+'.jpg')
                f.writelines(content+'\n')
            f.close()

def main():
    work = make_txt(data_path, proportion)
    work.getting_data()

if __name__ == '__main__':
    main()