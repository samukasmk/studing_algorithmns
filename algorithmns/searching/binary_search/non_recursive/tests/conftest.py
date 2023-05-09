import pytest
from random import randint


@pytest.fixture()
def unique_short_list():
    """ Creating a short list of unique elements """
    unique_short_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    unique_short_list.sort()
    return unique_short_list


@pytest.fixture()
def repeated_short_list():
    """creating a short list of repeated elements"""
    repeated_short_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10]
    repeated_short_list.sort()
    return repeated_short_list


@pytest.fixture()
def billionaire_list():
    billionaire_list = [randint(1, 1000000) for i in range(1000000)]
    billionaire_list.sort()
    return billionaire_list
