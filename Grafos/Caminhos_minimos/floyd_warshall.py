def floyd_warshall(n, arestas):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, peso in arestas:
        dist[u][v] = min(dist[u][v], peso)   # cuidado com arestas paralelas

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

n = 4
arestas = [
    (0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1),
]

dist = floyd_warshall(n, arestas)
for linha in dist:
    print(linha)

# Detectando ciclo negativo: se dist[i][i] ficar negativo após o algoritmo, existe um ciclo negativo alcançável a partir de i
def floyd_warshall_ciclo_neg(n, arestas):
    dist = floyd_warshall(n, arestas)

    tem_ciclo_negativo = any(dist[i][i] < 0 for i in range(n))
    return dist, tem_ciclo_negativo

arestas_com_ciclo = [
    (0, 1, 1), (1, 2, -1), (2, 0, -1),
]

dist, ciclo_neg = floyd_warshall_ciclo_neg(3, arestas_com_ciclo)
print(ciclo_neg)

# Reconstruindo o caminho entre um par específico de vértices
def floyd_warshall_com_caminho(n, arestas):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    prox = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        prox[i][i] = i

    for u, v, peso in arestas:
        if peso < dist[u][v]:
            dist[u][v] = peso
            prox[u][v] = v

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prox[i][j] = prox[i][k]

    return dist, prox

def reconstruir_caminho(prox, u, v):
    if prox[u][v] is None:
        return [] # não há caminho entre u e v

    caminho = [u]
    while u != v:
        u = prox[u][v]
        caminho.append(u)
    return caminho

dist, prox = floyd_warshall_com_caminho(n, arestas)
print(reconstruir_caminho(prox, 0, 3))