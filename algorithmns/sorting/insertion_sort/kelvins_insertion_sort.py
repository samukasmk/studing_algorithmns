""" Insertion Sort in Python (Iterative and Recursive) """


def insertion_sort_iterative(vector):
    """
    Implementation of insertion sort iteratively.

    Arguments:
        vector (list): list to be sorted.

    Returns:
        Returns the sorted list.
    """
    for i in range(1, len(vector)):
        key = vector[i]
        aux = i - 1
        while aux >= 0 and vector[aux] > key:
            vector[aux + 1] = vector[aux]
            aux -= 1
        vector[aux + 1] = key
    return vector


def insertion_sort_recursive(vector, index):
    """
    Implementation of insertion sort recursively.

    Arguments:
        vector (list): list to be sorted.
        index (int): index of the element to be sorted in the list.

    Returns:
        Returns the sorted list.
    """
    aux = index
    while vector[aux] < vector[aux - 1]:
        temp = vector[aux]
        vector[aux] = vector[aux - 1]
        vector[aux - 1] = temp
        aux -= 1
        if aux == 0:
            break
    if index < len(vector) - 1:
        insertion_sort_recursive(vector, index + 1)
    return vector


# if __name__ == "__main__":
#     list1 = [8, 1, 3, 5, 7, 9, 0, 2, 4, 6]
#     print("Unsorted list: ")
#     print(list1)
#
#     list1 = insertion_sort_iterative(list1)
#     print("Sorted list with iterative insertion sort: ")
#     print(list1)
#
#     list2 = [8, 1, 3, 5, 7, 9, 0, 2, 4, 6]
#     print("Unsorted list: ")
#     print(list2)
#
#     list2 = insertion_sort_recursive(list2, 1)
#     print("Sorted list with recursive insertion sort: ")
#     print(list2)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    insertion_sort_iterative(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100], f"List is not sorted: {numbers}"

    # print the sorted list
    print(f'Sorted list: {numbers}')


    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    insertion_sort_recursive(numbers, 0)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100], f"List is not sorted: {numbers}"

    # print the sorted list
    print(f'Sorted list: {numbers}')