def select(seq, start):
    minIndex = start

    for j in range(start + 1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j

    return minIndex


def selSort(seq):
    for i in range(len(seq) - 1):
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    selSort(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')