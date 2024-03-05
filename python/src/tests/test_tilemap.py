import pytest

from common.tilemap import get_randomized_full_set, get_suit
from common.SuitEnum import SuitEnum

def test_full_set():
    full_set = get_randomized_full_set()  
    assert len(full_set) == 144
    assert sum(full_set) ==  10296


def test_map_number_to_tiles():
    for i in range(1,11):
        assert get_suit(i) == SuitEnum.BAMBOO