""" Implementação de um algoritmo de selection sort com recursão """


def selection_sort(vetor, indice):
    """
    Implementação de um algoritmo de selection sort com recursão.

    Argumentos:
    vetor: lista. Lista que será ordenada
    indice: int. Indice do elemento a ser ordenado na lista

    Retorna a lista "vetor" ordenada.
    """
    if indice >= len(vetor) - 1:
        return -1

    # minIndice guarda a posicao onde esta o menor valor em relacao ao indice
    min_indice = indice

    for i in range(indice + 1, len(vetor)):
        if vetor[i] < vetor[min_indice]:
            min_indice = i

    temp = vetor[indice]
    vetor[indice] = vetor[min_indice]
    vetor[min_indice] = temp

    selection_sort(vetor, indice + 1)

    return vetor


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    selection_sort(numbers, 0)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')
