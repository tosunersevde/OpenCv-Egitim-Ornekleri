# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:00:14 2022

@author: tosun
"""

import cv2
import numpy  as np

def mutlak_deger(a,b):
    if a>b:
        return a-b
    elif b>a:
        return b-a
    else:
        return 0

img1 = cv2.imread("C:/Users/tosun/spyder_projeler/images/su.jpg",0)
img2 = cv2.imread("C:/Users/tosun/spyder_projeler/images/cicek.jpg",0)

cv2.imshow("Goruntu1",img1)
cv2.imshow("Goruntu2",img2)

x1,y1 = img1.shape[:2]
x2,y2 = img2.shape[:2]

img3 = np.zeros((x1,y1),np.uint8)

cv2.imshow("Goruntu3",img3)

for i in range(x1):
    for j in range(y1):
        sayi1 = img1[i,j]
        sayi2 = img2[i,j]
        sonuc = mutlak_deger(sayi1,sayi2)
        #print(sonuc)
        img3[i,j] = sonuc
        

cv2.imshow("Yeni Goruntu",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

        

