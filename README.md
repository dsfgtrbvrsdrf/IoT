# IoT Remote Monitoring and Data Processing System

This project is an IoT-based application that integrates ESP8266, speech-to-text, and video-to-text processing capabilities.
The system allows remote retrieval of temperature data from an ESP8266 device over an encrypted MQTT connection.
Additionally, the system can receive processed data from ESP8266 about recognized speech and objects detected via a camera.
All components are designed to work within a Dockerized environment.

## Table of Contents
- Project Overview
- Features
- Installation
- Usage
- Authors

## Project Overview
This project demonstrates how IoT devices, combined with modern machine learning models, can enable seamless remote data processing. Key highlights include:
- Encrypted MQTT communication with ESP8266.
- Real-time video object detection using YOLOv5.
- Speech-to-text processing in Polish language using Whisper.
- Easy deployment using Docker containers.

## Features
- **Temperature Monitoring**: ESP8266 publishes temperature data securely.
- **Speech-to-Text**: Recognizes and processes spoken words in Polish, sending the result to ESP8266.
- **Video-to-Text**: Detects objects in a camera feed using YOLOv5 and sends results to ESP8266.
- **Encrypted Communication**: Ensures secure data transfer using TLS.

## Installation
Follow these steps to set up the system:

Set Up Docker:
docker-compose up --build

Install Python 3.10 Dependencies:
pip install -r requirements.txt

## Usage

![Table for Usage](./images/table.svg)


Start the Application
python main.py

Configure ESP8266:
Set up your ESP8266 device to publish temperature data to the specified MQTT broker.

Interact with GUI:
Use the "video-to-text" button to start object detection.
Use the "speech-to-text" button to start speech recognition.
View Logs: The detected objects and recognized text will be logged and sent back to the ESP8266 device.

## Authors
Maksim Tsikhanau 28187

Dmytro Kobzar 28264


