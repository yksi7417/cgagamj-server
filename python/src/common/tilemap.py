import random
from common.SuitEnum import SuitEnum 

def get_randomized_full_set():
    unique_tiles=[]
    unique_tiles.extend(list(range(0,144)))
    random.shuffle(unique_tiles)
    return unique_tiles


def get_suit(tile_number : int):
    if (0 < tile_number and tile_number < 36):
        return SuitEnum.BAMBOO