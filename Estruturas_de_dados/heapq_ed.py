import heapq

# Cria um heap a partir de uma lista comum, transformando-a "in place" em um min-heap
numeros = [5, 2, 8, 1, 9, 3]
heapq.heapify(numeros)
print("Heap:", numeros)  # a lista agora respeita a propriedade de heap (menor elemento sempre no índice 0)

# heappush(heap, x): insere x mantendo a propriedade de min-heap, em tempo O(log n)
heapq.heappush(numeros, 0)
print("Heap:", numeros)

# heappop(heap): remove e retorna o MENOR elemento do heap, em tempo O(log n)
menor = heapq.heappop(numeros)
print(f"Menor elemento: {menor}. Heap: {numeros}")

# O menor elemento sempre pode ser consultado (sem remover) acessando o índice 0
print("Menor elemento:", numeros[0])

# Criação a partir de entrada do usuário
entrada = input("Digite números separados por espaço: ")
heap_entrada = list(map(int, entrada.split()))
heapq.heapify(heap_entrada)
print("Heap inserido:", heap_entrada)

# heappushpop(heap, x): insere x e já remove/retorna o menor elemento, mais eficiente que push + pop separados
resultado = heapq.heappushpop(numeros, 4)
print(f"Remoção: {resultado}. Inserção: {numeros}")

# heapreplace(heap, x): remove/retorna o menor elemento e SÓ DEPOIS insere x (equivalente a pop + push, também mais eficiente que separado)
resultado2 = heapq.heapreplace(numeros, 100)
print(resultado2, numeros)

# nlargest(n, iteravel): retorna os n maiores elementos, já ordenados do maior para o menor
print("3 maiores elementos:", heapq.nlargest(3, numeros))

# nsmallest(n, iteravel): retorna os n menores elementos, já ordenados do menor para o maior
print("3 menores elementos:", heapq.nsmallest(3, numeros))

# Python só tem min-heap nativamente. Para simular um max-heap, inverte-se o sinal dos valores ao inserir e ao remover
max_heap = []
valores = [5, 2, 8, 1, 9]
for v in valores:
    heapq.heappush(max_heap, -v)  # insere o valor negativo

maior = -heapq.heappop(max_heap)  # remove o menor negativo (equivale ao maior valor real) e desfaz o sinal
print("Menor negativo (absoluto):", maior) 

# Heap de tuplas: por padrão, a comparação é feita elemento a elemento da tupla (o primeiro item decide a prioridade)
tarefas = []
heapq.heappush(tarefas, (2, "lavar louça"))
heapq.heappush(tarefas, (1, "estudar para a maratona"))
heapq.heappush(tarefas, (3, "dormir"))

# Ao remover, vem sempre a tupla com o menor primeiro elemento (menor prioridade numérica = mais urgente)
while tarefas:
    prioridade, tarefa = heapq.heappop(tarefas)
    print(prioridade, tarefa)

# Cuidado: se o primeiro elemento da tupla empatar, o Python tenta comparar o segundo elemento.
# Se o segundo elemento não for comparável (ex: dicionários), gera erro. Uma solução comum é
# adicionar um índice/contador único como segundo item da tupla para desempatar sem comparar o restante
import itertools
contador = itertools.count()  # gerador de números incrementais únicos

fila_prioridade = []
heapq.heappush(fila_prioridade, (5, next(contador), "tarefa A"))
heapq.heappush(fila_prioridade, (5, next(contador), "tarefa B"))
print(heapq.heappop(fila_prioridade))  # desempata pela ordem de inserção, não pelo texto