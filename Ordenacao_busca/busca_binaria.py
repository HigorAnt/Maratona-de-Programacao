def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio  # encontrou o elemento, retorna o índice
        elif lista[meio] < alvo:
            # o alvo está na metade direita, descarta a esquerda (incluindo o meio)
            inicio = meio + 1
        else:
            # o alvo está na metade esquerda, descarta a direita (incluindo o meio)
            fim = meio - 1
    return -1  # elemento não encontrado

lista1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Índice do 23:", busca_binaria(lista1, 23)) 
print("Índice do 100:", busca_binaria(lista1, 100))

# Versão RECURSIVA da busca binária
def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1  # caso base: intervalo vazio
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)
    else:
        return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)

print(busca_binaria_recursiva(lista1, 72, 0, len(lista1) - 1))
print(busca_binaria_recursiva(lista1, 999, 0, len(lista1) - 1))

lista_2 = [50, 3, 88, 12, 5]
print("Índice do 12 na lista desordenada:", busca_binaria(lista_2, 12))