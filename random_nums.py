#!/usr/bin/python
#-*- coding:UTF-8 -*-
                                                # SAIL LAB 机器学习研发 2021.9.7
                                                # 此代码功能是将数据集打乱, 
                                                # 生成train-75% val-25%的随机编号, 
                                                # 写入txt文件中, 仿照UCF数据格式, 
                                                # 再生成多个不同的list
import os
import random

n_s = 3
classs = 102
root_path = 'V:\\Coding\\timesformer\\video_proc\\video_result\\Lie_videos'
save_path = 'V:\\Coding\\timesformer\\video_proc\\video_result\\'

class make_dataset:
    def __init__(self, roots, saved, n_slices, cls):
        self.roots = roots
        self.saved = saved
        self.n_slices = n_slices
        self.cls = cls

    def proc(self):
        videos = [video for video in os.listdir(self.roots)]
        val_nums = int(len(videos)*float(0.25))                                        #随机生成25%的编号
        temp_i = random.sample( range(0, len(videos)-1), val_nums )
        list_val = [videos[i] for i in temp_i]                                         
        for i in list_val:                                                                 
            videos.remove(i)                                                           #将25%的val数据delete, 保留75%的数据用于train

        self.write_txt(self.saved, 'train_list.txt', videos)                           #保存记录train编号的list
        self.write_txt(self.saved, 'val_list.txt', list_val)                           #保存记录val编号的list

        self.split_nslice(videos, 'train')                                             #将train划分为n slices并写入txt
        self.split_nslice(list_val, 'val')                                             #将val划分为n slices并写入txt

    def split_nslice(self, temp_list, func):
        total_nums = len(temp_list)
        for n in range(1, self.n_slices):                                              #循环n-1次, 写入n-1 slices的编号list
            part_nums = int(total_nums*float(0.30))
            temp_i = random.sample( range(0, len(temp_list)-1), part_nums)
            list_rest = [temp_list[i] for i in temp_i]
            for i in list_rest:
                temp_list.remove(i)
            content = func+'list0'+str(n)+'.txt'
            self.write_txt(self.saved, content, list_rest)                            
       
        content = func+'list0'+str(self.n_slices)+'.txt'
        self.write_txt(self.saved, content, temp_list)                                 #将剩余的一部分写入编号的list

    def write_txt(self, temp_pth, named, temp_list):
        temp_txt = os.path.join(temp_pth, named)
        w_t = open(temp_txt, 'w+', encoding='UTF-8')
        for i in temp_list:
            content = 'Lie/'+i+' '+str(self.cls)+'\n'
            w_t.writelines(content)
        w_t.close()

def main():
    work = make_dataset(root_path, save_path, n_s, classs)
    work.proc()

if __name__ == '__main__':
    main()