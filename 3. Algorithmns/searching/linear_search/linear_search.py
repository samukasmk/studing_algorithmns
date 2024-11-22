"""
Solution: linear O(n)
"""
import pytest
from array import array


def linear_search(array, element_to_search):
    for i in range(len(array)):
        if array[i] == element_to_search:
            return True
    return False


class TestLinearSearch:
    def setup_method(self):
        self.zero_to_ten_array = array('b', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    @pytest.mark.parametrize("zero_to_ten_case", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_linear_search_existing_element(self, zero_to_ten_case):
        assert linear_search(self.zero_to_ten_array, zero_to_ten_case) is True

    @pytest.mark.parametrize("zero_to_ten_case", [-3, -2, -1, 11, 12, 13, 14, 1000])
    def test_linear_search_non_existing_element(self, zero_to_ten_case):
        assert linear_search(self.zero_to_ten_array, zero_to_ten_case) is False


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])
