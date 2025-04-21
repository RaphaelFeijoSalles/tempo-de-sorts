def insertion_sort(lista):
    for i in range(1, len(lista)):  # Começa do segundo elemento
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]  # Move os elementos para a direita
            j -= 1
        lista[j + 1] = chave  # Insere o elemento na posição correta
        print (lista)
    return lista
