def invert_array_positions(array_num):
    temp_array = []

    for index in range(len(array_num)-1, -1, -1):
        temp_value = array_num[index]
        temp_array.append(temp_value)

    return temp_array

if __name__ == '__main__':
    array_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    invert_array_num = invert_array_positions(array_num)
    assert invert_array_num == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print('Inverted array positions:', invert_array_num)
    ">>> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]"