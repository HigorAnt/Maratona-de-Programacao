from collections import defaultdict, deque
# Abordagem 1: baseada em DFS 
# A ideia é: ao finalizar completamente a exploração de um vértice (todos os seus vizinhos já visitados),
# ele é inserido no INÍCIO do resultado - o que equivale a inverter a ordem de finalização do DFS
def ordenacao_topologica_dfs(grafo, vertices):
    visitados = set()
    pilha_resultado = []

    def dfs(atual):
        visitados.add(atual)
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                dfs(vizinho)
        pilha_resultado.append(atual)  # adiciona APÓS explorar todos os vizinhos (pós-ordem)

    for vertice in vertices:
        if vertice not in visitados:
            dfs(vertice)

    return pilha_resultado[::-1]  # inverte, pois o último a finalizar deve vir primeiro

grafo_dag = defaultdict(list, {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
})
vertices_dag = [5, 4, 2, 3, 1, 0]

print("Ordenação topológica:", ordenacao_topologica_dfs(grafo_dag, vertices_dag))

# Abordagem 2: Algoritmo de Kahn (baseada em BFS e grau de entrada) 
# A ideia é: processar primeiro os vértices que não dependem de nenhum outro (grau de entrada 0),
# removendo-os do grafo e atualizando o grau de entrada dos seus vizinhos, repetindo o processo
def ordenacao_topologica_kahn(grafo, vertices):
    grau_entrada = {v: 0 for v in vertices}

    for v in vertices:
        for vizinho in grafo[v]:
            grau_entrada[vizinho] += 1

    # Inicia a fila com todos os vértices que não possuem nenhuma dependência (grau de entrada 0)
    fila = deque([v for v in vertices if grau_entrada[v] == 0])
    resultado = []

    while fila:
        atual = fila.popleft()
        resultado.append(atual)

        for vizinho in grafo[atual]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    # Se nem todos os vértices foram processados, o grafo possui um CICLO (não é um DAG válido)
    if len(resultado) != len(vertices):
        return None

    return resultado

print("Ordenação topológica:", ordenacao_topologica_kahn(grafo_dag, vertices_dag)) 

# Verificando com um grafo que POSSUI CICLO: a ordenação topológica não deve ser possível
grafo_com_ciclo = defaultdict(list, {0: [1], 1: [2], 2: [0]})
print(ordenacao_topologica_kahn(grafo_com_ciclo, [0, 1, 2]))

# Exemplo prático: ordenar disciplinas de um curso respeitando pré-requisitos
prerequisitos = defaultdict(list, {
    "Cálculo 1": ["Cálculo 2"],
    "Cálculo 2": ["Cálculo 3"],
    "Cálculo 3": [],
    "Programação 1": ["Programação 2", "Estrutura de Dados"],
    "Programação 2": [],
    "Estrutura de Dados": ["Algoritmos"],
    "Algoritmos": []
})
disciplinas = ["Cálculo 1", "Cálculo 2", "Cálculo 3", "Programação 1", "Programação 2", "Estrutura de Dados", "Algoritmos"]

ordem_cursando = ordenacao_topologica_kahn(prerequisitos, disciplinas)
print("Ordem a ser cursada:", ordem_cursando)