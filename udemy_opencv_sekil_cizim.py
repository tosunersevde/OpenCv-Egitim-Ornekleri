# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:32:04 2022

@author: tosun
"""

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #3 renk uzayinda, int pozitif degerler

#Cizgi cizme
"""cv2.line(img,(0,0),(512,512),(255,0,0),5) 
cv2.line(img,(50,400),(400,50),(0,255,0),10) 
#resim - x-y de konum - en soldan en saga - renk - kalinlik(pixel)"""

#Dikdortgen Cizme
"""#cv2.rectangle(img,(50,50),(300,300),(0,0,255),5)
cv2.rectangle(img,(50,50),(300,300),(0,0,255),5-1)
#resim - sol ust kose - sag alt kose - renk - kalinlik veya ic"""

#Cember Cizme
"""#cv2.circle(img,(255,255),60,(120,120,120),5)
cv2.circle(img,(100,100),90,(255,50,500),-1)
#resim - merkez konum - yaricap - renk - kalinlik veya ic"""

#Elips Cizme
"""cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3)
cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,100,0),-1)
#resim - merkez konum - uzunluk - aci - baslangic/bitis aci - renk - kalinlik veya ic"""

#Cokgen Cizme 
"""pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2 = pts.reshape(-1,1,2) #Satirlarin teker teker almasini saglar.

cv2.polylines(img,[pts],True,(255,255,255),-1)
#resim - noktalar - noktalar birlesir/kapali sekil - renk - kalinlik veya ic"""

#Yazi Yazma
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"OpenCv",(10,400),font,4,(0,155,255),2,cv2.LINE_AA)
#yazi - solt alt kose konum - boyut - duzgun goruntu

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()