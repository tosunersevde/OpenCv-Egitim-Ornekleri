# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:06:24 2022

@author: tosun
"""
import cv2
import numpy as np
import matplotlib as plt

image = cv2.imread("C:/Users/tosun/spyder_projeler/images/kalem.jpg",0)
img = cv2.resize(image,(300,300))

#Resme treshhold yaptım.
esik_deger = 65
max_deger = 255
ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_BINARY)

#Matris Degerlerini Buldum.
x2,y2 = threshold_img.shape[:2]
for x1 in range(x2-1):
    for y1 in range(y2-1):
        if threshold_img[x1,y1] == 0:
            if threshold_img[(x1+1),y1] == 255:
                cv2.circle(img,(y1,x1),1,(0,255,0),-1)
                print(x1,y1,threshold_img[x1,y1])
            if threshold_img[x1,(y1+1)] == 255:
                cv2.circle(img,(y1,x1),1,(0,255,0),-1)
                print(x1,y1,threshold_img[x1,y1])
        if threshold_img[x1,y1] == 255:
            if threshold_img[(x1+1),y1] == 0:
                cv2.circle(img,(y1,x1),1,(0,255,0),-1)
                print(x1,y1,threshold_img[x1,y1])
            if threshold_img[x1,(y1+1)] == 0:
                cv2.circle(img,(y1,x1),1,(0,255,0),-1)
                print(x1,y1,threshold_img[x1,y1])

cv2.imshow("Original",img)
cv2.imshow("Threshold",threshold_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
import cv2
import numpy as np
import matplotlib as plt

image = cv2.imread("C:/Users/tosun/spyder_projeler/images/kalem.jpg",0)
img = cv2.resize(image,(300,300))

#Resme treshhold yaptım.
esik_deger = 65
max_deger = 255
ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_BINARY)

#Kenarlari Belirginlestirdim.
alt_esik = 100
ust_esik = 200
edges = cv2.Canny(threshold_img,alt_esik,ust_esik)

#Kontur Bulma
countour,hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#print("Bulunan kontur sayisi: " + str(len(countour)))

#Konturlerin Cizimi
kontur = cv2.drawContours(img, countour, -1, (0,0,255),3)
#-1 parametresi kullanilarak tum hepsi cizdirilir

cv2.imshow("Original",img)
cv2.imshow("Threshold",threshold_img)
cv2.imshow("Edges",edges)
cv2.imshow("Konturlar",kontur)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.CHAIN_APPROX_NONE - tum sinir noktalari saklanir.




