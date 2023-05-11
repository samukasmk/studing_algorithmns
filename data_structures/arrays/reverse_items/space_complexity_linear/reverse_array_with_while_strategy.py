def revert_array_with_while_loop_strategy(numbered_array):
    begin_index = 0
    end_index = len(numbered_array) - 1

    while begin_index < end_index:
        begin_value = numbered_array[end_index]
        end_value = numbered_array[begin_index]

        numbered_array[begin_index] = begin_value
        numbered_array[end_index] = end_value

        begin_index += 1
        end_index -= 1

    return numbered_array

class TestReverseArrayItemsWithWhileLoopStrategy:
    def test_reverse_even_items(self):
        assert revert_array_with_while_loop_strategy([0, 1, 2, 3]) == [3, 2, 1, 0]

    def test_reverse_odd(self):
        assert revert_array_with_while_loop_strategy([0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])