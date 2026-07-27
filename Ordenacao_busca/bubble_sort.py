def bubble_sort(lista):
    n = len(lista)

    # A cada passagem externa, o maior elemento "borbulha" até sua posição final correta
    for i in range(n - 1):
        trocou = False  # controla se alguma troca ocorreu nesta passagem

        # A cada passagem, o final da lista (últimos "i" elementos) já está ordenado,
        # por isso o laço interno pode ser encurtado progressivamente
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # troca (swap) os elementos adjacentes
                trocou = True

        # OTIMIZAÇÃO: se não houve nenhuma troca nesta passagem, a lista já está ordenada,
        # e é possível interromper mais cedo, sem precisar completar todas as passagens restantes
        if not trocou:
            break

    return lista

print("[5, 2, 9, 1, 5, 6] ordenados:", bubble_sort([5, 2, 9, 1, 5, 6]))

# Caso já ordenado: com a otimização do "trocou", o algoritmo percebe isso já na primeira passagem
print("[1, 2, 3, 4, 5] ordenados:", bubble_sort([1, 2, 3, 4, 5]))

# Casos extremos: lista vazia e lista de um único elemento
print("[] ordenado:", bubble_sort([]))
print("[3] ordenado:", bubble_sort([3]))

# Pior caso possível: lista completamente invertida, exige o número máximo de trocas
print("[5, 4, 3, 2, 1] ordenados:", bubble_sort([5, 4, 3, 2, 1]))