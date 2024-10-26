def bubble_sort(data, size):
    """
    Implementation of a bubble sort algorithm with recursion.

    Arguments:
    data: list. List to be sorted
    size: int. List size

    Returns the ordered "data" list.
    """
    swap = False
    for i in range(0, size - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swap = True
    if swap:
        bubble_sort(data, size - 1)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubble_sort(numbers, len(numbers))

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')