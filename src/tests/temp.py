from ultralytics import YOLO
import os, cv2
import matplotlib.pyplot as plt

model = YOLO('runs/detect/train/weights/best.pt')
model2 = YOLO('yolo11n.pt')

img_path = '../../data/images/'
lst = os.listdir(img_path)

result = model(img_path+'09.jpg', conf=0.1)
result2 = model2(img_path+'09.jpg', conf=0.1)
# for file in lst:
#     results = model(img_path+file, conf=0.1)


result[0].show()
result2[0].show()