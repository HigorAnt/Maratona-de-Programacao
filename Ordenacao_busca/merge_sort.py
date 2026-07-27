def merge_sort(lista):
    # Caso base: uma lista vazia ou com um único elemento já está, por definição, ordenada
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio (estratégia de dividir para conquistar)
    meio = len(lista) // 2
    metade_esquerda = merge_sort(lista[:meio])   # ordena recursivamente a metade esquerda
    metade_direita = merge_sort(lista[meio:])    # ordena recursivamente a metade direita

    # Mescla as duas metades já ordenadas em uma única lista ordenada
    return mesclar(metade_esquerda, metade_direita)

def mesclar(esquerda, direita):
    # Combina duas listas JÁ ORDENADAS em uma única lista ordenada, usando dois ponteiros
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona o restante da lista que ainda não foi totalmente percorrida
    # (uma das duas sempre chega ao fim primeiro; a outra pode ainda ter elementos "sobrando")
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

print("[5, 2, 9, 1, 5, 6] ordenados:", merge_sort([5, 2, 9, 1, 5, 6]))
print("[1, 2, 3, 4, 5] ordenados:", merge_sort([1, 2, 3, 4, 5]))

# Casos extremos: lista vazia e lista de um único elemento
print("[] ordenado:", merge_sort([]))
print("[3] ordenado:", merge_sort([3]))

# Pior caso possível: lista completamente invertida
print("[5, 4, 3, 2, 1] ordenados:", merge_sort([5, 4, 3, 2, 1]))

# Funciona também com números negativos, sem nenhuma alteração necessária
print("[-3, 5, -1, 0, 8, -8] ordenados:", merge_sort([-3, 5, -1, 0, 8, -8]))