# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:08:12 2022

@author: tosun
"""

import sys #uygulamalar komut satirindan calisacagi icin
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt_Goruntu import Ui_MainWindow

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()   

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        
        #self.btn_save = QtWidgets.QPushButton(self)
        self.ui.btn_gercek.clicked.connect(self.gercek)
        self.ui.btn_gray.clicked.connect(self.gray)
        self.ui.btn_negatif.clicked.connect(self.negatif)
    
    def gercek(self):
        image = cv2.imread("C:/Users/tosun/spyder_projeler/images/kisi.jpg")
        img = cv2.resize(image,(200,200))
        cv2.imwrite("images/kisi_gercek.jpg",img)
        self.ui.gorsel_buton.setStyleSheet("border-image:url(C:/Users/tosun/spyder_projeler/images/kisi_gercek.jpg)")
        #gercek = cv2.imshow("Gercek Goruntu",img)
        #self.ui.lbl_gercek.setPixmap(QtGui.QPixmap(img))
        
    def gray(self):
        image = cv2.imread("C:/Users/tosun/spyder_projeler/images/kisi.jpg")
        img = cv2.resize(image,(200,200))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite("images/kisi_gray.jpg",gray)
        self.ui.gorsel_buton.setStyleSheet("border-image:url(C:/Users/tosun/spyder_projeler/images/kisi_gray.jpg)")
        #cv2.imshow("Gri Goruntu",gray)
        #self.ui.lbl_gray.setPixmap(QtGui.QPixmap(gray_img))
    
    def negatif(self):
        image = cv2.imread("C:/Users/tosun/spyder_projeler/images/kisi.jpg")
        rows = image.shape[0]
        cols = image.shape[1]
        rows,cols = 200,200
        img = cv2.resize(image,(cols,rows))
        for i in range(rows):
            for j in range(cols):
                img[j,i,:]=1-img[j,i,:]
        cv2.imwrite("images/kisi_negatif.jpg",img)
        self.ui.gorsel_buton.setStyleSheet("border-image:url(C:/Users/tosun/spyder_projeler/images/kisi_negatif.jpg)")
        #cv2.imshow("Negatif Goruntu",img)
        #self.ui.lbl_negatif.setPixmap(QtGui.QPixmap(img))
        
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

app()
