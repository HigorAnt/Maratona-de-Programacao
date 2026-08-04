class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x == raiz_y:
            return False   # já conectados -> essa aresta fecharia um ciclo

        if self.rank[raiz_x] < self.rank[raiz_y]:
            raiz_x, raiz_y = raiz_y, raiz_x
        self.pai[raiz_y] = raiz_x
        if self.rank[raiz_x] == self.rank[raiz_y]:
            self.rank[raiz_x] += 1

        return True

# Utiliza a classe UnionFind e as funções __init__(), find() e union()
def arvore(n, arestas):
    uf = UnionFind(n)

    for u, v in arestas:
        if not uf.union(u, v):
            return False   # ciclo detectado, seja o grafo direcionado ou não

    # Depois de processar todas as arestas sem ciclo, o grafo só é árvore
    # se todos os vértices caíram em um único conjunto (grafo conexo)
    raizes = {uf.find(v) for v in range(n)}
    return len(raizes) == 1


# Árvore válida (não-direcionado)
print("Árvore:", arvore(4, [(0, 1), (1, 2), (2, 3)]))
# Árvore válida (mesmas arestas, mas "direcionadas" -> direção é ignorada)
print("Árvore:", arvore(4, [(0, 1), (2, 1), (2, 3)]))
# Ciclo -> não é árvore, independente da direção
print("Árvore:", arvore(3, [(0, 1), (1, 2), (2, 0)]))
# Desconexo (falta ligação entre {0,1} e {2,3}) -> não é árvore
print("Árvore:", arvore(4, [(0, 1), (2, 3)]))

# Verificação de arborescência
from collections import defaultdict, deque

def arborescencia(n, arestas):
    grau_entrada = [0] * n
    grafo = defaultdict(list)

    for u, v in arestas:
        grafo[u].append(v)
        grau_entrada[v] += 1

    raizes = [v for v in range(n) if grau_entrada[v] == 0]

    # Deve haver exatamente uma raiz, e todos os demais vértices
    # devem ter grau de entrada exatamente 1
    if len(raizes) != 1:
        return False
    if any(grau_entrada[v] > 1 for v in range(n)):
        return False

    # Verifica se todos os vértices são alcançáveis a partir da raiz
    raiz = raizes[0]
    visitados = {raiz}
    fila = deque([raiz])

    while fila:
        atual = fila.popleft()
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return len(visitados) == n

# Arborescência válida: raiz 0, cada nó tem exatamente um "pai"
print("Arborescência:", arborescencia(4, [(0, 1), (0, 2), (1, 3)]))
# Invertendo a aresta -> a raiz simplesmente muda de 0 para 1
# Continua sendo uma arborescência válida, só que enraizada em outro vértice
print("Arborescência:", arborescencia(4, [(1, 0), (0, 2), (1, 3)]))
# Vértice com duas arestas de entrada -> não é arborescência
print("Arborescência:", arborescencia(3, [(0, 1), (2, 1)]))
# Estrutura em árvore, mas sem raiz alcançando todo mundo (arestas "de baixo pra cima")
print("Arborescência:", arborescencia(3, [(1, 0), (2, 0)]))