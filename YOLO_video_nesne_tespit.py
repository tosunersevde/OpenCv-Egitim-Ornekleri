# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:30:39 2022

@author: tosun
"""

import cv2
import numpy as np

# Model ve cfg dosya yolları
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
 
# Nesne isimlerini dosyadan çekme
classes = []
with open("YOLO_isimler.txt", "r") as file:
    for line in file.readlines():
        classes.append(line.strip())
 
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(255, 0, size=(len(classes), 3))

cam = cv2.VideoCapture("video.mp4")
#cam = cv2.VideoCapture("video2.mp4")

while cam.isOpened():
    
    ret , frame = cam.read()
    
    height, width, channels = frame.shape
    
    # Tespit edilen objeler
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
 
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
 
                # Dikdortgen koordinatlari
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
 
            # Text arka planı için text boyutunu alıyoruz
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            textBg = cv2.rectangle(frame, (x, y - 15), (x + w, y), color, -1)
            cv2.putText(textBg, label, (x, y-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
 
    cv2.imshow("Video",frame)

    if cv2.waitKey(1) &0xFF == ord("q"): 
        break

cam.release()
cv2.destroyAllWindows()
