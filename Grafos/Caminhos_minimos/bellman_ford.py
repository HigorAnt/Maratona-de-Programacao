def bellman_ford(n, arestas, origem):
    dist = [float('inf')] * n
    dist[origem] = 0

    # Relaxa todas as arestas n-1 vezes
    for _ in range(n - 1):
        for u, v, peso in arestas:
            if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso

    # N-ésima rodada: se ainda houver relaxamento, há ciclo negativo
    for u, v, peso in arestas:
        if dist[u] != float('inf') and dist[u] + peso < dist[v]:
            return dist, True   # ciclo negativo detectado
    return dist, False

n = 5
arestas = [(0, 1, 6), (0, 2, 7), (1, 2, 8), (1, 3, 5), (1, 4, -4), 
    (2, 3, -3), (2, 4, 9), (3, 1, -2), (4, 3, 7), (4, 0, 2),]

dist, ciclo_neg = bellman_ford(n, arestas, 0)
print(f"Distâncias: {dist}. Ciclo negativo: {ciclo_neg}")

# Reconstruindo o caminho mínimo até um destino específico
def bellman_ford_com_caminho(n, arestas, origem):
    dist = [float('inf')] * n
    dist[origem] = 0
    anterior = [-1] * n

    for _ in range(n - 1):
        for u, v, peso in arestas:
            if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                anterior[v] = u
    return dist, anterior

def reconstruir_caminho(anterior, destino):
    caminho = []
    while destino != -1:
        caminho.append(destino)
        destino = anterior[destino]
    return caminho[::-1]

dist, anterior = bellman_ford_com_caminho(5, arestas, 0)
print(reconstruir_caminho(anterior, 3))