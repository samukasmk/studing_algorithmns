import pytest
from array import array

@pytest.fixture()
def zero_to_ten_array():
    return array('b', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])