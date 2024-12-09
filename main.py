from mqtt_connection import MqttClient
from video_to_text import YOLOv5CameraDetector
from speech_to_text import SpeechRecognizer
import tkinter as tk

mqtt_broker = "n113916d.ala.eu-central-1.emqxsl.com"
mqtt_port = 8883
mqtt_topics = ["esp/temperature", "esp/speech_to_text", "esp/video_to_text"]
mqtt_username = "ESP12341231241351345"
mqtt_password = "ESP12341231241351345"
mqtt_cert_path = "emqxsl-ca.txt.crt"


mqtt_client = MqttClient(broker=mqtt_broker, port=mqtt_port, topics=mqtt_topics,
                         username=mqtt_username, password=mqtt_password, cert_path=mqtt_cert_path)

mqtt_client.connect()

detector = YOLOv5CameraDetector(camera_index=1, model_name='yolov5s', mqtt_client=mqtt_client)
audio_processor = SpeechRecognizer(mqtt_client=mqtt_client)

root = tk.Tk()
root.title("Application")
root.geometry("400x300")

video_start_button = tk.Button(root, text="video-to-text", command=detector.run)
video_start_button.pack(pady=10)

audio_start_button = tk.Button(root, text="speech-to-text", command=audio_processor.run)
audio_start_button.pack(pady=10)

root.mainloop()