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
    video_path = '../../data/images/video_sample5.mp4'

    # model config
    model = YOLO('yolo11n.pt')

#functions
'''
def
'''

def draw_boundingbox(frame, model):
    if frame is None:
        print("There is no input Video.")

    detect_object = model(frame, conf=0.1, verbose=False)

    annotated_frame = detect_object[0].plot()

    return annotated_frame

def setting_videos(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise RuntimeError
        return cap
    except Exception as e:
        print(f"failed to load video: {e}")
        return None

def set_video_size(frame):
    ratio = round(frame.shape[0] / frame.shape[1], 2)
    frame = cv2.resize(frame, (640, int(640*ratio)))
    return frame

def calc_distance(frame, model):
    detect_crosswalk = model(frame, classes=0)
    detect_cars = model(frame, classes=5)
    crosswalk_box = []
    cars_box = []
    for coordinate in detect_crosswalk:
        for box in coordinate.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            crosswalk_box.append([x1, y1, x2, y2])
    for coordinate in detect_cars:
        for box in coordinate.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            cars_box.append([x1, y1, x2, y2])
    print(crosswalk_box)
    print()
    print(cars_box)
    print()
    

#codes
if __name__ == '__main__':
    config = Config()
    
    cap = setting_videos(config.video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = set_video_size(frame)
        result_frame = draw_boundingbox(frame, config.model)
        cv2.imshow('video', result_frame)
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