# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:24:55 2022

@author: tosun
"""

import cv2 

cam = cv2.VideoCapture(0)

mycascade = cv2.CascadeClassifier("C:/Users/tosun/spyder_projeler/mycascade/classifier/cascade.xml")

while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    pencils = mycascade.detectMultiScale(gray,1.3,7)
    
    for x,y,w,h in pencils:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,"Fosforlu Kalem",(x,y),cv2.FONT_HERSHEY_SIMPLEX,(0,255,0),2)
        
    cv2.imshow("Kalem Tespiti",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()
    