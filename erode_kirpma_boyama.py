# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:10:34 2022

@author: tosun
"""

import cv2
import numpy as np

path = "C:/Users/tosun/spyder_projeler/images/karpuz.jpg"
img = cv2.imread(path)
img2 = cv2.imread(path)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((10,10), np.uint8)
kernel2 = np.ones((1,1), np.uint8)

cv2.namedWindow("Karpuz",cv2.WINDOW_NORMAL)
cv2.namedWindow("Kirpilmis",cv2.WINDOW_NORMAL)
cv2.namedWindow("Thresh",cv2.WINDOW_NORMAL)
cv2.namedWindow("Erode",cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilate",cv2.WINDOW_NORMAL)
cv2.namedWindow("Kirmizi",cv2.WINDOW_NORMAL)


ret,threshold_img = cv2.threshold(gray_img,190,255,cv2.THRESH_BINARY)

erode_img = cv2.erode(threshold_img,kernel,iterations = 50)

contours, hierarchy =cv2.findContours(erode_img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
       
for k in contours:
    x,y,w,h = cv2.boundingRect((k))
    kirpik_karpuz = img[y:y+h,x:x+w]
    cv2.imwrite("images/kirp_karpuz.jpg",kirpik_karpuz)
   
dilate_img = cv2.dilate(threshold_img,kernel2,iterations = 1)
dilate_img = cv2.bitwise_not(dilate_img)

contours, hierarchy =cv2.findContours(dilate_img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
kontur = cv2.drawContours(img2, contours, -1, (0,0,255),270)
       
for k in contours:
    x,y,w,h = cv2.boundingRect((k))
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),5)
    
cv2.imshow("Karpuz",img)
cv2.imshow("Thresh",threshold_img)
cv2.imshow("Erode",erode_img)
cv2.imshow("Dilate",dilate_img)
cv2.imshow("Kirpilmis",kirpik_karpuz)
cv2.imshow("Kirmizi",img2)



cv2.waitKey(0)
cv2.destroyAllWindows()