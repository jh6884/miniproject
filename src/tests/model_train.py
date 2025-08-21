from ultralytics import YOLO
import yaml


model = YOLO('yolo11n.pt')

result = model.train(data='C:/Users/405/projects/miniproject/data/dataset/data.yaml', epochs=10, imgsz=640)