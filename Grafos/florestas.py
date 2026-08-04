from collections import defaultdict, deque
from dsu import UnionFind

def contar_floresta(n, arestas):
    uf = UnionFind(n)

    for u, v in arestas:
        uf.union(u, v) # agrupa em componentes, ignorando se a aresta é direcionada

    componentes = defaultdict(list)
    for v in range(n):
        componentes[uf.find(v)].append(v)

    arestas_por_componente = defaultdict(int)
    for u, v in arestas:
        arestas_por_componente[uf.find(u)] += 1

    arvores = []
    nao_arvores = []

    for raiz, vertices_comp in componentes.items():
        qtd_arestas = arestas_por_componente[raiz]
        qtd_vertices = len(vertices_comp)

        if qtd_arestas == qtd_vertices - 1:
            arvores.append(vertices_comp)
        else:
            nao_arvores.append(vertices_comp)

    return len(componentes), arvores, nao_arvores

# Verificação de arborescência por componente (respeita direção)
def contar_floresta_arborescencia(n, arestas):
    uf = UnionFind(n)
    for u, v in arestas:
        uf.union(u, v)

    componentes = defaultdict(list)
    for v in range(n):
        componentes[uf.find(v)].append(v)

    grafo = defaultdict(list)
    grau_entrada = [0] * n
    for u, v in arestas:
        grafo[u].append(v)
        grau_entrada[v] += 1

    arborescencias = []
    nao_arborescencias = []

    for raiz, vertices_comp in componentes.items():
        raizes_locais = [v for v in vertices_comp if grau_entrada[v] == 0]
        valido = len(raizes_locais) == 1 and all(grau_entrada[v] <= 1 for v in vertices_comp)

        if valido:
            raiz_local = raizes_locais[0]
            visitados = {raiz_local}
            fila = deque([raiz_local])

            while fila:
                atual = fila.popleft()
                for vizinho in grafo[atual]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)

            valido = len(visitados) == len(vertices_comp)

        if valido:
            arborescencias.append(vertices_comp)
        else:
            nao_arborescencias.append(vertices_comp)

    return len(componentes), arborescencias, nao_arborescencias

# Grafo de exemplo com 4 componentes:
# {0,1,2}: duas arestas apontando PARA o vértice 1 -> árvore geral, mas não arborescência (2 raízes)
# {3,4,5}: cadeia 3 -> 4 -> 5 -> árvore geral e arborescência válida (raiz única: 3)
# {6,7,8}: ciclo 6 -> 7 -> 8 -> 6 -> nem árvore, nem arborescência
# {9}: vértice isolado -> árvore geral trivial e arborescência trivial
n = 10
arestas = [
    (0, 1), (2, 1), (3, 4), (4, 5),
    (6, 7), (7, 8), (8, 6)
]

total, arvores, nao_arvores = contar_floresta(n, arestas)
print(f"Componentes: {total}")
print(f"Árvores ({len(arvores)}): {arvores}")
print(f"Não são árvores ({len(nao_arvores)}): {nao_arvores}")

total, arborescencias, nao_arborescencias = contar_floresta_arborescencia(n, arestas)
print(f"Componentes: {total}")
print(f"Arborescências ({len(arborescencias)}): {arborescencias}")
print(f"Não são arborescências ({len(nao_arborescencias)}): {nao_arborescencias}")