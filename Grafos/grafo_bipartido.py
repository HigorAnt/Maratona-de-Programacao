from collections import deque

def bipartido(n, adjacencia):
    cor = [-1] * n   # -1 = não colorido, 0 e 1 são as duas cores

    for inicio in range(n):
        if cor[inicio] != -1:
            continue   # já visitado em uma busca anterior

        cor[inicio] = 0
        fila = deque([inicio])

        while fila:
            u = fila.popleft()

            for v in adjacencia[u]:
                if cor[v] == -1:
                    cor[v] = 1 - cor[u]   # colore com a cor oposta
                    fila.append(v)
                elif cor[v] == cor[u]:
                    return False   # vizinho com a mesma cor -> não é bipartido

    return True

# Grafo bipartido (ciclo par)
n = 4
adjacencia = [[1, 3], [0, 2], [1, 3], [0, 2]]
print("Bipartido:", bipartido(n, adjacencia)) 

# Grafo não bipartido (ciclo ímpar - triângulo)
n2 = 3
adjacencia2 = [[1, 2], [0, 2], [0, 1]]
print("Bipartido:", bipartido(n2, adjacencia2))

# Versão que também retorna a coloração encontrada
def bipartido_com_cores(n, adjacencia):
    cor = [-1] * n

    for inicio in range(n):
        if cor[inicio] != -1:
            continue

        cor[inicio] = 0
        fila = deque([inicio])

        while fila:
            u = fila.popleft()

            for v in adjacencia[u]:
                if cor[v] == -1:
                    cor[v] = 1 - cor[u]
                    fila.append(v)
                elif cor[v] == cor[u]:
                    return False, None

    grupo_a = [v for v in range(n) if cor[v] == 0]
    grupo_b = [v for v in range(n) if cor[v] == 1]
    return True, (grupo_a, grupo_b)


bip, grupos = bipartido_com_cores(n, adjacencia)
print(f"Bipartido: {bip}. Grupos: {grupos}")

# Cuidado: grafo desconexo — o laço externo "for inicio in range(n)" garante que todos os componentes sejam verificados, não só o primeiro
n3 = 6
# componente {0,1} + {2,3,5} + {4}
adjacencia3 = [[1], [0], [3, 5], [2], [], [2]]   
print("Bipartido:", bipartido(n3, adjacencia3))