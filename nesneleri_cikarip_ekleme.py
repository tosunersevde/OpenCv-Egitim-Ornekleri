# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:02:57 2022

@author: tosun
"""

import cv2
import numpy as np

path = "C:/Users/tosun/spyder_projeler/images/"

img = cv2.imread("C:/Users/tosun/spyder_projeler/images/vida.jpeg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, threshold_img = cv2.threshold(gray_img,169,255,cv2.THRESH_BINARY)

kernel = np.ones((6,6), np.uint8)
dilate_img = cv2.dilate(threshold_img,kernel,iterations = 11)

contours, hierarchy =cv2.findContours(dilate_img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

sayac = 0
for k in contours:
    x,y,w,h = cv2.boundingRect((k))
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    sayac+=1
    kirpilmis = img[y:y+h,x:x+w]
    cv2.imwrite("images/Kirpilmis/"+str(sayac)+"_kirpilmis"+".jpg",kirpilmis)
    x2,y2,z2 = kirpilmis.shape

    image2 = cv2.imread("C:/Users/tosun/spyder_projeler/images/vida.jpeg")
    img2 = image2[800:1027,1150:1377]

    x = int((227 - kirpilmis.shape[0])/2)
    y = int((227 - kirpilmis.shape[1])/2)
    
    img2[x:x2+x,y:y2+y] = kirpilmis
    # img2[90:x2+90,90:y2+90] = kirpilmis
    cv2.imwrite("images/227_227/"+str(sayac)+"_eklenmis"+".jpg",img2)

cv2.namedWindow("Vidalar",cv2.WINDOW_NORMAL)
cv2.namedWindow("Thresh",cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilate",cv2.WINDOW_NORMAL)

cv2.imshow("Vidalar",img)
cv2.imshow("Thresh",threshold_img)
cv2.imshow("Dilate",dilate_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
