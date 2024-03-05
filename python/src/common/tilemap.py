import random

def get_randomized_full_set():
    unique_tiles=[]
    unique_tiles.extend(list(range(144)))
    random.shuffle(unique_tiles)
    return unique_tiles

