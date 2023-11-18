def encontra_elementos_duplicados(lista, m):
    """
    Imprime os números que aparecem mais de uma vez na lista de entrada.
    É garantido que todos os números na lista de entrada estão no intervalo [0, m].
    """
    # Retorna zero se a lista de entrada estiver vazia.
    if not lista:
        return []

    # Procura por elementos repetidos na lista.
    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicatas.append(lista[j])

    # A saída do algoritmo é a lista de elementos repetidos.
    return duplicatas

if __name__ == '__main__':
    elementos_duplicados = encontra_elementos_duplicados([1, 1, 20, 3, 3, 80, 7, 2, 25, 99, 75, 80], 100)
    assert elementos_duplicados == [1, 3, 80]
    print("Elementos duplicados: ", elementos_duplicados)
    ">>> Elementos duplicados:  [1, 3, 80]"

