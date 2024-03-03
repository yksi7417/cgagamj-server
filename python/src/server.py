import os 
import numpy

from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client

import flatbuffers
from common.mahjong import Suit, Wind, Player, Game
from common.game_utils import print_game, decode_game

whoami = os.path.splitext(os.path.basename(__file__))[0]  # remove the extension
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        if (msg.topic == topic):
            print(f"{whoami} Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        else:
            game=decode_game(msg.payload)
            print(f"{whoami} Received `{game}` from `{msg.topic}` topic")
            print_game(game)

    client.subscribe(topic)
    client.subscribe(flatbuffer_topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print(f'{whoami} Exiting gracefully')
        client.disconnect()

if __name__ == '__main__':
    run()
