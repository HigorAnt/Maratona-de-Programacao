# Verifica a existência de caminho/ciclo euleriano e, se houver caminho, retorna a sequência de vértices percorrida (via Hierholzer).
def caminho_euleriano(n, arestas):
    m = len(arestas)
    grau = [0] * n
    adjacencia = [[] for _ in range(n)]

    for i, (u, v) in enumerate(arestas):
        grau[u] += 1
        grau[v] += 1
        adjacencia[u].append((v, i))
        adjacencia[v].append((u, i))

    primeiro_vertice_com_aresta = -1
    for v in range(n):
        if grau[v] > 0:
            primeiro_vertice_com_aresta = v
            break
    if primeiro_vertice_com_aresta == -1:
        return None

    visitado = [False] * n
    visitado[primeiro_vertice_com_aresta] = True
    pilha_dfs = [primeiro_vertice_com_aresta]
    total_visitados = 1

    while pilha_dfs:
        u = pilha_dfs.pop()
        for v, _ in adjacencia[u]:
            if not visitado[v]:
                visitado[v] = True
                total_visitados += 1
                pilha_dfs.append(v)

    total_com_aresta = sum(1 for v in range(n) if grau[v] > 0)
    if total_visitados != total_com_aresta:
        return None  # desconexo

    impares = 0
    vertice_impar = -1
    for v in range(n):
        if grau[v] % 2 == 1:
            impares += 1
            if vertice_impar == -1:
                vertice_impar = v
            if impares > 2:
                return None

    if impares == 0:
        return "ciclo"
    if impares != 2:
        return None

    # Caso de CAMINHO: constrói via Hierholzer, começando no vértice de grau ímpar
    usada = [False] * m
    ponteiro = [0] * n
    pilha = [vertice_impar]
    caminho = []

    while pilha:
        u = pilha[-1]
        if ponteiro[u] < len(adjacencia[u]):
            v, idx_aresta = adjacencia[u][ponteiro[u]]
            ponteiro[u] += 1
            if not usada[idx_aresta]:
                usada[idx_aresta] = True
                pilha.append(v)
        else:
            caminho.append(pilha.pop())

    caminho.reverse()
    return caminho

def main():
    print(caminho_euleriano(3, [(0, 1), (1, 2), (2, 0)]))
    print(caminho_euleriano(4, [(0, 1), (1, 2), (2, 3)]))
    print(caminho_euleriano(4, [(0, 1), (2, 3)]))
    print(caminho_euleriano(4, [(0, 1), (0, 2), (0, 3)]))
    print(caminho_euleriano(4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]))

if __name__ == "__main__":
    main()