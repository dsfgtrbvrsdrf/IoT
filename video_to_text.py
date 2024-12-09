import cv2
import torch
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


class YOLOv5CameraDetector:
    def __init__(self, mqtt_client, camera_index=0, model_name='yolov5s'):
        self.mqtt_client = mqtt_client
        self.camera_index = camera_index
        self.model_name = model_name
        self.model = torch.hub.load('ultralytics/yolov5', self.model_name)
        self.cap = None

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Capture error")
        results = self.model(frame)
        detected_objects = results.pandas().xyxy[0]
        labels = detected_objects['name'].tolist()
        frame_with_boxes = results.render()[0]
        return frame_with_boxes, labels

    def run(self):
        print("Launching detection")
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise ValueError("No camera source")
        while True:
            try:
                frame_with_boxes, labels = self.process_frame()
                if labels:
                    self.mqtt_client.publish(labels[0], "esp/video_to_text")
                    print(f"Detected: {', '.join(labels)}")
                cv2.imshow('YOLO Object Detection', frame_with_boxes)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except RuntimeError as e:
                print(e)
                break
        self.cleanup()

    def cleanup(self):
        self.cap.release()
        cv2.destroyAllWindows()