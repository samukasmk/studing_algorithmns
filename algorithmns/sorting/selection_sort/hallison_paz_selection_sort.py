def selection_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    selection_sort(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')
