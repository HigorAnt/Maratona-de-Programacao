from collections import deque

def maximo_janela_deslizante(array, k):
    # A deque armazena ÍNDICES (não valores), mantidos em ordem decrescente de valor
    # Ou seja, o índice do maior valor da janela atual está sempre na frente da deque
    janela = deque()
    resultado = []

    for i in range(len(array)):
        # Remove da frente os índices que já saíram da janela atual (fora do intervalo [i-k+1, i])
        if janela and janela[0] <= i - k:
            janela.popleft()

        # Remove do final todos os índices cujo valor é menor ou igual ao elemento atual,
        # pois eles nunca mais poderão ser o máximo de nenhuma janela futura (o atual é melhor e mais recente)
        while janela and array[janela[-1]] <= array[i]:
            janela.pop()

        # Adiciona o índice atual ao final da deque
        janela.append(i)

        # A partir do momento em que a primeira janela completa se forma (i >= k - 1),
        # o índice na frente da deque é sempre o máximo da janela atual
        if i >= k - 1:
            resultado.append(array[janela[0]])

    return resultado

array_exemplo = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print("Maior valor de cada janela:", maximo_janela_deslizante(array_exemplo, k))
# Janelas: [1,3,-1]->3, [3,-1,-3]->3, [-1,-3,5]->5, [-3,5,3]->5, [5,3,6]->6, [3,6,7]->7

# Variação: mínimo da janela deslizante (mesma lógica, invertendo a condição de remoção da deque)
def minimo_janela_deslizante(array, k):
    janela = deque()
    resultado = []

    for i in range(len(array)):
        if janela and janela[0] <= i - k:
            janela.popleft()

        # Agora remove os índices cujo valor é MAIOR ou igual ao atual, mantendo a deque em ordem crescente
        while janela and array[janela[-1]] >= array[i]:
            janela.pop()

        janela.append(i)

        if i >= k - 1:
            resultado.append(array[janela[0]])

    return resultado

print(minimo_janela_deslizante(array_exemplo, k))
# Janelas: [1,3,-1]->-1, [3,-1,-3]->-3, [-1,-3,5]->-3, [-3,5,3]->-3, [5,3,6]->3, [3,6,7]->3