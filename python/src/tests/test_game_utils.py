import pytest
import flatbuffers
from common.game_utils import new_game, print_game, decode_game, encode_game
from common.mahjong import Game

def test_encode_decode_print():
    builder = flatbuffers.Builder(1024)
    new_game(builder, players=[])
    payload = encode_game(builder)
    print(f'length of payload:  {len(payload)} bytes')  
    print(f'{payload}')  
    dgame = decode_game(payload)
    print_game(dgame)

