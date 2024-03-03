import pytest
from src.common.tilemap import get_randomized_full_set

def test_full_set():
    full_set = get_randomized_full_set()  
    assert len(full_set) == 144
    assert sum(full_set) ==  4 * sum(range(36)) 


