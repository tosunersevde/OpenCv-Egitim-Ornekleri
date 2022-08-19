# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:44:44 2022

@author: tosun
"""

import cv2
#import numpy as np

image = cv2.imread("C:/Users/tosun/spyder_projeler/images/daireler.jpg")
img = cv2.resize(image,(500,500))
#cv2.imshow("Goruntu",img)

#Resme treshhold yaptım.
esik_deger = 65
max_deger = 255
ret,threshold_img = cv2.threshold(img,esik_deger,max_deger,cv2.THRESH_BINARY)

#Kenarlari Belirginlestirdim.
alt_esik = 100
ust_esik = 200
edges = cv2.Canny(threshold_img,alt_esik,ust_esik)

#Kontur Bulma
countours,hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#Toplam Kontur Sayisi
print("Bulunan kontur sayisi: " + str(len(countours)))

#Konturleri Belirleme
sayac = 0
for k in countours:
    sayac +=1
    x,y,w,h = cv2.boundingRect((k))
    cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,0),2)
    kirp = img[y:h+y,x:w+x]
    cv2.imwrite("images/kirp"+str(sayac)+".jpg",kirp) #Konturleri kesip kaydetme
    
    #Sinirda Olan Konturleri Bulma
    if x==0 or y==0 or x+w==0 or y+h==0 or x==500 or y==500 or x+w==500 or y+h==500:
        cv2.rectangle(img,(x,y),(w+x,h+y),(255,0,0),2)
  
#Kontur Buyukluk Bulma
for i in range(len(countours)):
    area = cv2.contourArea(countours[i])
    print(area)

#En Buyuk Konturu Bulma
max_area = -1
for i in range(len(countours)-1):
    area = cv2.contourArea(countours[i])
    if area > max_area:
        max_area = area             
print("Max Area: ",max_area)
    

#☼cv2.imshow("Konturlar",kontur)
cv2.imshow("Konturlar",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#%%
import cv2

img = cv2.imread("C:/Users/tosun/spyder_projeler/images/kiz_kulesi.png")

kirp = img[125:800,750:1525]

cv2.imshow("Goruntu",img)
cv2.imshow("Kirp",kirp)

cv2.waitKey(0)
cv2.destroyAllWindows()





