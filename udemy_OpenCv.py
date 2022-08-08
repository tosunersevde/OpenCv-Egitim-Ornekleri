# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:46:15 2022

@author: tosun
"""

#resim bir matristir.
import cv2
from matplotlib import pyplot as plt

#resim = cv2.imread("kiz_kulesi.png") #resim okuma islemi
resim = cv2.imread("kiz_kulesi.png",0) #resmi siyah beyaz yapar.

cv2.imshow("resim penceresi",resim)

#cv2.namedWindow("resim",cv2.WINDOW_AUTOSIZE) #Bos bir resim cercvesi olustutrur.
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",resim)


plt.imshow(resim,cmap="gray") #0-siyah beyaz-255
plt.show()

#cv2.waitKey(0) #Beklemesi icin

k = cv2.waitKey(0) #0xFF - numlock tusu - aktif pasif
print(k) #Kapatmak icin bastigimiz tusun degerini de gosterir.

if k == 27:
    print("ESC tusuna basildi")
    
elif k == ord("q"): #direk tus adi verilebilir.
    print("q tusuna basildi, resim kaydedildi.") 
    cv2.imwrite("kizkulesi_gri.png",resim) #resim kaydetme islemi
    
#cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows() #Tum tuslara basilarak kapatma islemi yapilabilir.






