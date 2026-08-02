from dsu import UnionFind

def kruskal(n, arestas_com_peso):
    uf = UnionFind(n)
    arestas_ordenadas = sorted(arestas_com_peso, key=lambda e: e[2])
    mst = []
    peso_total = 0

    for u, v, peso in arestas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            peso_total += peso

    return mst, peso_total

arestas_com_peso = [(0,1,4), (0,2,1), (1,2,2), (1,3,5), (2,3,8), (3,4,3)]
mst, peso = kruskal(5, arestas_com_peso)
print("MST (peso, arestas):", mst) 
print("Peso total:", peso)

# Detectando grafo desconexo: se a MST tiver menos de n-1 arestas, nem todos os vértices puderam ser conectados
def kruskal_verifica_conexo(n, arestas):
    mst, custo = kruskal(n, arestas)
    if len(mst) != n - 1:
        return None   # grafo desconexo, não existe árvore geradora
    return custo, mst

arestas_desconexas = [(1, 0, 1), (2, 3, 2)]
arestas_conexas = [(1, 0, 1), (2, 3, 2), (1, 2, 3)]
print("Conexo?", kruskal_verifica_conexo(4, arestas_desconexas))
print("Conexo?", kruskal_verifica_conexo(4, arestas_conexas))