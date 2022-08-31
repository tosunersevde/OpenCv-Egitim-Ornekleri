# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:46:20 2022

@author: tosun
"""
import cv2
import numpy as np
#import os

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
    sayac+=1
    kirpilmis = img[y:y+h,x:x+w]
    cv2.imwrite("images/Kirpilmis/"+str(sayac)+"_kirpilmis"+".jpg",kirpilmis)
    x,y,z = kirpilmis.shape
    print(kirpilmis.shape)
    
    image2 = cv2.imread("C:/Users/tosun/spyder_projeler/images/vida.jpeg")
    
    img2 = image2[800:1024,1150:1374] #224 #Goruntunun bos oldugu kısım.
    x2,y2,z2 = img2.shape
    h = int((x2 - kirpilmis.shape[0])/2)
    w = int((y2 - kirpilmis.shape[1])/2)
    img2[h:x+h,w:y+w] = kirpilmis
    cv2.imwrite("images/224_224/"+str(sayac)+"_eklenmis"+".jpg",img2)
    
    img3 = image2[800:1027,1150:1377] #227
    x3,y3,z3 = img3.shape
    h = int((x3 - kirpilmis.shape[0])/2)
    w = int((y3 - kirpilmis.shape[1])/2)
    img3[h:x+h,w:y+w] = kirpilmis
    cv2.imwrite("images/227_227/"+str(sayac)+"_eklenmis"+".jpg",img3)
    
    img4 = image2[568:1080,928:1440]  #512
    x4,y4,z4 = img4.shape      
    h = int((x4 - kirpilmis.shape[0])/2)
    w = int((y4 - kirpilmis.shape[1])/2)       
    img4[h:x+h,w:y+w] = kirpilmis
    cv2.imwrite("images/512_512/"+str(sayac)+"_eklenmis"+".jpg",img4)


cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
import cv2
import numpy as np
#import os

path = "C:/Users/tosun/spyder_projeler/images/"

image3 = cv2.imread("C:/Users/tosun/spyder_projeler/images/vida.jpeg",0)

ret, threshold_img = cv2.threshold(image3,169,255,cv2.THRESH_BINARY)

kernel = np.ones((6,6), np.uint8)
dilate_img = cv2.dilate(threshold_img,kernel,iterations = 11)

contours, hierarchy =cv2.findContours(dilate_img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

sayac = 0
for k in contours:
    x,y,w,h = cv2.boundingRect((k))
    sayac+=1
    kirpilmis = image3[y:y+h,x:x+w]
    cv2.imwrite("images/Kirpilmis2/"+str(sayac)+"_kirpilmis"+".jpg",kirpilmis)
    x,y = kirpilmis.shape
    print(kirpilmis.shape)
    
    if x<=128 and y<=128:
        image3 = cv2.imread("C:/Users/tosun/spyder_projeler/images/vida.jpeg",0)
        img5 = image3[800:928,1150:1278]  #128 
        x5,y5 = img5.shape
        h = int((x5 - kirpilmis.shape[0])/2)
        w = int((y5 - kirpilmis.shape[1])/2)
        img5[h:x+h,w:y+w] = kirpilmis
        cv2.imwrite("images/128_128/"+str(sayac)+"_eklenmis"+".jpg",img5)
        img5_1 = img5[0 : x5//2,  0 : y5//2]
        img5_2 = img5[0 : x5//2, y5//2 : y5+(y5//2)]
        img5_3 = img5[x5//2 : x5+(x5//2), 0 : y5//2]
        img5_4 = img5[x5//2 : x5+(x5//2) ,y5//2 : y5+(y5//2)]
        cv2.imwrite("images/128_128/bolunen/"+str(sayac)+"_bolunen1"+".jpg",img5_1)
        cv2.imwrite("images/128_128/bolunen/"+str(sayac)+"_bolunen2"+".jpg",img5_2)
        cv2.imwrite("images/128_128/bolunen/"+str(sayac)+"_bolunen3"+".jpg",img5_3)
        cv2.imwrite("images/128_128/bolunen/"+str(sayac)+"_bolunen4"+".jpg",img5_4)


    img6 = image3[664:1080,1024:1440]  #416
    x6,y6 = img6.shape 
    h = int((x6 - kirpilmis.shape[0])/2)
    w = int((y6 - kirpilmis.shape[1])/2)
    img6[h:x+h,w:y+w] = kirpilmis
    cv2.imwrite("images/416_416/"+str(sayac)+"_eklenmis"+".jpg",img6)
    

cv2.waitKey(0)
cv2.destroyAllWindows()