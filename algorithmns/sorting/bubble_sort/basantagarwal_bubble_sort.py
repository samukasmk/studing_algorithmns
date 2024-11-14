# unordered_list = [5, 2]
#
# temp = unordered_list[0]
# unordered_list[0] = unordered_list[1]
# unordered_list[1] = temp
#
# print(unordered_list)



def bubble_sort(unordered_list):
    iteration_number = len(unordered_list)-1
    for i in range(iteration_number,0,-1):
        for j in range(i):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp




# my_list = [4,3,2,1]
# bubble_sort(my_list)
# print(my_list)
#
# my_list = [1,12,3,4]
# bubble_sort(my_list)
# print(my_list)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubble_sort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
