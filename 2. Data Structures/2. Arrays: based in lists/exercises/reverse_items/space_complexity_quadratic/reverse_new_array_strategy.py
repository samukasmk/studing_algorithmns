def revert_array_with_new_array_strategy(array_num):
    temp_array = []

    for index in range(len(array_num)-1, -1, -1):
        temp_value = array_num[index]
        temp_array.append(temp_value)

    return temp_array

class TestReverseArrayItemsWithNewArrayStrategy:
    def test_reverse_even_items(self):
        assert revert_array_with_new_array_strategy([0, 1, 2, 3]) == [3, 2, 1, 0]

    def test_reverse_odd(self):
        assert revert_array_with_new_array_strategy([0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])
