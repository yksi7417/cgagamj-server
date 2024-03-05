import random
from common.SuitEnum import SuitEnum 

def get_randomized_full_set():
    unique_tiles=[]
    unique_tiles.extend(list(range(0,144)))
    random.shuffle(unique_tiles)
    return unique_tiles

def get_suit(tile_number : int):
    if (tile_number >= 0 and tile_number < 36):
        return SuitEnum.BAMBOO
    elif (tile_number < 72):
        return SuitEnum.CHARACTER
    elif (tile_number < 108):
        return SuitEnum.DOT
    elif (tile_number < 124):
        return SuitEnum.WINDS
    elif (tile_number < 136):
        return SuitEnum.DRAGONS
    elif (tile_number < 140):
        return SuitEnum.FLOWERS
    elif (tile_number < 144):
        return SuitEnum.SEASONS


def get_card_number(tile_number : int):
    if (tile_number >= 140):
        return tile_number - 140 
    elif (tile_number >= 136):
        return tile_number - 136 
    elif (tile_number >= 124):
        return (tile_number - 124) % 3 
    elif (tile_number >= 108):
        return (tile_number - 108) % 4 
    elif (tile_number >= 72):
        return (tile_number - 72) % 9 
    elif (tile_number >= 36):
        return (tile_number - 36) % 9
    else:
        return tile_number % 9


