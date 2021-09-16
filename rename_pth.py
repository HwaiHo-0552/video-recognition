#!/usr/bin/python
#-*- coding:UTF-8 -*-

###################################此代码是改写txt文件中的内容，重新保存至新txt中###################################
###################################      2021.9.16 sail lab in Soochow          ###################################

import os

txt_path = 'V:\\Coding\\food recognition\\food101\\food101\\rename\\test.txt'
add_content = '/home/maxiaozhi/project/object_detection/one_stage/dark_net/darknet/data/food101/images/'

class renaming:
    def __init__(self, txt_pth, add_c):
        self.txt_pth = txt_pth
        self.add_c = add_c

    def rening(self):
        with open(self.txt_pth, 'r+', encoding='UTF-8') as file:
            lines = file.readlines()

        old_c = [i.strip()+'.jpg' for i in lines]
        
        file_pth = self.txt_pth.split('\\')[:-1]
        file_last = self.txt_pth.split('\\')[-1]
        file_name = file_last.split('.')[0]+'.list'
        file_pth.append(file_name)
        up_l = file_pth[0]+'\\'
        for i in range(1, len(file_pth)):
            file_p = os.path.join(up_l, file_pth[i])
            up_l = file_p
        
        file = open(file_p, 'w+', encoding='UTF-8')

        for i in old_c:
            n_content = self.add_c+i+'\n'
            file.writelines(n_content)
        file.close()

def main():
    work = renaming(txt_path, add_content)
    work.rening()

if __name__ == '__main__':
    main()