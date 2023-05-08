import pytest
from algorithmns.searching.linear_search.linear_search import linear_search


@pytest.mark.parametrize("zero_to_ten_case", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_linear_search_existing_element(zero_to_ten_array, zero_to_ten_case):
    assert linear_search(zero_to_ten_array, zero_to_ten_case) is True


@pytest.mark.parametrize("zero_to_ten_case", [-3, -2, -1, 11, 12, 13, 14, 1000])
def test_linear_search_non_existing_element(zero_to_ten_array, zero_to_ten_case):
    assert linear_search(zero_to_ten_array, zero_to_ten_case) is False