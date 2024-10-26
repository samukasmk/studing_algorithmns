def bubble_sort(array):
    n = len(array)

    for _ in range(n - 1):
        for i in range(n - 1):

            # swip elements
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubble_sort(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')
