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
    video_path = '../../data/images/video_sample2.mp4'

    # video config
    frame_width = 640
    frame_height = 480

    # class config
    classes = {0: 'person',
               1: 'bicycle',
               2: 'car',
               3: 'motorcycle',
               5: 'bus',
               7: 'truck'
               }

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

def model_settings(frame, CLIENT, model, classes):
    if frame is None:
        print("There is no input Video.")

    detect_object = model(frame, classes=1, conf=0.3, verbose=False)
    detect_crosswalk = CLIENT.infer(frame, model_id="traffic-light-vzfpm/3")
    
    print(detect_object)
    pred = detect_crosswalk['predictions']
    print(pred)
    return

def setting_videos(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
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
        
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

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