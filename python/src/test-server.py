import os 
import numpy
import time
import colorama

from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client

import flatbuffers
from common.mahjong import Suit, Wind, Player, Game
from common.game_utils import print_game, decode_game

whoami = (os.path.splitext(os.path.basename(__file__))[0]).replace("test-","")  

dotenv_path = os.path.join(os.path.dirname(__file__), whoami, '.env')
load_dotenv(dotenv_path)
broker = os.environ.get("broker")
port = int(os.environ.get("port"))
topic = os.environ.get("topic")
flatbuffer_topic = os.environ.get("flatbuffer_topic")
username = os.environ.get(f'{whoami}_username')
password = os.environ.get("password")

print(f"{whoami} Connecting to MQTT Broker: {broker}\nPort: {port}\nTopic: {topic} & flatbuffer_topic: {flatbuffer_topic}\nUsername: {username}")

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc, list_of_stuff):
        if rc == 0:
            print(f'{whoami} Connected to MQTT Broker!')
        else:
            print(f'{whoami} Failed to connect, return code %d\n', rc)

    def on_log(client, userdata, paho_log_level, messages):
        print(message)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, protocol=mqtt_client.MQTTv5)

    client.tls_set(ca_certs='./common/server-ca.crt')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_log = on_log
    client.connect(broker, port, 60)

    return client


msg_count = 0
flatbuffer_msg_count = 0 
expected_msg_count = 3 

def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        global msg_count
        global flatbuffer_msg_count

        if (msg.topic == topic):
            print(f"{whoami} Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            msg_count+=1; 
        else:
            game=decode_game(msg.payload)
            print(f"{whoami} Received `{game}` from `{msg.topic}` topic")
            print_game(game)
            flatbuffer_msg_count+=1; 

    client.subscribe(topic)
    client.subscribe(flatbuffer_topic)
    client.on_message = on_message


def run():
    global msg_count
    global flatbuffer_msg_count

    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

    try:
        timeout = time.time() + 30   # 30 seconds from now
        while True:
            time.sleep(1)
            if msg_count >= expected_msg_count and flatbuffer_msg_count >= expected_msg_count or time.time() > timeout:
                break
    except KeyboardInterrupt:
        print(f'{whoami} KeyboardInterrupt')

    print(f'{whoami} Exiting gracefully')
    client.disconnect()


if __name__ == '__main__':
    run()
    if (msg_count != 3 or flatbuffer_msg_count !=3):
        assert msg_counter == expected_msg_count, "Not enough messages!"
        assert flatbuffer_msg_count == expected_msg_count, "Not enough binary messages!"
        exit -1 
