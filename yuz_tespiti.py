# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:46:06 2022

@author: tosun
"""

import cv2
import os

path = "C:/Users/tosun/spyder_projeler/images/" #dosya yolu
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml") #Dosyayi kullanilabilir hale getirme

for dosya in os.listdir(path):
    if dosya.endswith("kisi.jpg"):
        print(dosya)
        
        image = cv2.imread(path+dosya)
        img = cv2.resize(image,(1000,1000))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #resmi gri yapar.
        faces = face_cascade.detectMultiScale(gray,1.1,3) #Resimde yuz bulmak icin
        for x,y,w,h in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #yuz cevresine dikdortgen
        
        cv2.imshow("Goruntu",img) 
        cv2.waitKey(1000)
    
    if cv2.waitKey(1) == ord("q"): #q'ya basilirsa kapansin
        break

cv2.destroyAllWindows()



#%%
#Video Okuma
        
#path = "C:/Users/tosun/spyder_projeler/xml_dosya/" #resimlerin bulundugu dosya yolu
cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml") #Dosyalari kullanilabilir hale getirme

while True:
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)
   
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #resmi gri yapar.
    faces = face_cascade.detectMultiScale(gray,1.3,5) #Resimde yuz bulmak icin
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #yuz cevresine dikdortgen
   
    cv2.imshow('Yuz Tanima',frame)
    #cv2.imshow("Goruntu",dosya)
    
    if cv2.waitKey(1) == ord("q"): #q'ya basilirsa kapansin
        break

cam.release() #kamerayi kapatir.
cv2.destroyAllWindows()

    