from ultralytics import YOLO
import os, cv2
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient

model = YOLO('runs/detect/train/weights/best.pt')
model2 = YOLO('yolo11s.pt')

img_path = '../../data/images/'
img_name = '06.jpg'
lst = os.listdir(img_path)
img = cv2.imread(img_path+img_name)
result = model(img_path+img_name, conf=0.1)
result2 = model2(img_path+img_name, conf=0.3)

result[0].show()
result2[0].show()

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="Ct4LGBM8nYfY0kBogGnU"
)

result3 = CLIENT.infer(img_path+img_name, model_id="traffic-light-vzfpm/3")

print(result3)

pred = result3['predictions']

for i in range(len(pred)):
    if pred[i]['class'].lower() == 'red':
        color = (0, 0, 255)
    elif pred[i]['class'].lower() == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)
    xtl = int(pred[i]['x']-(pred[0]['width']/2))
    ytl = int(pred[i]['y']-(pred[0]['height']/2))
    xbr = int(pred[i]['x']+(pred[0]['width']/2))
    ybr = int(pred[i]['y']+(pred[0]['height']/2))
    print(xtl, ytl, xbr, ybr)
    cv2.rectangle(img, (xtl, ytl), (xbr, ybr), color, thickness=1, lineType=cv2.LINE_AA)
    cv2.putText(img, pred[i]['class'], (xtl, ytl-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()