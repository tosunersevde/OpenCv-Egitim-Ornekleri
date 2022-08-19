# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:08:23 2022

@author: tosun
"""

import cv2
import numpy as np
import time
#import os

#11x11'lik matris elde ettim.
matris = np.array([[1,1,1,1,1,1,1,1,1,1,1], 
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,1,1,1,1,1,1,1,1]])


path = "C:/Users/tosun/spyder_projeler/images/kiz_kulesi.png"
image = cv2.imread(path,0)
img = cv2.resize(image,(227,227)) #resmi yeniden boyutlandirdim.
                 
img_x,img_y = img.shape
mat_a,mat_b = matris.shape
#h,w = a//2,b//2
print(img_x,img_y,mat_a,mat_b)

img_conv  = np.zeros(img.shape) #resmin boyutunda sifirlardan olusan dizi olusturdum.
img2 = np.zeros(img.shape)


for i in range(mat_a, img_x - mat_a):
    for j in range(mat_b, img_y - mat_b):
        toplam = 0
        for k in range(mat_a):
            for m in range(mat_b):
                toplam += matris[k][m] * img[i- mat_a +k][j- mat_b +m]
        img_conv[i][j] = toplam
        #print(img_conv[i][j])
#print(img_conv)
        
cv2.imshow("Yeni resim",img_conv)

cv2.waitKey(0)
        
cv2.destroyAllWindows()

