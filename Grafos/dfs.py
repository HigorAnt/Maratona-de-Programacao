from collections import defaultdict
import sys

sys.setrecursionlimit(10000)  # aumenta o limite de recursão, importante para grafos com muitos vértices

# DFS: percorre o grafo indo o mais "fundo" possível por um caminho
# antes de retroceder (backtrack) e explorar outros ramos - naturalmente implementado com recursão

def dfs_recursivo(grafo, atual, visitados=None, ordem_visita=None):
    if visitados is None:
        visitados = set()
        ordem_visita = []

    visitados.add(atual)
    ordem_visita.append(atual)

    for vizinho in grafo[atual]:
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados, ordem_visita)

    return ordem_visita

grafo_exemplo = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
}
print("Resultado da busca:", dfs_recursivo(grafo_exemplo, 0))

# Versão ITERATIVA do DFS, usando uma pilha explícita (lista) ao invés de recursão
# Evita o risco de estourar o limite de recursão em grafos muito profundos
def dfs_iterativo(grafo, inicio):
    visitados = set()
    pilha = [inicio]
    ordem_visita = []

    while pilha:
        atual = pilha.pop()  # remove do TOPO da pilha (último a entrar, primeiro a sair)

        if atual not in visitados:
            visitados.add(atual)
            ordem_visita.append(atual)

            # adiciona os vizinhos em ordem REVERSA, para manter uma ordem de visita
            # mais parecida com a versão recursiva (opcional, apenas para consistência visual)
            for vizinho in reversed(grafo[atual]):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return ordem_visita

print(dfs_iterativo(grafo_exemplo, 0))  # [0, 1, 2, 3, 4]

# DFS para detectar CICLOS em um grafo NÃO DIRECIONADO
# Um ciclo existe se, ao visitar um vizinho já visitado, ele NÃO for o vértice de onde acabamos de vir (pai)
def tem_ciclo_nao_direcionado(grafo, vertices):
    visitados = set()

    def dfs_ciclo(atual, pai):
        visitados.add(atual)
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                if dfs_ciclo(vizinho, atual):
                    return True
            elif vizinho != pai:
                return True  # encontrou um vértice já visitado que NÃO é o pai - existe ciclo
        return False

    for vertice in vertices:
        if vertice not in visitados:
            if dfs_ciclo(vertice, None):
                return True

    return False

grafo_com_ciclo = defaultdict(list, {0: [1], 1: [0, 2], 2: [1, 0], 3: []}) 
grafo_sem_ciclo = defaultdict(list, {0: [1], 1: [0, 2], 2: [1], 3: []}) 

print("Possui ciclo?", tem_ciclo_nao_direcionado(grafo_com_ciclo, [0, 1, 2, 3])) 
print("Possui ciclo?", tem_ciclo_nao_direcionado(grafo_sem_ciclo, [0, 1, 2, 3]))  # False

# DFS para detectar CICLOS em um grafo DIRECIONADO
# Utiliza três estados: não visitado, "em processamento" (está na pilha de recursão atual),
# e "processado" (já finalizado). Um ciclo existe se encontrarmos um vizinho "em processamento"
def tem_ciclo_direcionado(grafo, vertices):
    NAO_VISITADO, EM_PROCESSAMENTO, PROCESSADO = 0, 1, 2
    estado = defaultdict(int)

    def dfs_ciclo(atual):
        estado[atual] = EM_PROCESSAMENTO

        for vizinho in grafo[atual]:
            if estado[vizinho] == EM_PROCESSAMENTO:
                return True  # encontrou um vértice que ainda está "no caminho atual" - ciclo!
            if estado[vizinho] == NAO_VISITADO:
                if dfs_ciclo(vizinho):
                    return True

        estado[atual] = PROCESSADO
        return False

    for vertice in vertices:
        if estado[vertice] == NAO_VISITADO:
            if dfs_ciclo(vertice):
                return True

    return False

grafo_dirigido_com_ciclo = defaultdict(list, {0: [1], 1: [2], 2: [0]})
grafo_dirigido_sem_ciclo = defaultdict(list, {0: [1], 1: [2], 2: []}) 

print("Possui ciclo?", tem_ciclo_direcionado(grafo_dirigido_com_ciclo, [0, 1, 2])) 
print("Possui ciclo?", tem_ciclo_direcionado(grafo_dirigido_sem_ciclo, [0, 1, 2])) 