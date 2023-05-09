

def binary_search_non_recursive_end(array, element_to_search):
    inicio = -1
    fim = len(array)
    contador = 0

    while inicio < fim - 1:
        contador += 1

        meio = (inicio + fim) // 2
        # if array[meio] == element_to_search:
        #     return meio
        if array[meio] < element_to_search:
            inicio = meio
        else:
            fim = meio

    index_position = fim
    # return fim

    print('binary_search_non_recursive_end contador:', contador)
    print('binary_search_non_recursive_end index position:', index_position)
    print('binary_search_non_recursive_end value:', array[index_position] if index_position < len(array) else None)


def binary_search_non_recursive_return(array, element_to_search):
    inicio = -1
    fim = len(array)
    contador = 0
    index_position = None

    while inicio < fim - 1:
        contador += 1

        meio = (inicio + fim) // 2
        if array[meio] == element_to_search:
            # return meio
            index_position = meio
            break
        elif array[meio] < element_to_search:
            inicio = meio
        else:
            fim = meio

    print('binary_search_non_recursive_return contador:', contador)
    print('binary_search_non_recursive_return index position:', index_position)
    print('binary_search_non_recursive_return value:', array[index_position] if index_position < len(array) else None)

# array_of_numbers = [0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 10, 10, 11]
# element_to_search = 0

# binary_search_non_recursive_end(element_to_search, array_of_numbers)
# binary_search = binary_search_non_recursive_end
binary_search = binary_search_non_recursive_return

