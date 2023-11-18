def revert_array_with_for_strategy(nums):
    length = len(nums)
    last_index = length - 1

    stop_half_items = int(length // 2)

    for left_index in range(stop_half_items):
        rigth_index = last_index - left_index
        nums[left_index], nums[rigth_index] = nums[rigth_index], nums[left_index]
    return nums


class TestReverseArrayItemsWithForLoopStrategy:
    def test_reverse_even_items(self):
        assert revert_array_with_for_strategy([0, 1, 2, 3]) == [3, 2, 1, 0]

    def test_reverse_odd(self):
        assert revert_array_with_for_strategy([0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])
