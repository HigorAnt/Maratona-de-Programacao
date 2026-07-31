# Exemplo 1: Dois ponteiros em array ORDENADO - encontrar um par cuja soma seja igual a um alvo
def par_com_soma(lista_ordenada, alvo):
    esquerda = 0
    direita = len(lista_ordenada) - 1

    while esquerda < direita:
        soma_atual = lista_ordenada[esquerda] + lista_ordenada[direita]

        if soma_atual == alvo:
            return (lista_ordenada[esquerda], lista_ordenada[direita])
        elif soma_atual < alvo:
            # soma pequena demais: precisa de um valor maior, então avança o ponteiro da esquerda
            esquerda += 1
        else:
            # soma grande demais: precisa de um valor menor, então recua o ponteiro da direita
            direita -= 1

    return None  # nenhum par encontrado

lista = [1, 3, 4, 6, 8, 11]
print("Par com soma igula a 11:", par_com_soma(lista, 11))

# Exemplo 2: Merge de duas listas JÁ ORDENADAS usando dois ponteiros (base do merge sort)
def mesclar_listas_ordenadas(lista1, lista2):
    resultado = []
    i = j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Adiciona o restante da lista que ainda não foi totalmente percorrida
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado

print("Mesclagem das listas:", mesclar_listas_ordenadas([1, 3, 5], [2, 4, 6]))

# Exemplo 3: trio que soma um valor alvo (3Sum) - combina loop externo + dois ponteiros
def trio_com_soma(lista, alvo):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    trios = []

    for i in range(n - 2):
        # evita reprocessar o mesmo valor fixo (evita trios duplicados)
        if i > 0 and lista_ordenada[i] == lista_ordenada[i - 1]:
            continue

        esquerda = i + 1
        direita = n - 1

        while esquerda < direita:
            soma_atual = lista_ordenada[i] + lista_ordenada[esquerda] + lista_ordenada[direita]

            if soma_atual == alvo:
                trios.append((lista_ordenada[i], lista_ordenada[esquerda], lista_ordenada[direita]))
                esquerda += 1
                direita -= 1
                # pula duplicatas para não repetir o mesmo trio
                while esquerda < direita and lista_ordenada[esquerda] == lista_ordenada[esquerda - 1]:
                    esquerda += 1
                while esquerda < direita and lista_ordenada[direita] == lista_ordenada[direita + 1]:
                    direita -= 1
            elif soma_atual < alvo:
                esquerda += 1
            else:
                direita -= 1

    return trios

print("Trio que soma resulta em 0:", trio_com_soma([-1, 0, 1, 2, -1, -4], 0))

# caso os dados não estejam ordenados
def par_com_soma_hash(lista, alvo):
    vistos = set()
    for x in lista:
        if (alvo - x) in vistos:
            return (alvo - x, x)
        vistos.add(x)
    return None

print("Par com soma igual a 13:", par_com_soma_hash([1, 3, 5, 9, 10, 2], 13))