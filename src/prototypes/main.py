from ultralytics import YOLO
import os, cv2
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient

#configs
'''
load video, model
setting var
'''
class Config:
    # file path config
    video_path = '../../data/images/video_sample.gif'

    # video config
    frame_width = 640
    frame_height = 480


#functions
'''
def
'''
def setting_models():
    # Call roboflow API for crosswalk, pedestrian light detection
    CLIENT = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key="Ct4LGBM8nYfY0kBogGnU"
    )

    # Call YOLO model for person, car detection
    model = YOLO('yolo11n.pt')
    return CLIENT, model

def draw_bounding_boxes(frame, CLIENT, model):
    if frame is None:
        print("There is no input Video.")

    detect_object = model.predict(source=frame)
    detect_crosswalk = CLIENT.infer(frame, model_id="traffic-light-vzfpm/3")
    
    for boxes in detect_object:
        boxes.boxes.xywh
        boxes.boxes.conf
    pred = detect_crosswalk['predictions']
    print(pred)
    return

def setting_videos(video_path, frame_width, frame_height):
    try:
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
        if not cap:
            raise RuntimeError
        return cap
    except Exception as e:
        print(f"failed to load video: {e}")
        return None
    
#codes
if __name__ == '__main__':
    config = Config()
    CLIENT, model = setting_models()
    cap = setting_videos(config.video_path, config.frame_width, config.frame_height)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        draw_bounding_boxes(frame, CLIENT, model)

'''
if __name__ == '__main__':
    call_images
        if no image:
            break
    
    call yolo model for detection
        detect crosswalk, car, pedestrian
        if traffic light == green:
            if pedestrian is True:
                check distance between car and crosswalk:
                    illegal
            else:
                legal

'''