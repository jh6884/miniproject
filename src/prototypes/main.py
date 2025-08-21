from ultralytics import YOLO
import os, cv2

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
    target_class = [0, 5]
    detect_crosswalk = model(frame, classes=target_class)
    
    for r in detect_crosswalk:
        for box in r.boxes:
            class_id = int(box.cls[0])

            if class_id in target_class:
                coords = box.xyxy[0].tolist()
                print(f'클래스 ID: {class_id}, BBox: {coords}')
                print(f'클래스 이름: {model.names[class_id]}')
    

#codes
if __name__ == '__main__':
    config = Config()
    
    cap = setting_videos(config.video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = set_video_size(frame)
        calc_distance(frame, config.model)
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