from collections import deque

valor = 6
# Cria uma deque a partir de uma lista (ou qualquer iterável)
minha_deque = deque([1, 2, 3, 4, 5])
print(minha_deque)

# Criação a partir de entrada do usuário
entrada = input("Digite números separados por espaço: ")
minha_deque = deque(map(int, entrada.split()))
print("Deque recebida:", minha_deque)

# Deque vazia
deque_vazia = deque()

# append(x): adiciona x ao final da deque, em tempo O(1)
minha_deque.append(valor)
print(f"Deque com {valor} inserido:", minha_deque)

# appendleft(x): adiciona x ao início da deque, também em tempo O(1) (diferente de uma lista, onde inserir no início custa O(n))
minha_deque.appendleft(valor)
print(f"Deque com {valor} inserido:", minha_deque)

# pop(): remove e retorna o último elemento, em tempo O(1)
ultimo = minha_deque.pop()
print(f"Elemento removido: {ultimo}; deque: {minha_deque}")

# popleft(): remove e retorna o primeiro elemento, em tempo O(1) (essencial para implementar filas/BFS)
primeiro = minha_deque.popleft()
print(f"Elemento removido: {primeiro}; deque: {minha_deque}")

# extend(iteravel): adiciona múltiplos elementos ao final
minha_deque.extend([7, 8, 9])
print("Deque com [7, 8, 9] inseridos:", minha_deque)

# extendleft(iteravel): adiciona múltiplos elementos ao início (atenção: a ordem final é invertida, pois cada elemento é inserido individualmente na frente)
minha_deque.extendleft([-1, -2])
print("Deque com [-1, -2] inseridos:", minha_deque) 

# Acesso por índice funciona como em uma lista, mas é O(n) no meio da deque (só as pontas são O(1))
print("Primeiro elemento:", minha_deque[0])
print("Último elemento:", minha_deque[-1])

# len(): retorna a quantidade de elementos
print("Tamanho da deque:", len(minha_deque))

# in / not in: verifica presença de um elemento
print("5 está na deque?", 5 in minha_deque)

# rotate(n): move os elementos n posições para a direita (n negativo move para a esquerda)
minha_deque.rotate(1)
print("Deque rotacionada em 1:", minha_deque) 

minha_deque.rotate(-2)
print("Deque rotacionada em -2:", minha_deque)  # desfaz a rotação anterior

# clear(): remove todos os elementos
copia = minha_deque.copy()
copia.clear()
print("Cópia vazia:", copia)

# count(x): conta quantas vezes x aparece na deque
print("Ocorrências de 7 na deque:", minha_deque.count(7))

# remove(x): remove a primeira ocorrência de x. Gera ValueError se x não existir
minha_deque.remove(7)
print("Deque:", minha_deque)

# deque(maxlen=n): cria uma deque com tamanho máximo fixo; ao exceder, remove automaticamente o elemento da outra ponta
janela = deque(maxlen=3)
for valor in [1, 2, 3, 4, 5]:
    janela.append(valor)
    print(janela)  # mantém sempre os 3 últimos valores (útil para janela deslizante)

# Exemplo prático: implementando uma fila (FIFO) para BFS
fila = deque()
fila.append("A")
fila.append("B")
fila.append("C")

while fila:
    atual = fila.popleft()  # remove sempre o primeiro que entrou
    print("Processando:", atual)