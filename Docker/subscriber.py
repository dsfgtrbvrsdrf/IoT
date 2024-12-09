import json
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point

influx_url = "http://influxdb:8086"
influx_token = "gLpjV3gz8gsAwiC7mnIjoKl6JpbQRrQnWMJsfpIfsr9oWVMCb8nv5w5s1mdW7kZPk3S2u6HWh7irThtjcc0Lug=="
influx_org = "mqtt"
influx_bucket = "temperature"
influx_client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload)
        temperature = float(data['temperature'])
        point = Point("temperature").tag("location", "mqtt").field("value", temperature)

        write_api = influx_client.write_api()
        write_api.write(influx_bucket, influx_org, point)

        print(f"Температура {temperature} записана в InfluxDB.")

    except Exception as e:
        print(f"Ошибка при обработке данных: {e}")

mqtt_broker = "n113916d.ala.eu-central-1.emqxsl.com"
mqtt_port = 8883
mqtt_topic = "esp/temperature"
mqtt_username = "ESP12341231241351345"
mqtt_password = "ESP12341231241351345"
mqtt_cert_path = "emqxsl-ca.txt.crt"

client = mqtt.Client()
client.on_message = on_message
client.tls_set(ca_certs=mqtt_cert_path)
client.tls_insecure_set(True)
client.username_pw_set(mqtt_username, mqtt_password)
client.connect(mqtt_broker, mqtt_port)
client.subscribe(mqtt_topic)
client.loop_forever()

influx_client.close()