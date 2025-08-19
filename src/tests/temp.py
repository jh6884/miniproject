from ultralytics import YOLO
import os, cv2
import matplotlib.pyplot as plt

model = YOLO('runs/detect/train/weights/best.pt')

img_path = '../../data/images/06.jpg'


result = model(img_path, conf=0.1)

result[0].show()