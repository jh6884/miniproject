# 핵심 기능: 횡단보도 신호를 파악하기
# 목표: 객체 인식을 통해 보행 신호등을 검출하기

from inference import get_model
import supervision as sv
import cv2

img_path = "../../data/test03.jpg"
image = cv2.imread(img_path)

model = get_model(model_id='traffic-light-detection-h8cvg/2')

results = model.infer(image)

# load the results into the supervision Detections api
detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

# create supervision annotators
bounding_box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# annotate the image with our inference results
annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections)

# display the image
sv.plot_image(annotated_image)