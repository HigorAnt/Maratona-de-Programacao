from itertools import count

# itertools.count(inicio, passo): gerador infinito de números, útil como contador incremental (ex: desempate em heapq)
contador = count(1)
print(next(contador), next(contador), next(contador))

# se dois itens tiverem a mesma prioridade (mesmo primeiro valor da tupla), 
# o heap tenta comparar o segundo elemento pra desempatar — e se esse segundo elemento não for comparável 
# (ex.: strings vs objetos, ou objetos sem __lt__), o programa quebra com erro. 
# O contador garante que nunca existam dois itens com os dois primeiros valores iguais, evitando esse erro.
import heapq

fila = []
contador = count()
heapq.heappush(fila, (5, next(contador), "tarefa_B"))
heapq.heappush(fila, (5, next(contador), "tarefa_A"))
heapq.heappush(fila, (1, next(contador), "tarefa_C"))
print([heapq.heappop(fila) for _ in range(3)])

# Útil pra qualquer problema que envolva rotação/alternância cíclica 
# (ex.: distribuir tarefas em turnos, percorrer direções em ordem fixa)
from itertools import cycle
ciclo = cycle(["A", "B", "C"])
print([next(ciclo) for _ in range(7)])

# Quando é preciso percorrer várias listas/ranges como se fossem uma sequência só, sem o custo de criar uma lista concatenada
from itertools import chain
a, b, c = [1, 2, 3], [4, 5], [6]
print(list(chain(a, b, c)))

# agrupa (conta) elementos consecutivos, não totais, como o Counter
from itertools import groupby
dados = "aabaa"
grupos = [(chave, len(list(grupo))) for chave, grupo in groupby(dados)]
print(grupos)