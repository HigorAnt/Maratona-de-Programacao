# Vetor é o termo comumente usado para uma lista unidimensional de tamanho conhecido
# Leitura de um vetor a partir de uma única linha de entrada
vetor = list(map(int, input("Digite os elementos do vetor separados por espaço: ").split()))
print(vetor)

# Leitura de um vetor com tamanho informado antes de receber os elementos 
n = int(input("Digite o tamanho do vetor: "))
vetor_com_tamanho = list(map(int, input("Digite os elementos: ").split()))
print(f"Vetor de tamanho {n}: {vetor_com_tamanho}")

# Criação de um vetor de tamanho fixo, preenchido com um valor inicial
tamanho = 10
vetor_zerado = [0] * tamanho
print(vetor_zerado)  

# Vetor de marcação/visitados
visitado = [False] * tamanho
visitado[3] = True
print(visitado)

# Vetor de frequência: conta quantas vezes cada valor aparece, usando o próprio valor como índice
# Só funciona bem quando os valores são pequenos e não-negativos (senão, usar dicionário/Counter)
valores = [1, 3, 3, 5, 1, 1, 2]
maior_valor = max(valores)
frequencia = [0] * (maior_valor + 1)

for valor in valores:
    frequencia[valor] += 1
print(frequencia)

# Percorrendo um vetor com índice explícito 
for i in range(len(vetor)):
    print(f"Elemento na posição {i}: {vetor[i]}")

# Percorrendo pares de elementos adjacentes
for i in range(len(vetor) - 1):
    diferenca = vetor[i + 1] - vetor[i]
    print(f"Diferença entre posição {i} e {i+1}: {diferenca}")

# Vetor 1-indexado "na prática": alguns problemas descrevem índices começando em 1
# Uma forma comum de lidar com isso é adicionar um elemento "de folga" no início do vetor
vetor_original = [10, 20, 30, 40]
vetor_um_indexado = [0] + vetor_original  # posição 0 vira "lixo", e os dados reais começam do índice 1
print(vetor_um_indexado[1])  # acessa o "primeiro" elemento como o problema descreveria (10)

# Leitura de múltiplos vetores em linhas separadas (padrão comum: primeiro a quantidade de casos, depois cada vetor)
quantidade_casos = int(input("Quantos vetores serão lidos? "))
vetores_lidos = []
for _ in range(quantidade_casos):
    vetores_lidos.append(list(map(int, input().split())))
print(vetores_lidos)

# Redimensionar um vetor (aumentar) preenchendo as novas posições com um valor padrão
vetor_pequeno = [1, 2, 3]
vetor_pequeno.extend([0] * 2)  # aumenta em 2 posições, preenchidas com 0
print("Vetor redimensionado: ", vetor_pequeno) 

# Trocar (swap) dois elementos de posição - padrão muito usado em algoritmos de ordenação manual
vetor_swap = [1, 2, 3, 4]
vetor_swap[0], vetor_swap[3] = vetor_swap[3], vetor_swap[0]
print(vetor_swap)  # [4, 2, 3, 1]

# Vetor de duas dimensões "achatado" em uma única dimensão (útil para simular matriz com um vetor só)
# Posição (linha, coluna) em uma matriz de C colunas corresponde ao índice: linha * C + coluna
linhas, colunas = 3, 4
vetor_achatado = [0] * (linhas * colunas)

def indice_matriz(linha, coluna, num_colunas):
    return linha * num_colunas + coluna

vetor_achatado[indice_matriz(1, 2, colunas)] = 99
print(vetor_achatado)  # o valor 99 estará na posição correspondente à linha 1, coluna 2

# Inversão de um vetor sem usar reverse() ou fatiamento, com dois ponteiros 
def inverter_vetor(vetor):
    esquerda = 0
    direita = len(vetor) - 1
    while esquerda < direita:
        vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]
        esquerda += 1
        direita -= 1
    return vetor

print(inverter_vetor([1, 2, 3, 4, 5])) 

# Vetor booleano usado como crivo/marcação 
limite = 20
eh_primo_vetor = [True] * (limite + 1)
eh_primo_vetor[0] = eh_primo_vetor[1] = False
print(eh_primo_vetor)