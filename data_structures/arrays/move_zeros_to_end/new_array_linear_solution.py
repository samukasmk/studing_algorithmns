def move_zeros_to_end(array_num):
    total_elements = len(array_num)
    new_array = []
    count_zeros_found = 0

    # get array elements only different than zero
    for index in range(total_elements):
        array_element = array_num[index]
        if array_element != 0:
            new_array.append(array_element)
        else:
            count_zeros_found += 1

    # append zeros to the end of array
    new_array += [0] * count_zeros_found

    return new_array

if __name__ == '__main__':
    initial_array_input = [0, 1, 0, 3, 12, 0]
    expected_array_output = [1, 3, 12, 0, 0, 0]
    returned_array_output = move_zeros_to_end(initial_array_input)
    print(f'Zeros moved ({expected_array_output == returned_array_output}):', returned_array_output)
    ">>> Zeros moved (True): [1, 3, 12, 0, 0, 0]"
    assert expected_array_output == returned_array_output

    initial_array_input = [0, 1, 2, 0, 19, 0, 39, 9, 0, 9, 28, 0, 0, 0, 18, 2, 8]
    expected_array_output = [1, 2, 19, 39, 9, 9, 28, 18, 2, 8, 0, 0, 0, 0, 0, 0, 0]
    returned_array_output = move_zeros_to_end(initial_array_input)
    print(f'Zeros moved ({expected_array_output == returned_array_output}):', returned_array_output)
    ">>> Zeros moved (True): [1, 2, 19, 39, 9, 9, 28, 18, 2, 8, 0, 0, 0, 0, 0, 0, 0]"
    assert expected_array_output == returned_array_output