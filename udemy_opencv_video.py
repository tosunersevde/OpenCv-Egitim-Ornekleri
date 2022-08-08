# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:09:07 2022

@author: tosun
"""

import cv2

#Video oynatma
"""cam = cv2.VideoCapture("drone.mp4") #oynatilacak video

while cam.isOpened():
    
    ret , frame = cam.read()
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("Kameradan goruntu okunamiyor.")
        break
    
    cv2.imshow("goruntu",frame)
    
    if cv2.waitKey(1) &0xFF == ord("q"): #q'ya basilirsa kapansin
        print("Video Kapatildi.")
        break
    
cam.release()
cv2.destroyAllWindows()"""

#Video cekme
"""cam = cv2.VideoCapture(0)

#codec islemi
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
fourcc = cv2.VideoWriter_fourcc(*'XVID') #Boyutu daha az

out = cv2.VideoWriter("drone_gri.avi",fourcc,30.0,(640,480)) #Dad - codec - fps - boyut 


while cam.isOpened():
    ret , frame = cam.read()

    if not ret:
        print("Kameradan goruntu alinamadi.")
        break

    out.write(frame) #sablon icine frame goruntusu kaydedildi.
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"): #q'ya basilirsa kapansin
        print("Videodan Ayrildiniz.")
        break
    
cam.release()
out.release() #sablonu da kapatir.
cv2.destroyAllWindows()"""












