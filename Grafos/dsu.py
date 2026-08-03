class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n)) # cada elemento começa sendo seu próprio representante
        self.rank = [0] * n # usado para manter a árvore rasa na união por rank

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x]) # compressão de caminho
        return self.pai[x]

    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x == raiz_y:
            return False # já estavam no mesmo conjunto

        # União por rank: pendura a árvore menor embaixo da maior
        if self.rank[raiz_x] < self.rank[raiz_y]:
            raiz_x, raiz_y = raiz_y, raiz_x
        self.pai[raiz_y] = raiz_x
        if self.rank[raiz_x] == self.rank[raiz_y]:
            self.rank[raiz_x] += 1

        return True

    def conectados(self, x, y):
        return self.find(x) == self.find(y)

# Aplicação: verificar se um grafo tem ciclo (não direcionado)
def tem_ciclo(n, arestas):
    uf = UnionFind(n)

    for u, v in arestas:
        if not uf.union(u, v):
            return True   # u e v já estavam conectados -> formar essa aresta cria um ciclo

    return False

# Aplicação: contar o número de componentes conexas
def contar_componentes(n, arestas):
    uf = UnionFind(n)

    for u, v in arestas:
        uf.union(u, v)

    return len({uf.find(i) for i in range(n)})

def main():
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print("Mesmo conjunto?", uf.conectados(0, 2))
    print("Mesmo conjunto?", uf.conectados(0, 3))
    print("Mesmo conjunto?", uf.find(0) == uf.find(1) == uf.find(2))

    arestas = [(0, 1), (1, 2), (2, 0)]
    print("Ciclíco?", tem_ciclo(3, arestas))

    arestas_sem_ciclo = [(0, 1), (1, 2), (2, 3)]
    print("Ciclíco?", tem_ciclo(4, arestas_sem_ciclo))

    print("Quantidade de componentes:", contar_componentes(6, [(0, 1), (1, 2), (3, 4)]))

if __name__ == "__main__":
    main()