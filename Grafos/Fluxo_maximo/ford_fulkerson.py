import sys
from collections import defaultdict

# Representa um grafo direcionado com capacidades, para cálculo de fluxo máximo
# Usa lista de adjacência com dicionário de capacidades residuais, incluindo
# arestas reversas (inicialmente com capacidade 0) para permitir o "desfazer" de fluxo já enviado
class GrafoFluxo:
    def __init__(self):
        self.capacidade = defaultdict(dict)
        self.vertices = set()

    def adicionar_aresta(self, u, v, cap):
        #Adiciona aresta u -> v com capacidade 'cap'. Cria a reversa com capacidade 
        self.capacidade[u][v] = self.capacidade[u].get(v, 0) + cap  # lida com arestas paralelas
        self.capacidade[v][u] = self.capacidade[v].get(u, 0)  # garante a reversa, sem sobrescrever
        self.vertices.add(u)
        self.vertices.add(v)

    # Busca em profundidade iterativa por um caminho de aumento na rede residual
    # Retorna o caminho (lista de vértices) até o sumidouro, ou None se não existir.
    def _busca_caminho_aumento(self, fonte, sumidouro):
        visitados = {fonte}
        pai = {fonte: None}
        pilha = [fonte]

        while pilha:
            u = pilha.pop()

            if u == sumidouro:
                caminho = []
                atual = sumidouro
                while atual is not None:
                    caminho.append(atual)
                    atual = pai[atual]
                caminho.reverse()
                return caminho

            # .get(u, {}) evita criar uma entrada vazia no defaultdict para vértices sem arestas de saída
            for vizinho, cap_residual in self.capacidade.get(u, {}).items():
                if vizinho not in visitados and cap_residual > 0:
                    visitados.add(vizinho)
                    pai[vizinho] = u
                    pilha.append(vizinho)

        return None  # sumidouro não foi alcançado: não há caminho de aumento

    # Calcula o fluxo máximo de 'fonte' até 'sumidouro' usando Ford-Fulkerson
    # com busca em profundidade iterativa para encontrar caminhos de aumento
    # Tempo: O(E * f_max). Espaço: O(V + E).
    def fluxo_maximo(self, fonte, sumidouro):
        fluxo_total = 0

        while True:
            caminho = self._busca_caminho_aumento(fonte, sumidouro)
            if caminho is None:
                break

            gargalo = min(
                self.capacidade[caminho[i]][caminho[i + 1]]
                for i in range(len(caminho) - 1)
            )

            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i + 1]
                self.capacidade[u][v] -= gargalo
                self.capacidade[v][u] += gargalo

            fluxo_total += gargalo

        return fluxo_total

def main():
    grafo = GrafoFluxo()
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