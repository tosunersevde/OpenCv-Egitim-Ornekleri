# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:37:58 2022

@author: tosun
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 09:47:36 2022

@author: tosun
"""

#Kutuphaneleri tanimladim.
#import cv2
#import numpy as np

#Sifir ve birlerden olusan matrisler olusturdum.
#sifir = np.zeros((500,500))
#bir = np.ones((500,500))

#Resim gosterecek pencere olusturdum.Pencereye isim verdim. 
#Pencere boyutunu manuel olarak değiştirebilecegim sekilde ayarladim.
#cv2.namedWindow("Siyah Resim",cv2.WINDOW_NORMAL)
#cv2.namedWindow("Beyaz Resim",cv2.WINDOW_NORMAL)

#Pencereyi goruntuledim. Resmin ismini ve goruntulecek resmi verdim. 
#cv2.imshow("Siyah Resim",sifir)
#cv2.imshow("Beyaz Resim",bir)

#Herhangi bir tuşa basılana kadar pencereyi goruntulenmesini sagladim.
#cv2.waitKey(0)

#Tüm pencerelerin kapatilmasini sagladim.
#cv2.destroyAllWindows()

#%%
#Kutuphaneleri tanimladim.
"""import cv2
import numpy as np
import os
import shutil"""

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

#%%
#5 Goruntu Okudum. Ismini Degistirdim.
"""sayac = 0
for dosya in os.listdir("C:/Users/tosun/Downloads/"):
    if dosya.endswith("unsplash.jpg"):
        sayac+=1
        print(dosya)
        resim = cv2.imread("C:/Users/tosun/Downloads/" +dosya)
        cv2.imwrite("resim" +str(sayac)+".jpg",resim)"""
        
#Dosyalari bilgisayardan okudum. Yeniden adlandirdim.
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
    
#Enumerate ile yaptim.
"""path = "C:/Users/tosun/Downloads/" #resimlerin bulundugu dosya yolu
for dosya in enumerate(os.listdir(path)):
    if dosya[1].endswith("unsplash.jpg"):
        print(dosya[1]) #Dosya isimlerini aldim.
        #print(dosya[0])
        resim = cv2.imread(path+dosya[1])
        # cv2.imwrite("resim" +str(dosya[0])+".jpg",resim)
        cv2.namedWindow("ornek",cv2.WINDOW_NORMAL)
        cv2.imshow("ornek",resim)
        cv2.waitKey(100)
cv2.destroyAllWindows()"""
"""count = 0
for resim in os.listdir("C:/Users/tosun/spyder_projeler"):
    count+=1
    os.rename("resim"+str(count)+".jpg","Resim" +str(count)+".jpg")"""

#%%
#Kutuphaneleri tanimladim.
import cv2
import numpy as np
import os
import shutil

#Goruntu Okudum.
img = cv2.imread("kiz_kulesi.png")

#Orta pixel degerini okudum.
"""cols = img.shape[0] // 2
rows = img.shape[1] // 2
orta_deger = img[cols][rows]"""
#ortadeger2 = gray_img[cols][rows]

#Goruntuyu tasidim.    
"""sayac = 0
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
            print("Tasinacak resimler Bulunamadi!")"""
                
#%%
import cv2

img = cv2.imread("kiz_kulesi.png")

#Goruntuye Yazi Ekledim
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
konum = (100,200)
renk = (255,255,255)
boyut = 5
kalinlik = 5
yazi = "Istanbul"
ekran_satir = img.shape[0] // 50
ekran_sutun = img.shape[1] // 200

#Goruntudeki yazinin kaymasini ve alt satira gecmesini sagladim.
sayac = 0 #Yazinin satirdaki konumu
count = 100 #Yazinin sutundaki konumu
for i in range(ekran_sutun):
    for j in range(ekran_satir):
        sayac += 50
        konum = (sayac,count)
        img = cv2.imread("kiz_kulesi.png")
        cv2.putText(img,yazi,konum,font,boyut,renk,kalinlik)
        cv2.imshow("Kayan_yazi",img)
        cv2.waitKey(100)
    count += 100
    sayac = 0
    konum = (sayac,count)
    img = cv2.imread("kiz_kulesi.png")
    cv2.putText(img,yazi,konum,font,boyut,renk,kalinlik)
    cv2.imshow("Kayan_yazi",img)
    cv2.waitKey(100)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
#Goruntuye Daire - Kare Cizdim.
"""cv2.circle(img,(75,200),30,(0,0,140),-1)
cv2.rectangle(img,(635,200),(670,235),(0,0,140),5)"""

#new_img = cv2.transpose(img)

#Pencereyi goruntuledim. Resmin ismini ve goruntulecek resmi verdim. 
#cv2.imshow("Resim_Yazi",img)

#Herhangi bir tuşa basılana kadar pencereyi goruntulenmesini sagladim.
#cv2.waitKey(0)

#Tüm pencerelerin kapatilmasini sagladim.
#cv2.destroyAllWindows()


#%%
#Kutuphaneleri tanimladim.
import cv2
import matplotlib as plt

#Goruntuyu Okudum.
kisi = cv2.imread("C:/Users/tosun/Downloads/kisi.jpg")
#resim1 = cv2.imread("C:/Users/tosun/Downloads/fil.jpg")

#Dondurme
"""cols = resim1.shape[0]
rows = resim1.shape[1]
aci = 180
resim_oran = 0.3 #%70 oran kuculme

rotasyon_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),aci,0.3)
dondurulen = cv2.warpAffine(resim1,rotasyon_matrix,(rows,cols))"""

#Goruntuyu resize ettim.
#kucuk_resim = cv2.resize(kisi,(227,227))

#%%
#Bulaniklastirma
ksize=(5,5) #Bulaniklasan cekirdek boyutu
mean_blur =  cv2.blur(kisi,ksize)
gaussian_blur = cv2.GaussianBlur(kisi,ksize,0)
median_blur = cv2.medianBlur(kisi,5)

#Cerceve cizdim.
"""boyut = 15
renk = (0,255,0)
sol_ust = (1250,1000)
sag_alt = (2400,2700)

cv2.rectangle(kisi,sol_ust,sag_alt,renk,boyut)"""

#Goruntu buyuklugu degistirilebilecek sekilde ayarladim.
"""cv2.namedWindow("Kucuk Resim",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Dondurulen",cv2.WINDOW_NORMAL)"""

#%%
cv2.namedWindow("Kisi",cv2.WINDOW_NORMAL)
cv2.namedWindow("Mean_Blur",cv2.WINDOW_NORMAL)
cv2.namedWindow("Gaussian_Blur",cv2.WINDOW_NORMAL)
cv2.namedWindow("Median_Blur",cv2.WINDOW_NORMAL)

#Goruntuyu Gosterdim.
cv2.imshow("Kisi",kisi)
"""cv2.imshow("Dondurulen",dondurulen)
cv2.imshow("Kucuk Resim",kucuk_resim)"""
"""cv2.imshow("Mean_Blur",mean_blur)
cv2.imshow("Gaussian_Blur",gaussian_blur)
cv2.imshow("Median_Blur",median_blur)"""

#Tusa Basildiginda kapansin.
cv2.waitKey(0)

#Pencereleri Kapattim.







