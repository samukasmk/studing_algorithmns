def selection_sort(array):
    n = len(array)

    for leftmost in range(n - 1):
        minor = leftmost

        for i in range(leftmost, n):
            if array[i] < array[minor]:
                minor = i

        if minor != leftmost:
            array[leftmost], array[minor] = array[minor], array[leftmost]


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    selection_sort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
