# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 09:44:07 2022

@author: tosun
"""

"""for i in dir(cv2):
    if 'EVENT' in i:
        print(i)"""

import cv2
import numpy as np

cizim = False
mod = False
xi,yi = -1,-1 #Baslangic koordinat

def draw(event,x,y,flags,param):
    #print(x,y) #Farenin gezdigi yerde koordinatlari yazar.
    """if event == cv2.EVENT_LBUTTONDBLCLK: #Cift tiklanirsa
        cv2.circle(img,(x,y),50,(255,0,0),-1) #Tiklanan yere daire cizer."""
        
    global cizim
    global xi,yi,mod
    
    if event == cv2.EVENT_LBUTTONDOWN: #Mouse'a basildigi surece
        xi,yi = x,y
        cizim = True
    elif event == cv2.EVENT_MOUSEMOVE: #Mouse'a hareket ettirrilirse
        if cizim == True:
            if mod:   
                cv2.circle(img,(x,y),5,(100,50,0),-1)
            else:
                cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),-1)
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP: #Mouse birakilirsa
        cizim = False
        if mod:   
                cv2.circle(img,(x,y),5,(100,50,0),-1)
        else:
            cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),-1)
    

img = np.ones((512,512,3),np.uint8)

cv2.namedWindow("paint")

cv2.setMouseCallback("paint",draw)

while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod
    
cv2.destroyAllWindows()


