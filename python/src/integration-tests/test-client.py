import time
import colorama

import os 
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

import flatbuffers
from mahjong import Suit, Wind, Player, Game
from common.game_utils import new_game, encode_game
from common.PlayerState import PlayerState

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

msg_count = 0

# Sample data for 4 players
temp_players = [
    PlayerState(1, "Alice", [1, 2, 3], [], 1000, 0),
    PlayerState(2, "Bob", [6, 7, 8], [9, 10], 2000, 1),
    PlayerState(3, "Charlie", [11, 12, 13], [14, 15], 3000, 2),
    PlayerState(4, "Dave", [], [19, 20], 4000, 3),
]

def connect_mqtt():
    def on_connect(client, userdata, flags, rc, list_of_stuff):
        if rc == 0:
            print(f'{whoami} Connected to MQTT Broker!', client, userdata, flags, rc, list_of_stuff)
        else:
            print(f'{whoami} Failed to connect, return code %d\n', rc)

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
    global msg_count

    for i in range(0,3):
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f'{whoami} Send `{msg}` to topic `{topic}`')
        else:
            print(f'{whoami} Failed to send message to topic {topic}')
        msg_count += 1

        game_builder = flatbuffers.Builder(1024)
        game = new_game(game_builder, players=temp_players)

        result = client.publish(flatbuffer_topic, encode_game(game_builder))
        status = result[0]
        if status == 0:
            print(f'{whoami} Send `{result}` to topic `{topic}`')
        else:
            print(f'{whoami} Failed to send message to topic {topic}')

        msg_count += 1
    

def run():
    client = connect_mqtt()
    client.loop_start()
    try:
        publish(client)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    print(f'{whoami} Exiting gracefully')
    client.disconnect()


if __name__ == '__main__':
    run()
    if (msg_count != 6):
        assert msg_count == 6 , "Didn't publish enough messages! "
        exit -1 
