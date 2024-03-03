import random

def add(a, b):
    return a + b

def get_randomized_full_size():
    unique_tiles=[]
    for i in range(4):
        unique_tiles.extend(list(range(36)))
    random.shuffle(unique_tiles)
    return unique_tiles

