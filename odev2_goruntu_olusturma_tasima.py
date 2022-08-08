# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 09:53:26 2022

@author: tosun
"""
#Kutuphaneleri tanimladim.
import cv2
import numpy as np

#Sifir ve birlerden olusan matrisler olusturdum.
sifir = np.zeros((500,500))
bir = np.ones((500,500))

#Resim gosterecek pencere olusturdum.Pencereye isim verdim. 
#Pencere boyutunu manuel olarak değiştirebilecegim sekilde ayarladim.
cv2.namedWindow("Siyah Resim",cv2.WINDOW_NORMAL)
cv2.namedWindow("Beyaz Resim",cv2.WINDOW_NORMAL)

#Pencereyi goruntuledim. Resmin ismini ve goruntulecek resmi verdim. 
cv2.imshow("Siyah Resim",sifir)
cv2.imshow("Beyaz Resim",bir)

#Herhangi bir tuşa basılana kadar pencereyi goruntulenmesini sagladim.
cv2.waitKey(0)

#Tüm pencerelerin kapatilmasini sagladim.
cv2.destroyAllWindows()

#%%
#Kutuphaneleri tanimladim.
import cv2
import numpy as np
import os
import shutil

#Birlerden olusan matrisler olusturdum.
#bir = np.ones((500,500))

#Resim gosterecek bos pencere olusturdum.Pencereye isim verdim. 
#Pencere boyutunu otomatik sekilde ayarladim.
#cv2.namedWindow("Bos Goruntu",cv2.WINDOW_AUTOSIZE)

#Pencereyi goruntuledim. Resmin ismini ve goruntulecek resmi verdim. 
#cv2.imshow("Bos Goruntu",bir)

#Goruntu Okudum.
#img = cv2.imread("kiz_kulesi.png")

#Goruntuyu kaydettim.
#cv2.imwrite("kiz_kulesi2.jpg",img)

#RGB'den grayscole cevirdim.
#gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Orta pixel degerini okudum.
"""cols = img.shape[0] // 2
rows = img.shape[1] // 2
orta_deger = img[cols][rows]
ortadeger2 = gray_img[cols][rows]"""

#Belirli pixel degerlerini okudum.
"""pixel_orta = [img.shape[0] // 2, img.shape[1] // 2]
print("Orta Pixel:" ,pixel_orta)"""

#RGB'yi HSV degerine donusturdum.
#hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
#♣goruntu resize edilecek 227 227
#5 Goruntu Okudum. Ismini Degistirdim.
"""sayac = 0
for dosya in os.listdir("C:/Users/tosun/Downloads/"):
    if dosya.endswith("unsplash.jpg"):
        sayac+=1
        print(dosya)
        resim = cv2.imread("C:/Users/tosun/Downloads/" +dosya)
        cv2.imwrite("resim" +str(sayac)+".jpg",resim)"""
        
#enumarate ile yap
"""sayac = 0
path = "C:/Users/tosun/Downloads/" #resimlerin bulundugu dosya yolu
for dosya in os.listdir(path):
    if dosya.endswith("unsplash.jpg"):
        sayac+=1
        print(dosya)
        resim = cv2.imread(path +dosya)
        cv2.imwrite("resim" +str(sayac)+".jpg",resim)
        if sayac == 5:
            break

count = 0
for resim in os.listdir("C:/Users/tosun/spyder_projeler"):
    count+=1
    os.rename("resim"+str(count)+".jpg","Resim" +str(count)+".jpg")"""

#Goruntuyu tasidim.    
sayac = 0
path = "C:/Users/tosun/Downloads/" #resimlerin bulundugu dosya yolu
new_path = "C:/Users/tosun/Downloads/Klasor_Resim" #Olusturulacak klasor
if os.path.exists(new_path): #Belirtilen klasor varsa
    for dosya in os.listdir(path):
        if os.path.exists(path): #Resimler varsa
            if dosya.endswith("unsplash.jpg"):
                sayac+=1
                print(dosya)
                shutil.move(path+dosya,new_path)
        else:
            print("Tasinacak resimler Bulunamadi!")
            
else: #Belirtilen klasor yoksa
    klasor = os.mkdir(new_path)
    for dosya in os.listdir(path):
        if os.path.exists(path): #Resimler varsa
            if dosya.endswith("unsplash.jpg"): 
                sayac+=1
                print(dosya)
                shutil.move(path+dosya,new_path)
        else:
            print("Tasinacak resimler Bulunamadi!")
                

#Goruntuye Yazi Ekledim
#font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#cv2.putText(img,"Istanbul",(100,200),font,5,(0,0,155),5)

#Goruntuye Daire - Kare Cizdim.
#cv2.circle(img,(75,200),30,(0,0,140),-1)
#cv2.rectangle(img,(635,200),(670,235),(0,0,140),5)

#Goruntuyu dondurdum ve Goruntuyu kuculttum.
#new_img = cv2.transpose(img)

#Pencereyi goruntuledim. Resmin ismini ve goruntulecek resmi verdim. 
#cv2.imshow("Gri Kiz Kulesi",gray_img)
#cv2.imshow("Hsv Kiz Kulesi",hsv_img)
"""cv2.imshow("Resim_Yazi",img)
cv2.imshow("Dondurulen Resim",img)"""

#Herhangi bir tuşa basılana kadar pencereyi goruntulenmesini sagladim.
cv2.waitKey(0)

#Tüm pencerelerin kapatilmasini sagladim.
cv2.destroyAllWindows()






