# python 3.8

import random
import time

import paho.mqtt.client as mqtt

broker = 'ieea4188.ala.us-east-1.emqxsl.com'
port = 8883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'client'
password = 'cgaga11840Power'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc, list_of_stuff):
        if rc == 0:
            print("Connected to MQTT Broker!", client, userdata, flags, rc, list_of_stuff)
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_log(client, userdata, paho_log_level, messages):
        print(message)


    # client = mqtt_client.Client(client_id)
    # client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)

    # client.tls_set(ca_certs='./server-ca.crt')
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
