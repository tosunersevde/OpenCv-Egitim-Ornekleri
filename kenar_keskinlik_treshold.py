# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 09:47:04 2022

@author: tosun
"""

import cv2
import numpy as np
import matplotlib as plt

#%%  Bulaniklastirma islemi
images = cv2.imread("C:/Users/tosun/spyder_projeler/kalem.jpg",0)

ksize=(7,7) #Bulaniklasan cekirdek boyutu
blur =  cv2.blur(images,ksize)
gaussian_blur = cv2.GaussianBlur(images,ksize,cv2.BORDER_DEFAULT)
median_blur = cv2.medianBlur(images,15)

cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
cv2.namedWindow("Blur",cv2.WINDOW_NORMAL)
cv2.namedWindow("Gaussian_Blur",cv2.WINDOW_NORMAL)
cv2.namedWindow("Median_Blur",cv2.WINDOW_NORMAL)

cv2.imshow("Original Image",images)
cv2.imshow("Blur",blur)
cv2.imshow("Gaussian_Blur",gaussian_blur)
cv2.imshow("Median_Blur",median_blur)

#Tusa Basildiginda kapansin.
cv2.waitKey(0)

#Pencereleri Kapattim.
cv2.destroyAllWindows()

#%%

#Goruntuyu okudum.
img = cv2.imread("C:/Users/tosun/spyder_projeler/kalem.jpg",0)

#Resme uygulanacak matris
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

#kernel = np.array([[0,-1,0],[-1,9,-1],[0,-1,0]])
derinlik = -1 #Ciktinin derinligini giris ile ayni verir.

#Resmi keskinlestirdim.
img_sharpened = cv2.filter2D(img,derinlik,kernel)

#Kenarlari Belirginlestirdim.
"""edges = cv2.Canny(img,100,200)
edges_sharpened = cv2.Canny(img_sharpened,100,200)"""

cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.namedWindow("Sharpened",cv2.WINDOW_NORMAL)
"""cv2.namedWindow("Edges",cv2.WINDOW_NORMAL)
cv2.namedWindow("Edges Sharpened",cv2.WINDOW_NORMAL)"""

cv2.imshow("Original",img)
cv2.imshow("Sharpened",img_sharpened)
"""cv2.imshow("Edges",edges)
cv2.imshow("Edges Sharpened",edges_sharpened)"""

cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
img = cv2.imread("C:/Users/tosun/spyder_projeler/kalem.jpg",0)

#Resme treshhold yaptım.
esik_deger = 65 #Piksel değerlerinin değişeceği değer
max_deger = 255 #Bir pixele gelebilecek max deger
ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_BINARY)
#ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_BINARY_INV)
#ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_TOZERO)




cv2.imshow("Original",img)
cv2.imshow("Threshold",threshold_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.THRESH_BINARY: 
#Piksel yoğunluğu ayarlanan eşikten büyükse, değer 255'e degilse 0'a ayarlanır.
#cv.THRESH_TOZERO : 
#Piksel yoğunluğu, eşik değerinden daha düşük tüm piksel yoğunluğu için 0 olarak ayarlanır.

#%%
img = cv2.imread("C:/Users/tosun/spyder_projeler/images/top.jpg")

#Kenarlari Belirginlestirdim.
alt_esik = 100
ust_esik = 200
edges = cv2.Canny(img,alt_esik,ust_esik)

cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.namedWindow("Edges",cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
#img = cv2.imread("C:/Users/tosun/spyder_projeler/kalem.jpg",0)

"""cols = img.shape[0] // 100
rows = img.shape[1] //100"""

"""matris = np.array([[cols//100,0],[cols//100,rows//200],[cols//100,rows//100],
          [cols//90,0],[cols//90,rows//200],[cols//90,rows//100]])"""



