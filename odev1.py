# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:47:58 2022

@author: tosun
"""

#
import cv2
import numpy as np

#
sifir = np.zeros((500,500))
bir = np.ones((500,500))

#
cv2.namedWindow("Siyah Resim",cv2.WINDOW_NORMAL)
cv2.namedWindow("Beyaz Resim",cv2.WINDOW_NORMAL)

cv2.imshow("Siyah Resim",sifir)
cv2.imshow("Beyaz Resim",bir)

cv2.waitKey(0)

cv2.destroyAllWindows()