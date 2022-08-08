# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:30:45 2022

@author: tosun
"""

#Her bir piksel bir sayi
#Videolar saniyede cok fazla resim iceren
#cam.get() icersine sayi veya yazi yazarak kamera ozelliklerini ulasilabilir.
import cv2
import numpy as np

"""sifir = np.zeros((300,300))
bir = np.ones((300,300))

#cv2.imshow("sifir",sifir) #Kucuk bir matris olusuyor.
#cv2.imshow("bir",bir)

cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

cv2.waitKey(0)

cv2.destroyAllWindows()"""

"""cam = cv2.VideoCapture(0) #Bilgisayarin dahii kamerasi icin 0 kullanilir.

print(cam.get(3)) #Kamera ozelliklerini alma
print(cam.get(4))

cam.set(3,320) #Kamera ozelliklerini degistirme
cam.set(4,240)

print(cam.get(3))
print(cam.get(4))

if not cam.isOpened():
    print("Kamera taninamadi!")
    exit()

while True:
    ret, frame = cam.read() #ret kameradan deger okunuyor mu? True-false dondurur. Frame - cerceve
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Opencv goruntuyu BGR olarak okur. goruntuyu siyah-beyaz yapar.
    
    if not ret:
        print("Kameradan goruntu okunamiyor.")
        break
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) &0xFF == ord("q"): #cv2.waitKey(1) icerisine yazilan deger fazlaysa video yavaslamis gibi gorunur.
        print("Goruntu sonlandirildi.")
        break
    
cam.release() #Kamerayi kapatir.
cv2.destroyAllWindows() #tum pencereleri kapatir."""
