from collections import deque, defaultdict

# BFS (Busca em Largura): percorre o grafo "em camadas", visitando primeiro todos os vizinhos
# diretos de um vértice, depois os vizinhos dos vizinhos, e assim por diante
# Utiliza uma FILA (deque), garantindo que os vértices sejam processados na ordem em que foram descobertos

def bfs(grafo, inicio):
    visitados = {inicio}
    fila = deque([inicio])
    ordem_visita = []

    while fila:
        atual = fila.popleft()  
        ordem_visita.append(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho) 
                fila.append(vizinho)

    return ordem_visita

grafo_exemplo = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
}
print("Busca:", bfs(grafo_exemplo, 0))

# BFS para encontrar a MENOR DISTÂNCIA (em número de arestas) de um vértice origem até todos os outros
# Funciona apenas em grafos NÃO PONDERADOS (ou onde todas as arestas têm o mesmo peso)
def bfs_distancias(grafo, inicio):
    distancias = {inicio: 0}
    fila = deque([inicio])

    while fila:
        atual = fila.popleft()

        for vizinho in grafo[atual]:
            if vizinho not in distancias:
                distancias[vizinho] = distancias[atual] + 1
                fila.append(vizinho)

    return distancias

print("Quantidade de arestas para alcançar cada vértice:", bfs_distancias(grafo_exemplo, 0)) 

# BFS reconstruindo o CAMINHO percorrido até um vértice de destino específico
def bfs_caminho(grafo, inicio, destino):
    visitados = {inicio}
    fila = deque([inicio])
    predecessor = {inicio: None}  # guarda de qual vértice cada um foi alcançado

    while fila:
        atual = fila.popleft()

        if atual == destino:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                predecessor[vizinho] = atual
                fila.append(vizinho)

    if destino not in predecessor:
        return None  # destino inalcançável a partir da origem

    # Reconstrói o caminho "andando para trás", do destino até a origem
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessor[atual]

    return caminho[::-1]  # inverte para exibir da origem até o destino

print("Caminho:", bfs_caminho(grafo_exemplo, 0, 4)) 

# BFS em um grafo com MÚLTIPLAS COMPONENTES CONEXAS: é necessário rodar o BFS a partir de
# cada vértice ainda não visitado, para garantir que todas as componentes sejam alcançadas
def bfs_todas_componentes(grafo, vertices):
    visitados_global = set()
    componentes = []

    for vertice in vertices:
        if vertice not in visitados_global:
            visitados = {vertice}
            fila = deque([vertice])
            componente_atual = []

            while fila:
                atual = fila.popleft()
                componente_atual.append(atual)
                visitados_global.add(atual)

                for vizinho in grafo[atual]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)

            componentes.append(componente_atual)

    return componentes

grafo_desconexo = defaultdict(list, {
    0: [1], 1: [0],
    2: [3], 3: [2],
    4: []
})
print("Busca em grafo desconexo:", bfs_todas_componentes(grafo_desconexo, [0, 1, 2, 3, 4]))