from itertools import permutations

# Busca por força bruta um CICLO hamiltoniano: uma rota que visita todos os vértices exatamente uma vez e retorna ao vértice inicial.
def ciclo_hamiltoniano(n, adjacencia):
    if n <= 1:
        return None

    for permutacao in permutations(range(1, n)):
        rota = (0,) + permutacao

        valido = all(rota[i + 1] in adjacencia[rota[i]] for i in range(n - 1))
        if valido and rota[0] in adjacencia[rota[-1]]:
            return list(rota) + [rota[0]]

    return None

def caminho_hamiltoniano(n, adjacencia):
    if n == 0:
        return None

    for permutacao in permutations(range(n)):
        valido = all(permutacao[i + 1] in adjacencia[permutacao[i]] for i in range(n - 1))
        if valido:
            return list(permutacao)

    return None

def main():
    # Grafo completo K4: qualquer ordem funciona, tem ciclo e caminho
    adjacencia_completo = [{1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}]
    print(ciclo_hamiltoniano(4, adjacencia_completo))
    print(caminho_hamiltoniano(4, adjacencia_completo))

    # Caminho simples 0-1-2-3 (sem aresta de volta 3-0): tem CAMINHO, mas não CICLO
    adjacencia_caminho = [{1}, {0, 2}, {1, 3}, {2}]
    print(ciclo_hamiltoniano(4, adjacencia_caminho))
    print(caminho_hamiltoniano(4, adjacencia_caminho))

    # Grafo estrela: não tem nem caminho nem ciclo hamiltoniano
    adjacencia_estrela = [{1, 2, 3}, {0}, {0}, {0}]
    print(ciclo_hamiltoniano(4, adjacencia_estrela))
    print(caminho_hamiltoniano(4, adjacencia_estrela))

    # Grafo desconexo: nem caminho nem ciclo
    adjacencia_desconexo = [{1}, {0}, {3}, {2}]
    print(ciclo_hamiltoniano(4, adjacencia_desconexo))
    print(caminho_hamiltoniano(4, adjacencia_desconexo))

if __name__ == "__main__":
    main()