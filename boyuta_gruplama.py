# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:01:42 2022

@author: tosun
"""

import cv2
import os
import shutil
import time

baslangic = time.time()
path = "C:/Users/tosun/spyder_projeler/images3/"

for i in os.listdir(path):
    if i.endswith(".jpg"):
        #print(i)
        img = cv2.imread(path+i)
        x,y = img.shape[:2]
        
        if y == 640:
            new_path = "C:/Users/tosun/spyder_projeler/images2/640_img"
            if os.path.exists(new_path):
                shutil.move(path+i,new_path)
            else:
                os.mkdir(new_path)
                shutil.move(path+i,new_path)
        
        elif y == 1920:
            new_path = "C:/Users/tosun/spyder_projeler/images2/1920_img"
            if os.path.exists(new_path):
                shutil.move(path+i,new_path)
            else:
                os.mkdir(new_path)
                shutil.move(path+i,new_path)
        
        elif y == 2400:
            new_path = "C:/Users/tosun/spyder_projeler/images2/2400_img"
            if os.path.exists(new_path):
                shutil.move(path+i,new_path)
            else:
                os.mkdir(new_path)
                shutil.move(path+i,new_path)

saniye = time.time() - baslangic
gecen_zaman = saniye * (10**3)
print("Milisaniye:",gecen_zaman)
