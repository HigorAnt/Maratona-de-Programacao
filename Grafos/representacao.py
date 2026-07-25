from collections import defaultdict
import sys

# ========== Lista de Adjacência ==========
# Cada vértice aponta para uma lista de seus vizinhos - eficiente em memória para grafos ESPARSOS
# (poucas arestas em relação ao número de vértices)

# Construção a partir de uma lista de arestas, para um grafo NÃO DIRECIONADO e NÃO PONDERADO
def construir_lista_adjacencia(vertices, arestas, direcionado=False):
    grafo = defaultdict(list)

    for v in range(vertices):
        grafo[v]  # garante que todo vértice apareça no dicionário, mesmo sem nenhuma aresta

    for u, v in arestas:
        grafo[u].append(v)
        if not direcionado:
            grafo[v].append(u)

    return grafo

arestas_exemplo = [(0, 1), (0, 2), (1, 2), (2, 3)]
grafo_lista = construir_lista_adjacencia(4, arestas_exemplo)
print("Lista de adjacência do grafo:", dict(grafo_lista))

# Versão PONDERADA: cada vizinho é armazenado junto com o peso da aresta, como uma tupla (vizinho, peso)
def construir_lista_adjacencia_ponderada(vertices, arestas, direcionado=False):
    grafo = defaultdict(list)

    for v in range(vertices):
        grafo[v]

    for u, v, peso in arestas:
        grafo[u].append((v, peso))
        if not direcionado:
            grafo[v].append((u, peso))

    return grafo

arestas_ponderadas = [(0, 1, 5), (0, 2, 3), (1, 2, 1), (2, 3, 7)]
grafo_lista_ponderado = construir_lista_adjacencia_ponderada(4, arestas_ponderadas)
print("Lista de adjacência do grafo ponderado:", dict(grafo_lista_ponderado))

# Percorrendo os vizinhos de um vértice específico
for vizinho in grafo_lista[0]:
    print(f"Vizinho de 0: {vizinho}")

# ========== Matriz de Adjacência ==========
# Uma matriz V x V, onde a posição [i][j] indica se existe aresta entre i e j (e opcionalmente o peso)
# Eficiente para grafos DENSOS (muitas arestas), e permite verificar a existência de uma aresta em O(1)

def construir_matriz_adjacencia(vertices, arestas, direcionado=False):
    matriz = [[0] * vertices for _ in range(vertices)]

    for u, v in arestas:
        matriz[u][v] = 1
        if not direcionado:
            matriz[v][u] = 1

    return matriz

matriz = construir_matriz_adjacencia(4, arestas_exemplo)
print("Matriz de adjacência:")
for linha in matriz:
    print(linha)

# Versão PONDERADA: armazena o peso da aresta na posição correspondente, e "infinito" onde não há aresta
def construir_matriz_adjacencia_ponderada(vertices, arestas, direcionado=False):
    matriz = [[float('inf')] * vertices for _ in range(vertices)]

    for i in range(vertices):
        matriz[i][i] = 0

    for u, v, peso in arestas:
        matriz[u][v] = peso
        if not direcionado:
            matriz[v][u] = peso

    return matriz

matriz_ponderada = construir_matriz_adjacencia_ponderada(4, arestas_ponderadas)
print("Matriz de adjacência ponderada:")
for linha in matriz_ponderada:
    print(linha)

# Verificando a existência de uma aresta específica em O(1) - vantagem da matriz sobre a lista
print("Existe aresta entre 0 e 1?", matriz[0][1])  # 1, existe aresta entre 0 e 1
print("Existe aresta entre 0 e 3?", matriz[0][3])  # 0, não existe aresta entre 0 e 3

# ========== Comparação de uso de memória entre as duas representações ==========
# Para um grafo ESPARSO (poucas arestas em relação aos vértices), a diferença de memória é expressiva
vertices_teste = 1000
arestas_teste = [(i, i + 1) for i in range(vertices_teste - 1)]  # grafo esparso: só 999 arestas

lista_teste = construir_lista_adjacencia(vertices_teste, arestas_teste)
matriz_teste = construir_matriz_adjacencia(vertices_teste, arestas_teste)

tamanho_lista = sum(sys.getsizeof(v) for v in lista_teste.values())
tamanho_matriz = sum(sys.getsizeof(linha) for linha in matriz_teste)

print(f"Lista de adjacência: aproximadamente {tamanho_lista} bytes")  
print(f"Matriz de adjacência: aproximadamente {tamanho_matriz} bytes") 
# A lista de adjacência usa cerca de 90x menos memória neste grafo esparso