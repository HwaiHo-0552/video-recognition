#!/usr/bin/python
#-*- coding:UTF-8 -*-
##################################制作coco数据集------标签txt文件############################################


import os
import json

mapping = {'step':'0', 'lie':'1'}
json_path = 'V:\\Coding\\timesformer\\video_proc\\labels\\chute01_cam1'   #存放ground truth的json数据格式，文件夹目录
save_path = 'V:\\Coding\\timesformer\\video_proc\\labels\\ground_truth'   #准备保存的txt的路径


class get_info:
    def __init__(self, json_pth, save_pth, map):
        self.json_pth = json_pth
        self.save_pth = save_pth
        self.map = map
    
    def read_write(self):                                              #此段函数是将读入json的GT-类别、坐标信息写入txt中
        for i in os.listdir(self.json_pth):
            name = i.split('.')[0]
            ab_path = os.path.join(self.json_pth, i)
            gt_infos = self.getting(ab_path)
            txt_pth = os.path.join(self.save_pth, name+'.txt')
            with open(txt_pth,'w+', encoding='UTF-8') as f:
                for gt in gt_infos:
                    for nums, i in enumerate(gt):
                        if nums==(len(gt)-1):
                           f.write(str(i)+'\n')
                        else:
                           f.write(str(i)+' ')                    
                f.close()

    def getting(self, pth):                                         #此段函数是爬取json中需要的GT信息
        GT=[]
        f = open(pth)
        t = json.load(f)
        gt_infos = t['shapes']
        for gt in gt_infos:
            label_n = gt['label']
            gt_map = self.map[label_n]
            points = gt['points']
            x = points[0][0]
            y = points[0][1]
            w = points[1][0]
            h = points[1][1]
            info = [gt_map, x, y, w, h]
            GT.append(info)

        return GT

def main():
    work = get_info(json_path, save_path, mapping)
    work.read_write()

if __name__ == '__main__':
    main()