import sys
import os 
import time
from enum import Enum

from dotenv import load_dotenv
import paho.mqtt.client as mqtt

import flatbuffers
from mahjong import Suit, Wind, Player, Game
from common.game_utils import new_game, encode_game
from common.PlayerState import PlayerState

whoami = (os.path.splitext(os.path.basename(__file__))[0]).replace("-test","")  

dotenv_path = os.path.join(os.path.dirname(__file__), whoami, '.env')
load_dotenv(dotenv_path)
broker = os.environ.get("broker")
port = int(os.environ.get("port"))

username = os.environ.get(f'{whoami}_username')
password = os.environ.get("password")

player_matching_topic = os.environ.get("player_matching_topic")

print(f"{whoami} Connecting to MQTT Broker: {broker} Port: {port} Username: {username}")
print(f"player_matching_topic: {player_matching_topic} ")

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


def find_a_match_to_start_a_game(client):

    flatbuffer_builder = flatbuffers.Builder(1024)
    result = client.publish(player_matching_topic, "msg")
    status = result[0]
    if status == 0:
        print(f'{whoami} Send `{msg}` to topic `{topic}`')
    else:
        print(f'{whoami} Failed to send message to topic {topic}')


class GameStatusEnum(Enum):
    WAITING, 
    STARTED, 
    ENDED


# table Player {
#   id: ulong;
#   name: string;
#   hidden_tiles: [ubyte];
#   shown_tiles: [ubyte];
#   account_balance: short ;
#   seat: ubyte;
# }

class PlayerGameState():
    def __init__(self, my_player_id : ulong):
        self.my_id  = my_player_id 
        self.status = GameStatusEnum.WAITING
    
    def start_game(self, game: Game):
        self.players = game.Players
        self.me = next(player for player in self.players if player.id == my_id)
        
        self.discarded_tiles = game.DiscardedTiles
        self.hidden_tiles = []
        self.current_wind = game.CurrentWind
        self.current_turn = game.CurrentTurn
        self.current_round = game.CurrentRound

    def draw_tile(self, tile: Tile):
        self.discarded_tiles.append(tile)

    def discarded_tile(self, tile: Tile):
        self.discarded_tiles.append(tile)

game_state = PlayerGameState()

def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        global game_state
        if (msg.topic == player_matching_topic):
            print(f"{whoami} Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        else:
            game=decode_game(msg.payload)
            print(f"{whoami} Received `{game}` from `{msg.topic}` topic")
            print_game(game)
            flatbuffer_msg_count+=1; 

    client.subscribe(topic)
    client.subscribe(flatbuffer_topic)
    client.on_message = on_message


def play_a_tile(client: mqtt_client):
    tile = input("what tile to play?")
    print(f"playing this {tile}")

def run(player_name, player_id):
    global game_state
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

    try:
        find_a_match_to_start_a_game(client)
        while game_state.status == WAITING:
            time.sleep(1)
            print("waiting for game to start")

        while game_state.status == STARTED:
            if (game_state.CurrentTurn == game_state.seat):
                play_a_tile(client)

        print("Good Game! ")
        
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    print(f'{whoami} Exiting gracefully')
    client.disconnect()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <player_name> <player_id>")
        return

    player_name = sys.argv[1]
    player_id = sys.argv[2]

    print(f'Player Name: {player_name}')
    print(f'Player ID: {player_id}')

    run(player_name, player_id)
