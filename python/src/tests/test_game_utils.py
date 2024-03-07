import pytest
import flatbuffers

from mahjong import Game
from common.game_utils import new_game, print_game, decode_game, encode_game
from common.PlayerState import PlayerState

# Sample data for 4 players
temp_players = [
    PlayerState(1, "Alice", [1, 2, 3], [], 1000, 0),
    PlayerState(2, "Bob", [6, 7, 8], [9, 10], 2000, 1),
    PlayerState(3, "Charlie", [11, 12, 13], [14, 15], 3000, 2),
    PlayerState(4, "Dave", [], [19, 20], 4000, 3),
]

def test_encode_decode_print():
    builder = flatbuffers.Builder(1024)
    my_game = new_game(builder, players=temp_players)
    payload = encode_game(builder)
    print(f'length of payload:  {len(payload)} bytes')  
    print(f'{payload}')  
    dgame = decode_game(payload)
    print_game(dgame)

