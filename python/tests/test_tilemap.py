import pytest
from src.common.tilemap import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_full_set():
    full_set = byte[144] // Cantonese MJ has 144 tiles 
    assert len(full_set) == 144 
    