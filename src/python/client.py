# python 3.8

import time

import os 
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

dotenv_path = os.path.join(os.path.dirname(__file__), 'client', '.env')
load_dotenv(dotenv_path)
broker = os.environ.get("broker")
port = int(os.environ.get("port"))
topic = os.environ.get("topic")
username = os.environ.get("client_username")
password = os.environ.get("password")

print(f"Connecting to MQTT Broker: {broker}\nPort: {port}\nTopic: {topic}\nUsername: {username}")

def connect_mqtt():
    def on_connect(client, userdata, flags, rc, list_of_stuff):
        if rc == 0:
            print("Connected to MQTT Broker!", client, userdata, flags, rc, list_of_stuff)
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_log(client, userdata, paho_log_level, messages):
        print(message)

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
    client.username_pw_set(username, password)
    client.tls_set(ca_certs='./common/server-ca.crt')
    client.on_connect = on_connect
    client.on_log = on_log
    client.connect(broker, port, 60)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
