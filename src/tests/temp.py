from ultralytics import YOLO
import os, cv2
import matplotlib.pyplot as plt

model = YOLO('runs/detect/train/weights/best.pt')
class_name = {
    0 : 'crosswalk',
    1 : 'red',
    2 : 'green'
}

img_path = '../../data/images/02.jpg'


result = model(img_path, classes=list(class_name.keys()), conf=0.1)

result[0].show()