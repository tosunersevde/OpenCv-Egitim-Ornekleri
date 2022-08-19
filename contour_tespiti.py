# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:42:53 2022

@author: tosun
"""

import cv2
import os
import numpy as np
import time

path = "C:/Users/tosun/spyder_projeler/images/"
for dosya in os.listdir(path):
    if dosya.endswith("blob.jpg"):
        print(dosya)
        image = cv2.imread(path+dosya)
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(image,(400,400))
      
        #Resme treshhold yaptım.
        esik_deger = 70
        max_deger = 255
        ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_BINARY)
        
        #Kenarlari Belirginlestirdim.
        alt_esik = 100
        ust_esik = 200
        edges = cv2.Canny(threshold_img,alt_esik,ust_esik)
        
        #Kontur bulmadan once baslangic zamani belirledim.
        baslangic_zamani = time.time()
        
        #Kontur Bulma
        countours,hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        #Konturlerin etrafina dikdortgen cizdim. 
        #Bos goruntuye bulunan kontur sayisini ve gecen zamani yazdirdim.
        for k in countours:
            x,y,w,h = cv2.boundingRect((k))
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,0),2)
            
            bir = np.ones((500,500))
            
            cv2.putText(bir,"Kontur:",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
            cv2.putText(bir,str(len(countours)),(30,90),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
            
            cv2.putText(bir,"Saniye:",(30,130),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
            cv2.putText(bir,str(time.time()-baslangic_zamani),(30,170),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
            
            cv2.imshow("Sayi",bir)
        
        
        print("Bulunan kontur sayisi: " + str(len(countours)))
        
        cv2.imshow("Goruntu",img)
        
        cv2.waitKey(0)
        
cv2.destroyAllWindows
        