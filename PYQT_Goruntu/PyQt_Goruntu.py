# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt_Goruntu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_gercek = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gercek.setGeometry(QtCore.QRect(130, 290, 151, 28))
        self.btn_gercek.setObjectName("btn_gercek")
        self.btn_gray = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gray.setGeometry(QtCore.QRect(297, 290, 181, 28))
        self.btn_gray.setObjectName("btn_gray")
        self.btn_negatif = QtWidgets.QPushButton(self.centralwidget)
        self.btn_negatif.setGeometry(QtCore.QRect(490, 290, 171, 28))
        self.btn_negatif.setObjectName("btn_negatif")
        self.gorsel_buton = QtWidgets.QPushButton(self.centralwidget)
        self.gorsel_buton.setGeometry(QtCore.QRect(280, 80, 200, 200))
        self.gorsel_buton.setText("")
        self.gorsel_buton.setObjectName("gorsel_buton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_gercek.setText(_translate("MainWindow", "Gercek Goruntu"))
        self.btn_gray.setText(_translate("MainWindow", "Gri Goruntu"))
        self.btn_negatif.setText(_translate("MainWindow", "Negatif Goruntu"))

