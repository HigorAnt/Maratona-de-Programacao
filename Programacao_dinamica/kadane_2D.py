# Kadane tradicional: retorna a maior soma de subarray contíguo. Tempo: O(n)
def kadane_1d(array: list) -> int:
    soma_atual = array[0]
    soma_maxima = array[0]

    for i in range(1, len(array)):
        soma_atual = max(array[i], soma_atual + array[i])
        soma_maxima = max(soma_maxima, soma_atual)

    return soma_maxima

# Kadane 2D com otimização de dimensão: sempre fixa pares de índices na dimensão MENOR da matriz (transpondo se necessário), 
# garantindo complexidade O(min(R,C)^2 * max(R,C)) em vez de assumir cegamente O(R^2 * C), o que é péssimo para matrizes muito retangulares.
def kadane_2d_otimizado(matriz: list) -> int:
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Se há mais linhas que colunas, transpõe a matriz para que o laço externo (o que é elevado ao quadrado) opere sobre a dimensão menor
    if linhas > colunas:
        matriz = [list(linha) for linha in zip(*matriz)]
        linhas, colunas = colunas, linhas

    maior_soma = float("-inf")

    for topo in range(linhas):
        soma_colunas = [0] * colunas

        for base in range(topo, linhas):
            for c in range(colunas):
                soma_colunas[c] += matriz[base][c]

            maior_soma = max(maior_soma, kadane_1d(soma_colunas))

    return maior_soma

# Kadane tradicional, mas também retorna os índices [inicio, fim] do subarray que produz a soma máxima. Tempo: O(n).
def kadane_1d_com_indices(array: list) -> tuple[int, int, int]:
    soma_atual = array[0]
    soma_maxima = array[0]

    inicio_atual = 0
    inicio_melhor = 0
    fim_melhor = 0

    for i in range(1, len(array)):
        if array[i] > soma_atual + array[i]:
            soma_atual = array[i]
            inicio_atual = i
        else:
            soma_atual += array[i]

        if soma_atual > soma_maxima:
            soma_maxima = soma_atual
            inicio_melhor = inicio_atual
            fim_melhor = i

    return soma_maxima, inicio_melhor, fim_melhor

# Retorna a maior soma de submatriz contígua, junto com os índices (linha_topo, linha_base, coluna_esquerda, coluna_direita) que a delimitam
# Tempo: O(min(R,C)^2 * max(R,C))
def kadane_2d_com_submatriz(matriz: list) -> tuple[int, tuple[int, int, int, int]]:
    linhas_original = len(matriz)
    colunas_original = len(matriz[0])
    transposta = linhas_original > colunas_original

    if transposta:
        matriz = [list(linha) for linha in zip(*matriz)]

    linhas = len(matriz)
    colunas = len(matriz[0])

    maior_soma = float("-inf")
    melhor_topo = melhor_base = melhor_esq = melhor_dir = 0

    for topo in range(linhas):
        soma_colunas = [0] * colunas

        for base in range(topo, linhas):
            for c in range(colunas):
                soma_colunas[c] += matriz[base][c]

            soma, esq, dir_ = kadane_1d_com_indices(soma_colunas)

            if soma > maior_soma:
                maior_soma = soma
                melhor_topo, melhor_base = topo, base
                melhor_esq, melhor_dir = esq, dir_

    # Se a matriz foi transposta, os papéis de linha/coluna precisam ser invertidos de volta para corresponder à matriz original fornecida
    if transposta:
        return maior_soma, (melhor_esq, melhor_dir, melhor_topo, melhor_base)
    else:
        return maior_soma, (melhor_topo, melhor_base, melhor_esq, melhor_dir)

# Extrai a submatriz de 'matriz' dado (linha_topo, linha_base, coluna_esq, coluna_dir)
def extrair_submatriz(matriz: list, indices: tuple[int, int, int, int]) -> list:
    linha_topo, linha_base, coluna_esq, coluna_dir = indices
    return [linha[coluna_esq:coluna_dir + 1] for linha in matriz[linha_topo:linha_base + 1]]

def main():
    matriz_exemplo = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]
   
    # Matriz bem retangular: 3 linhas, muitas colunas -> se beneficia de transpor
    matriz_retangular = [
        [1, -5, 2, 3, -1, 4],
        [2, -1, -3, 4, 1, -2],
        [-1, 3, 2, -4, 5, 1]
    ]

    matriz_exemplo = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]

    matriz_negativa = [
        [-1, -1, -1],
        [-1, 5, 5],
        [-1, 5, 5]
    ]
    
    soma, indices = kadane_2d_com_submatriz(matriz_exemplo)
    soma2, indices2 = kadane_2d_com_submatriz(matriz_negativa)

    print("Maior soma:", kadane_2d_otimizado(matriz_exemplo)) 
    print("Maior soma:", kadane_2d_otimizado(matriz_retangular))
    print("Maior soma:", soma)
    print("Índices (topo, base, esq, dir):", indices)
    print("Submatriz:", extrair_submatriz(matriz_exemplo, indices))
    print("Maior soma:", soma2)
    print("Submatriz:", extrair_submatriz(matriz_negativa, indices2))

main()