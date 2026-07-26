# Matriz em Python é representada como uma "lista de listas" - cada elemento da lista externa é uma linha
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)

# Acessando um elemento específico: primeiro índice é a LINHA, segundo é a COLUNA
print("Elemento [0][0]:", matriz[0][0])  
print("Elemento [1][2]:", matriz[1][2])  

# Obtendo as dimensões da matriz
quantidade_linhas = len(matriz)
quantidade_colunas = len(matriz[0])  # assume que todas as linhas têm o mesmo tamanho (matriz retangular)
print(f"Matriz {quantidade_linhas}x{quantidade_colunas}")

# CUIDADO - Criação incorreta de matriz usando multiplicação de lista:
# [[0] * colunas] * linhas cria "linhas" REFERÊNCIAS para a MESMA lista interna, não linhas independentes!
matriz_errada = [[0] * 3] * 3
matriz_errada[0][0] = 99
print("Matriz errada:", matriz_errada)

# Forma CORRETA de criar uma matriz de tamanho fixo, com list comprehension
# Cada "for" interno cria uma nova lista independente para cada linha
matriz_correta = [[0] * 3 for _ in range(3)]
matriz_correta[0][0] = 99
print("Matriz correta:", matriz_correta)

# Leitura de uma matriz a partir de várias linhas de entrada
linhas, colunas = map(int, input("Digite o número de linhas e colunas: ").split())
matriz_lida = []
for _ in range(linhas):
    linha = list(map(int, input().split()))
    matriz_lida.append(linha)
print("Matriz inserida:", matriz_lida)

# Percorrendo TODOS os elementos de uma matriz, com dois laços aninhados
print("Matriz:")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()  # pula linha ao terminar de percorrer cada linha da matriz

# Percorrendo diretamente pelos elementos, sem usar índices (quando a posição não é necessária)
print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

# Somando todos os elementos de uma matriz
soma_total = 0
for linha in matriz:
    for elemento in linha:
        soma_total += elemento
print("Soma total:", soma_total)

# Forma compacta usando sum() aninhado (soma cada linha, depois soma o resultado das linhas)
soma_compacta = sum(sum(linha) for linha in matriz)
print("Soma total (compacta):", soma_compacta)

# Transposta de uma matriz: troca linhas por colunas (elemento [i][j] vira [j][i])
def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = [[0] * linhas for _ in range(colunas)]  # dimensões invertidas: colunas x linhas

    for i in range(linhas):
        for j in range(colunas):
            resultado[j][i] = matriz[i][j]

    return resultado

print("Matriz transposta:", transposta(matriz))

# Forma alternativa de obter a transposta usando zip() - muito mais compacta
# zip(*matriz) "desempacota" cada linha como um argumento separado e as agrupa por posição
transposta_zip = [list(linha) for linha in zip(*matriz)]
print("Matriz transposta:", transposta_zip)

# Matriz identidade: 1's na diagonal principal, 0's no restante
def matriz_identidade(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("Matriz identidade:", matriz_identidade(4))

# Soma de duas matrizes de mesmas dimensões, elemento a elemento
def somar_matrizes(m1, m2):
    linhas = len(m1)
    colunas = len(m1[0])
    resultado = [[0] * colunas for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = m1[i][j] + m2[i][j]

    return resultado

matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
print("Soma das matrizes A e B:", somar_matrizes(matriz_a, matriz_b))

# Multiplicação de matrizes (produto matricial, não elemento a elemento)
def multiplicar_matrizes(m1, m2):
    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])
    colunas_m2 = len(m2[0])

    resultado = [[0] * colunas_m2 for _ in range(linhas_m1)]

    for i in range(linhas_m1):
        for j in range(colunas_m2):
            for k in range(colunas_m1):
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado

print("Produto de matrizes:", multiplicar_matrizes(matriz_a, matriz_b))

# Percorrendo apenas a diagonal principal de uma matriz quadrada
print("Diagonal principal:")
for i in range(len(matriz)):
    print(matriz[i][i], end=" ")
print()

# Percorrendo a diagonal secundária (anti-diagonal) de uma matriz quadrada
print("Diagonal secundária:")
n = len(matriz)
for i in range(n):
    print(matriz[i][n - 1 - i], end=" ")  # 3, 5, 7
print()

# Rotação de uma matriz quadrada em 90 graus (sentido horário), usando zip() + reversed()
def rotacionar_90_graus(matriz):
    return [list(linha) for linha in zip(*matriz[::-1])]

print("Matriz rotacionada:", rotacionar_90_graus(matriz))

# Verificação de matriz simétrica (matriz é igual à sua própria transposta)
def eh_simetrica(matriz):
    return matriz == transposta(matriz)

matriz_simetrica = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
print("É simétrica?", eh_simetrica(matriz_simetrica))
print("É simétrica?", eh_simetrica(matriz))