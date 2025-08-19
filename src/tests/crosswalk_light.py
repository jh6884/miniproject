# 핵심 기능: 횡단보도 신호를 파악하기
# 목표: 객체 인식을 통해 보행 신호등을 검출하기

from ultralytics import YOLO
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient


model = YOLO("yolo11n.pt")

results = model.train(data="../../data/crosswalk_data/data.yaml", epochs=30, imgsz=416)