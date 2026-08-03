import sys
from collections import defaultdict, deque

class GrafoFluxoEdmondsKarp:
    def __init__(self):
        self.capacidade = defaultdict(lambda: defaultdict(int))
        self.vertices = set()

    def adicionar_aresta(self, u, v, cap):
        # Adiciona aresta u -> v com capacidade 'cap'. Cria a reversa com capacidade 0
        self.capacidade[u][v] += cap  # += para lidar com arestas paralelas (multigrafo)
        self.capacidade[v][u] += 0
        self.vertices.add(u)
        self.vertices.add(v)

    # Busca em largura por um caminho de aumento na rede residual. Retorna o dicionário de predecessores, ou None se não há caminho
    def _bfs_caminho_aumento(self, fonte, sumidouro):
        visitados = {fonte}
        predecessor = {}
        fila = deque([fonte])

        while fila:
            atual = fila.popleft()
            if atual == sumidouro:
                return predecessor

            for vizinho, cap_residual in self.capacidade[atual].items():
                if vizinho not in visitados and cap_residual > 0:
                    visitados.add(vizinho)
                    predecessor[vizinho] = atual
                    fila.append(vizinho)

        return None if sumidouro not in visitados else predecessor

    # Calcula o fluxo máximo de 'fonte' até 'sumidouro' usando Edmonds-Karp
    def fluxo_maximo(self, fonte, sumidouro):
        fluxo_total = 0

        while True:
            predecessor = self._bfs_caminho_aumento(fonte, sumidouro)

            if predecessor is None:
                break  # Não há mais caminho de aumento: fluxo máximo atingido

            # Reconstrói o caminho a partir dos predecessores (sumidouro -> fonte)
            caminho = []
            atual = sumidouro
            while atual != fonte:
                anterior = predecessor[atual]
                caminho.append((anterior, atual))
                atual = anterior
            caminho.reverse()

            # Encontra o gargalo (menor capacidade residual no caminho)
            gargalo = min(self.capacidade[u][v] for u, v in caminho)

            # Atualiza as capacidades residuais (direta e reversa) ao longo do caminho
            for u, v in caminho:
                self.capacidade[u][v] -= gargalo
                self.capacidade[v][u] += gargalo

            fluxo_total += gargalo

        return fluxo_total

def main():
    grafo = GrafoFluxoEdmondsKarp()

    arestas = [
        (0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12),
        (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)
    ]

    for u, v, cap in arestas:
        grafo.adicionar_aresta(u, v, cap)
    fonte, sumidouro = 0, 5

    print("Fluxo máximo:", grafo.fluxo_maximo(fonte, sumidouro))

if __name__ == "__main__":
    main()