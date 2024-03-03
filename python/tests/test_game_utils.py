import pytest
import flatbuffers
from src.common.game_utils import new_game, print_game, decode_game, encode_game

def test_encode_decode_print():
    builder = flatbuffers.Builder(1024)
    my_new_game = new_game(builder)
    payload = encode_game(builder)
    print(f'length of payload:  {len(payload)} bytes')  
    print(f'{payload}')  
    dgame = decode_game(payload)
    print_game(dgame)


