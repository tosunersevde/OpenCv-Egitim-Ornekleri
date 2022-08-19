# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:52:59 2022

@author: tosun
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/tosun/spyder_projeler/images/yildizlar.jpg",0)

#Resme uygulanacak matris
kernel = np.ones((3,3), np.uint8)

#Goruntuye erode -asindirma, dilate-genisleme uyguladim.
erode_img = cv2.erode(img, kernel) 
dilate_img = cv2.dilate(img,kernel)
  
cv2.imshow("Original",img)
cv2.imshow("Erode Image",erode_img)
cv2.imshow("Dilate Image",dilate_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#dilate: parlak alanlar genisler. 

#%%
#camera video cekme

import cv2

cam = cv2.VideoCapture(0) #dahili camera icin 

frame_width = int(cam.get(3))
frame_height = int(cam.get(4))
   
size = (frame_width, frame_height)
   
out = cv2.VideoWriter('Camera.avi',cv2.VideoWriter_fourcc(*'MJPG'),30, size)
#saniyede fps kadar goruntu okuyor.
 
goruntu_sayi =0
while cam.isOpened():
    ret , frame = cam.read()
    goruntu_sayi+=1

    if not ret:
        print("Kameradan goruntu alinamadi.")
        break

    out.write(frame) #sablon icine frame goruntusu kaydedildi.
    
    cv2.imshow("Frame",frame)
    
    if cv2.waitKey(1) == ord("q"): #q'ya basilirsa kapansin
        print("Goruntu_sayisi: ",goruntu_sayi)
        print("Videodan Ayrildiniz.")
        break
    
cam.release()
out.release() #sablonu da kapatir.
cv2.destroyAllWindows()


