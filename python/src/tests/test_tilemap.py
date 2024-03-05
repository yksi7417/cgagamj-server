import pytest

from common.tilemap import get_randomized_full_set, get_suit, get_card_number
from common.SuitEnum import SuitEnum

def test_full_set():
    full_set = get_randomized_full_set()  
    assert len(full_set) == 144
    assert sum(full_set) ==  10296


def test_map_number_to_tiles_for_bamboos():
    tile_num = 0 
    for j in range(4):
        for i in range(9):
            assert get_suit(tile_num) == SuitEnum.BAMBOO
            assert get_card_number(tile_num) == i
            assert tile_num >= 0
            assert tile_num <= 35
            tile_num+=1

    ##  0,9,18,27 -> 1 BAMBOO
    ##  ...
    ##  4,13,22,31 -> 5 BAMBOO

    ##  There are 4 five_bamboos 
    five_bamboos = [4,13,22,31]
    for five_bamboo in five_bamboos:
        assert get_suit(five_bamboo) == SuitEnum.BAMBOO
        assert get_card_number(five_bamboo) == 4  # zero indexing 

def test_map_number_to_tiles_for_characters():
    tile_num = 36 
    for j in range(4):
        for i in range(9):
            assert get_suit(tile_num) == SuitEnum.CHARACTER
            assert get_card_number(tile_num) == i
            assert tile_num >= 36
            assert tile_num <= 72
            tile_num+=1

    ##  36,45,54,63 -> 1 character
    one_characters = [ 36,45,54,63]
    for one_character in one_characters:
        assert get_suit(one_character) == SuitEnum.CHARACTER
        assert get_card_number(one_character) == 0  # zero indexing 

def test_map_number_to_tiles_for_dots():
    tile_num = 72
    for j in range(4):
        for i in range(9):
            assert get_suit(tile_num) == SuitEnum.DOT
            assert get_card_number(tile_num) == i
            assert tile_num >= 72
            assert tile_num <= 108
            tile_num+=1

def test_map_number_to_tiles_for_winds_and_dragons():
    tile_num = 108
    for j in range(4):
        for i in range(4):
            assert get_suit(tile_num) == SuitEnum.WINDS
            assert get_card_number(tile_num) == i
            tile_num+=1
    for j in range(4):
        for i in range(3):
            assert get_suit(tile_num) == SuitEnum.DRAGONS
            assert get_card_number(tile_num) == i
            tile_num+=1
    assert tile_num == 136


def test_map_number_to_tiles_for_flowers_and_seasons():
    tile_num = 136
    for i in range(4):
        assert get_suit(tile_num) == SuitEnum.FLOWERS
        assert get_card_number(tile_num) == i
        tile_num+=1
    for i in range(4):
        assert get_suit(tile_num) == SuitEnum.SEASONS
        assert get_card_number(tile_num) == i
        tile_num+=1
    assert tile_num == 144 
