import random

def get_randomized_full_set():
    unique_tiles=[]
    for i in range(4):
        unique_tiles.extend(list(range(36)))
    random.shuffle(unique_tiles)
    return unique_tiles

