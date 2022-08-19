# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:24:49 2022

@author: tosun
"""

import os
import cv2

def karsilastirma(path1,path2):
    img1= cv2.imread(path1)
    img2 = cv2.imread(path2)
    
    x1,y1 = img1.shape[:2]
    x2,y2 = img2.shape[:2]
    
    for i in range(x1-1):
        for j in range(y2-1):
            if not img1[i,j][2] == img2[i,j][2]:
                return False
            else:
                return True
            
def klasor_olusturma(path):
    cols = []
    klasorler = []
    dosyalar = os.listdir(path)
    
    for i,dosya in enumerate(dosyalar):
        if dosya.endswith(".jpg"):
            #print(dosya)
            img = cv2.imread(path+dosya)
            cols.append(img.shape[1])
            
            for j,col in enumerate(cols):
                newpath = path + str(col) +"_klasoru"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                    if not newpath in klasorler:
                        klasorler.append(newpath)
                if (cols[j] == img.shape[1]):
                    cv2.imwrite(newpath+"/"+dosya, img)

    for i in range(len(klasorler)):
        ayni_dosya(klasorler[i])
                    
def ayni_dosya(path):
    
    resimler = os.listdir(path)
    
    for i in range((len(resimler)-1)):
        #print(resimler[i])
        img1 = resimler[i]
        img2 = resimler[(len(resimler)-1)-i]
        path1 = path+ "/" + img1
        path2 = path+ "/" + img2

        if karsilastirma(path1,path2) == True:
            print("{}, {} Goruntuleri aynidir.".format(img1,img2))
        else:
            print("{}, {} Goruntuleri farklidir.".format(img1,img2))
                    
path = "C:/Users/tosun/spyder_projeler/images4/"
klasor_olusturma(path)


                    
#iki goruntu karsilastirma
"""if len(os.listdir(path)) > 1:
    img1 = cv2.imread(path+"/"+os.listdir(newpath)[0])
    img2 = cv2.imread(newpath+"/"+os.listdir(newpath)[1])"""

"""img1 = cv2.imread("C:/Users/tosun/spyder_projeler/images/goruntu1.jpg")
img2 = cv2.imread("C:/Users/tosun/spyder_projeler/images/goruntu2.jpg")

x1,y1 = img1.shape[:2]
x2,y2 = img2.shape[:2]

for i in range(x1-1):
    for j in range(y2-1):
        #pixel1 = img1[i,j]
        #pixel2 = img2[i,j]
        if img1[i,j][2] == img2[i,j][2]: #renk degerleri
            print("Goruntunun pixel degerleri aynidir!")
            break
        else:
            print("Bu iki goruntu farklidir!")
            break"""


            
            