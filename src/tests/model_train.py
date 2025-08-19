from ultralytics import YOLO
import yaml


model = YOLO('yolo11n.pt')

result = model.train(data='data.yaml', epochs=30, imgsz=640)