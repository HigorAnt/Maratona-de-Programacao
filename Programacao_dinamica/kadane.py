def kadane(array):
    # Inicializa ambas as variáveis com o primeiro elemento (cobre o caso de array com um único elemento)
    soma_atual = array[0]
    soma_maxima = array[0]

    for i in range(1, len(array)):
        # Decide se é melhor começar um novo subarray a partir daqui, ou estender o subarray anterior
        soma_atual = max(array[i], soma_atual + array[i])

        # Atualiza a maior soma encontrada até agora, se necessário
        soma_maxima = max(soma_maxima, soma_atual)

    return soma_maxima

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Soma máxima:", kadane(array))

# Variação: Kadane que também retorna os ÍNDICES do subarray que gera a soma máxima
def kadane_com_indices(array):
    soma_atual = array[0]
    soma_maxima = array[0]
    inicio = 0
    melhor_inicio = 0
    melhor_fim = 0

    for i in range(1, len(array)):
        if array[i] > soma_atual + array[i]:
            # Melhor começar um novo subarray a partir do índice i
            soma_atual = array[i]
            inicio = i
        else:
            # Melhor estender o subarray que já vinha sendo formado
            soma_atual += array[i]

        if soma_atual > soma_maxima:
            soma_maxima = soma_atual
            melhor_inicio = inicio
            melhor_fim = i

    return soma_maxima, melhor_inicio, melhor_fim

resultado, inicio, fim = kadane_com_indices(array)
print(f"Soma = {resultado}. Índices do subvetor: {inicio}-{fim}")
print("Elementos do subvetor:", array[inicio:fim + 1])

# Caso especial: array com todos os valores negativos - Kadane ainda funciona, retornando o "menos negativo"
array_negativo = [-3, -1, -4, -2, -5]
print("Soma máxima:", kadane(array_negativo))