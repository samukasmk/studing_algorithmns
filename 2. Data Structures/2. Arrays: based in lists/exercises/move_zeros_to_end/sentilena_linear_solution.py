def move_zeros_to_end(nums):
    sentinela = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[sentinela], nums[i] = nums[i], nums[sentinela]
            sentinela += 1
        print("Iteração " + str(i) + ": Lista de entrada: " + str(nums))
    return nums

# print("Lista final: ", move_zeros([0, 1, 0, 3, 12]))



# def move_zeros_to_end(array_num):
#     total_elements = len(array_num)
#     print(array_num)
#     index = 0
#     while index < len(array_num):
#         array_element = array_num[index]
#         if array_element == 0:
#             array_num.pop(index)
#             array_num.append(0)
#         print(index, array_element, array_num)
#         index += 1




    # for index in range(total_elements):
    #
    #     array_element = array_num[index]
    #     if array_element == 0:
    #         array_num.pop(index)
    #         array_num.append(0)
    #
    #
    # return array_num

if __name__ == '__main__':
    # initial_array_input = [0, 1, 0, 3, 12, 0]
    # expected_array_output = [1, 3, 12, 0, 0, 0]
    # returned_array_output = move_zeros_to_end(initial_array_input)
    # print(f'Zeros moved ({expected_array_output == returned_array_output}):', returned_array_output)
    # ">>> Zeros moved (True): [1, 3, 12, 0, 0, 0]"
    # assert expected_array_output == returned_array_output

    initial_array_input = [0, 1, 2, 0, 19, 0, 39, 9, 0, 9, 28, 0, 0, 0, 18, 2, 8]
    expected_array_output = [1, 2, 19, 39, 9, 9, 28, 18, 2, 8, 0, 0, 0, 0, 0, 0, 0]
    returned_array_output = move_zeros_to_end(initial_array_input)
    print(f'Zeros moved ({expected_array_output == returned_array_output}):', returned_array_output)
    ">>> Zeros moved (True): [1, 2, 19, 39, 9, 9, 28, 18, 2, 8, 0, 0, 0, 0, 0, 0, 0]"
    assert expected_array_output == returned_array_output