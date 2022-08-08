# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:36:24 2022

@author: tosun
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/tosun/spyder_projeler/images/kalem.jpg")

kirp = img[400:800,300:600]

img[100:500,300:600] = kirp #sagdakini solun icerisine gonderdik.

img[:,:,2] = 0 #Kirmizilar artik resimde olmaz.

plt.subplot(121) #1 satir 2 sutundan olusacak - 1.resim
plt.imshow(img) #OpenCv-BGR / Matplotlib-RGB -> yer degistirerek algilar.
plt.subplot(122) #2.resim
plt.imshow(kirp)
plt.show()

#%%
import cv2
import matplotlib.pyplot as plt

#Cerceve Cizme
img = cv2.imread("C:/Users/tosun/spyder_projeler/images/kalem.jpg")

BLUE = [255,0,0] #Mavi olmasina ragmen kirimizi gorunuyor.

replicate = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title("ORIGINAL")
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title("REPLICATE")
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title("REFLECT")
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title("REFLECT101")
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title("WRAP")
plt.subplot(236),plt.imshow(constant,'gray'),plt.title("CONSTANT")

plt.show()



#%%
#Pixellere Ulasma
#px = img[100,100] #ordaki renk degeri
#px_blue = img[100,100,0] #0.kanal(mavi)
"""img[100,100,0] = 255
   px_blue = img[100,100,0] 
   img[100,100] = [255,255,255]
   px = img[100,100] #resim pixel renk degistirme"""
#img.item(100,100,0) #kanal degiskeni de verilerek degeri okunabilir.
#img.itemset((100,100,0),100) #mavinin degeri 100 olsun.
"""b,g,r = cv2.split(img)
   img = cv2.merge((b,g,r))"""
   
#b = img[:,:,0]


#Resim Bilgisi
#img.shape #resmin boyutu-kanali
#img.size  #resmin alani*kanal sayisi
#img.dtype : (uint8)  #pozitif - int - 8 bitlik verilerden olusur.

#ROI - Region Of Image #Resmin belli bir alaninin kirpilmasi/ayrilmasi