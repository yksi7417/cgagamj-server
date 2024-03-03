import pytest
from src.common.tilemap import add, get_randomized_full_size

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_full_set():
    full_set = get_randomized_full_size()  
    assert len(full_set) == 144
    assert sum(full_set) ==  4 * sum(range(36)) 


