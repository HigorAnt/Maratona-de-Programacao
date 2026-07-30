from itertools import accumulate

# itertools.accumulate(iteravel): gera as somas acumuladas (equivalente a soma de prefixos)
somas_parciais = list(accumulate([1, 2, 3, 4]))
print(somas_parciais) 

def existe_subarray_com_soma(array, alvo):
    soma_acumulada = 0
    somas_vistas = {0}
    for numero in array:
        soma_acumulada += numero
        if (soma_acumulada - alvo) in somas_vistas:
            return True
        somas_vistas.add(soma_acumulada)
    return False

print(existe_subarray_com_soma([1, 2, 3, 5], 8))
print(existe_subarray_com_soma([1, 2, 3, 5], 12))

def construir_prefix_sum_2d_itertools(matriz):
    # soma de prefixos em cada linha (acumulação horizontal), feita em C
    passo1 = [list(accumulate(linha)) for linha in matriz]

    # transpõe a matriz para transformar colunas em linhas
    transposta = list(zip(*passo1))

    # soma de prefixos em cada "linha" da transposta (ou seja, cada coluna original)
    passo2 = [list(accumulate(linha)) for linha in transposta]

    # transpõe de volta para a orientação original
    prefix_sum = list(zip(*passo2))

    return prefix_sum

def soma_submatriz_itertools(prefix_sum, linha1, coluna1, linha2, coluna2):
    total = prefix_sum[linha2][coluna2]

    if linha1 > 0:
        total -= prefix_sum[linha1 - 1][coluna2]
    if coluna1 > 0:
        total -= prefix_sum[linha2][coluna1 - 1]
    if linha1 > 0 and coluna1 > 0:
        total += prefix_sum[linha1 - 1][coluna1 - 1]

    return total

matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

prefix_sum = construir_prefix_sum_2d_itertools(matriz_exemplo)
print("Soma de prefixos 2-D:", prefix_sum)

print(soma_submatriz_itertools(prefix_sum, 1, 1, 2, 2))
print(soma_submatriz_itertools(prefix_sum, 0, 0, 1, 1))
print(soma_submatriz_itertools(prefix_sum, 0, 0, 2, 2))
print(soma_submatriz_itertools(prefix_sum, 1, 1, 1, 1))