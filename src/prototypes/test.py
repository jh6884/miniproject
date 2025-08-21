from ultralytics import YOLO
import os, cv2
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient

video_path = '../../data/images/video_sample2.mp4'

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="Ct4LGBM8nYfY0kBogGnU"
)
model = YOLO('yolo11n.pt')

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# 3. 프레임 단위로 객체 탐지
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    new_width = int(frame.shape[1] / 4)
    new_height = int(frame.shape[0] / 4)
    frame = cv2.resize(frame, (new_width, new_height))
    # 현재 프레임에 대해 객체 탐지 실행
    # 'stream=True'를 사용하면 메모리 효율성이 높아집니다.
    results = model(frame, stream=True)
    

    # 탐지 결과 시각화
    # results는 반복 가능한 객체이며, 각 요소는 하나의 이미지에 대한 결과입니다.
    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("YOLOv8 Object Detection", annotated_frame)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. 종료 및 자원 해제
cap.release()
cv2.destroyAllWindows()