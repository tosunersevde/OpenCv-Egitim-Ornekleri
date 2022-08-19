# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:17:45 2022

@author: tosun
"""

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("haarcascade_mouth.xml")

cam = cv2.VideoCapture(0)

while True:
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)
   
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)
    if len(faces)==0:
        cv2.putText(frame,"Yuz tespit Edilemedi!",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    else:
        for x,y,w,h in faces:
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
       
            mouth = mouth_cascade.detectMultiScale(roi_gray,1.7,22) 
            if len(mouth)==0:
                cv2.putText(frame,"Maske Var",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            else:
                for ix,iy,iw,ih in mouth:
                    cv2.rectangle(roi_color,(ix,iy),(ix+iw,iy+ih),(255,0,0),2)
                    cv2.putText(frame,"Maske Yok",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   
    cv2.imshow('Maske Tespiti',frame)
    
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

