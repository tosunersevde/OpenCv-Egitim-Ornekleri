# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:26:10 2022

@author: tosun
"""

import cv2
import numpy as np
import os
 
# Model ve cfg dosya yollarını
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
 
# Nesne isimlerini 'coco.names' dosyasından çekme
classes = []
with open("coco.names.txt", "r") as file:
    for line in file.readlines():
        classes.append(line.strip())
 
# Resim yolu
images_path = "C:/Users/tosun/spyder_projeler/images/"
 
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(255, 0, size=(len(classes), 3))
 
for dosya in os.listdir(images_path):
    if dosya.endswith("unsplash.jpg"):
        print(dosya)
        img = cv2.imread(images_path+dosya)
        img = cv2.resize(img,(600,600))
        height, width, channels = img.shape
     
        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
     
        net.setInput(blob)
        outs = net.forward(output_layers)
     
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                 
                # Doğruluk oranı
                if confidence > 0.3:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
     
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
     
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
     
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
     
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
     
                dogruluk = (f"%{round(confidences[i],2)}")
                label = (f"{classes[class_ids[i]]} {dogruluk}")
     
                color = [int(c) for c in colors[class_ids[i]]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
     
                # Text arka planı için text boyutunu alıyoruz
                (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                textBg = cv2.rectangle(img, (x, y - 15), (x + w, y), color, -1)
                cv2.putText(textBg, label, (x, y-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
     
        cv2.imshow("Image", img)
        key = cv2.waitKey(0)
 
cv2.destroyAllWindows()