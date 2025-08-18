# 핵심 기능: 횡단보도 신호를 파악하기
# 목표: 객체 인식을 통해 보행 신호등을 검출하기

from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt


model = YOLO("yolo11n.pt")

img = '../../data/test09.jpg'

# results = model(img)

train_model = model.train(data="../../data/dataset/data.yaml", epochs = 5, imgsz = 640)