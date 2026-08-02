import heapq

def prim(n, adjacencia, inicio=0):
    visitado = [False] * n
    heap = [(0, inicio, -1)]   # (peso, vertice, pai)
    custo_total = 0
    mst = []

    while heap:
        peso, u, pai = heapq.heappop(heap)

        if visitado[u]:
            continue

        visitado[u] = True
        custo_total += peso
        if pai != -1:
            mst.append((pai, u, peso))  # agora é uma aresta completa, igual ao Kruskal

        for v, peso_aresta in adjacencia[u]:
            if not visitado[v]:
                heapq.heappush(heap, (peso_aresta, v, u))

    return custo_total, mst

# Construindo a lista de adjacência com pesos: adjacencia[u] = [(v, peso), ...]
n = 9
adjacencia = [[] for _ in range(n)]
arestas = [
    (0, 1, 4), (0, 7, 8),
    (1, 7, 11), (1, 2, 8),
    (2, 3, 7), (2, 5, 2), (2, 8, 4),
    (3, 4, 9), (3, 5, 14),
    (4, 5, 10),
    (5, 6, 1),
    (6, 7, 2), (6, 8, 6),
    (7, 8, 7)
]

for u, v, peso in arestas:
    adjacencia[u].append((v, peso))
    adjacencia[v].append((u, peso))

custo, mst = prim(n, adjacencia)
print("Custo AGM:", custo) 
print("AGM:", mst)

# Detectando grafo desconexo: se nem todos os vértices forem visitados, não existe árvore geradora a partir do vértice inicial
def prim_verifica_conexo(n, adjacencia, inicio=0):
    visitado = [False] * n
    heap = [(0, inicio)]
    custo_total = 0
    visitados_count = 0

    while heap:
        peso, u = heapq.heappop(heap)
        if visitado[u]:
            continue
        visitado[u] = True
        visitados_count += 1
        custo_total += peso

        for v, peso_aresta in adjacencia[u]:
            if not visitado[v]:
                heapq.heappush(heap, (peso_aresta, v))

    if visitados_count != n:
        return None # grafo desconexo

    return custo_total

n_desconexo = 4
adjacencia_desconexa = [[] for _ in range(n_desconexo)]
adjacencia_desconexa[0].append((1, 1))
adjacencia_desconexa[1].append((0, 1))
adjacencia_desconexa[2].append((3, 2))
adjacencia_desconexa[3].append((2, 2))

print(prim_verifica_conexo(4, adjacencia_desconexa)) # None