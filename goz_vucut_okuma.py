# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:34:16 2022

@author: tosun
"""

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml") #Dosyalari kullanilabilir hale getirme
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye_tree_eyeglasses.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_upperbody.xml")
lowerbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_lowerbody.xml")

cam = cv2.VideoCapture(0)

while True:
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)
   
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5) #Yuz tespiti
    upperbody = upperbody_cascade.detectMultiScale(gray,1.1,5) #min(50,100)
    lowerbody = lowerbody_cascade.detectMultiScale(gray,1.1,5)
    
    for x,y,w,h in faces:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #Yuz cevresine dikdortgen
   
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3) #Goz tespiti
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            
        smile = smile_cascade.detectMultiScale(roi_gray,1.7,22) #Gulucuk tespiti
        for ix,iy,iw,ih in smile:
            cv2.rectangle(roi_color,(ix,iy),(ix+iw,iy+ih),(255,0,0),2)
        
    for ux,uy,uw,uh in upperbody:
        cv2.rectangle(frame,(ux,uy),(ux+uw,uy+uh),(0,0,255),2)
        
    for lx,ly,lw,lh in lowerbody:
        cv2.rectangle(frame,(lx,ly),(lx+lw,ly+lh),(0,0,255),2)
   
    
    cv2.imshow('Yuz Tanima',frame)
    
    if cv2.waitKey(1) == ord("q"): #q'ya basilirsa kapansin
        break

cam.release() #kamerayi kapatir.
cv2.destroyAllWindows()
