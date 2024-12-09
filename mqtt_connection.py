#mqtt_connection.py
import paho.mqtt.client as mqtt
import json

class MqttClient:
    def __init__(self, broker, port, topics, username, password, cert_path=None):
        self.broker = broker
        self.port = port
        self.topics = topics
        self.username = username
        self.password = password
        self.cert_path = cert_path
        self.client = mqtt.Client()
        self.client.username_pw_set(self.username, self.password)

        if self.cert_path:
            self.client.tls_set(ca_certs=self.cert_path)
            self.client.tls_insecure_set(True)

        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to broker with code {rc}")
        for topic in self.topics:
            client.subscribe(topic)
            print(f"Subscribed to topic: {topic}")


    def connect(self):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    def publish(self, message, topic):
        self.client.publish(topic, json.dumps(message))
        print(f"Message {message} has been sent to {topic}")

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("MQTT disconnect")