import sounddevice as sd
import numpy as np
import whisper
import re

class SpeechRecognizer:
    def __init__(self, mqtt_client, model_name="base", language="pl", sample_rate=16000):
        self.sample_rate = sample_rate
        self.mqtt_client = mqtt_client
        self.language = language
        self.model = whisper.load_model(model_name)

    def record_audio(self, duration):
        print("Recording...")
        audio = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait()
        print("Recorded!")
        return audio.flatten()

    def replace_polish_chars(self, text):
        polish_to_english = {
            'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
            'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N', 'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
        }
        pattern = re.compile('|'.join(re.escape(key) for key in polish_to_english.keys()))
        return pattern.sub(lambda match: polish_to_english[match.group(0)], text)
    def recognize_speech(self, audio_data):
        audio_data_float = audio_data.astype(np.float32) / 32768.0
        result = self.model.transcribe(audio_data_float, language=self.language)
        return result['text']

    def process(self, duration):
        audio_data = self.record_audio(duration)
        recognized_text = self.recognize_speech(audio_data)
        return recognized_text
    def run(self, duration=5):
        text = self.process(duration)
        self.mqtt_client.publish(self.replace_polish_chars(text), "esp/speech_to_text")