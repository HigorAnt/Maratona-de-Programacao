import heapq

def dijkstra(n, adjacencia, origem):
    dist = [float('inf')] * n
    dist[origem] = 0
    heap = [(0, origem)] # (distancia, vertice)

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue # essa entrada da heap está desatualizada, ignora

        for v, peso in adjacencia[u]:
            nova_dist = d + peso
            if nova_dist < dist[v]:
                dist[v] = nova_dist
                heapq.heappush(heap, (nova_dist, v))

    return dist

n = 5
adjacencia = [[] for _ in range(n)]
arestas = [
    (0, 1, 10), (0, 2, 3),
    (1, 2, 1), (2, 1, 4),
    (1, 3, 2), (2, 3, 8),
    (2, 4, 2), (3, 4, 7),
    (4, 3, 9),
]

for u, v, peso in arestas:
    adjacencia[u].append((v, peso)) # grafo direcionado

dist = dijkstra(n, adjacencia, 0)
print(dist) 

# Reconstruindo o caminho mínimo até um destino específico
def dijkstra_com_caminho(n, adjacencia, origem):
    dist = [float('inf')] * n
    dist[origem] = 0
    anterior = [-1] * n
    heap = [(0, origem)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue

        for v, peso in adjacencia[u]:
            nova_dist = d + peso
            if nova_dist < dist[v]:
                dist[v] = nova_dist
                anterior[v] = u
                heapq.heappush(heap, (nova_dist, v))

    return dist, anterior

def reconstruir_caminho(anterior, destino):
    caminho = []
    while destino != -1:
        caminho.append(destino)
        destino = anterior[destino]
    return caminho[::-1]

dist, anterior = dijkstra_com_caminho(n, adjacencia, 0)
print(dist, anterior)
print(reconstruir_caminho(anterior, 4))