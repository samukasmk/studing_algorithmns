def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[i] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave

if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    insertion_sort(numbers)
    print(f'Final list: {numbers}')

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100], f'Final list: {numbers} is not equal than: [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]'

    # print the sorted list
    print(f'Sorted list: {numbers}')