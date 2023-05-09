def swip_positions(array_nums):
    begin = 0
    end = len(array_nums) - 1

    while begin < end:
        new_begin_value = array_nums[end]
        new_end_value = array_nums[begin]

        array_nums[begin] = new_begin_value
        array_nums[end] = new_end_value

        begin += 1
        end -= 1

    return array_nums

if __name__ == '__main__':
    array_nums = [0, 2, 4, 6, 8, 10]
    swipped_array = swip_positions(array_nums)
    assert swipped_array == [10, 8, 6, 4, 2, 0]
    print('Inverted positions:', swipped_array)
    ">>> [10, 8, 6, 4, 2, 0]"
