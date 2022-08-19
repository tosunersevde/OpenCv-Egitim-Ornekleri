# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 10:49:18 2022

@author: tosun
"""

import cv2
import random

img = cv2.imread("C:/Users/tosun/spyder_projeler/images/gol.jpg",0)

x,y = img.shape[:2]

cv2.imshow("Goruntu",img)

for i in range(x-1):
    for j in range(y-1):
        sayi = random.randint(0,255)
        img[i,j] = sayi
        cv2.imshow("Yeni Goruntu",img)
        cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()
