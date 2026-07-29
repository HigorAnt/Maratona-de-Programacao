import sys

# O Python tem um limite padrão de profundidade de recursão (geralmente 1000 chamadas)
# Em problemas com recursão profunda (árvores grandes, grafos com muitos vértices), isso pode gerar RecursionError
# Por isso, é comum aumentar esse limite logo no início do código
sys.setrecursionlimit(10 ** 6)

# Estrutura básica de uma função recursiva: precisa de um CASO BASE (condição de parada)
# e um CASO RECURSIVO (a função chamando a si mesma com uma entrada "menor", se aproximando do caso base)
def fatorial(n):
    if n == 0 or n == 1:  # caso base: evita chamadas infinitas
        return 1
    return n * fatorial(n - 1)  # caso recursivo: reduz o problema a uma instância menor

print("5! =", fatorial(5))

# Fibonacci recursivo SEM otimização: mostra o problema clássico de recomputação
# Cada chamada gera duas outras chamadas, recalculando os mesmos valores repetidamente
# Complexidade exponencial O(2^n) - inviável para n grande
def fibonacci_recursivo(n):
    if n <= 1:  # caso base
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)  # duas chamadas recursivas

print("Fibonacci 10:", fibonacci_recursivo(10))

# Somando os elementos de uma lista recursivamente (recursão não se aplica só a números isolados)
def soma_recursiva(lista):
    if len(lista) == 0:  # lista vazia soma 0
        return 0
    return lista[0] + soma_recursiva(lista[1:])  # soma o primeiro elemento + a soma recursiva do restante

print("Soma da lista:", soma_recursiva([1, 2, 3, 4, 5]))

# Busca binária implementada de forma recursiva
def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio > fim:  # intervalo vazio, elemento não encontrado
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        # chama recursivamente apenas na metade direita
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)
    else:
        # chama recursivamente apenas na metade esquerda
        return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)

lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Índice do elemento 23:", busca_binaria_recursiva(lista_ordenada, 23, 0, len(lista_ordenada) - 1))

# Recursão de cauda (tail recursion): quando a chamada recursiva é a ÚLTIMA operação da função
# Python NÃO otimiza esse tipo de recursão (diferente de outras linguagens), então ainda consome uma chamada de pilha por vez
def fatorial_cauda(n, acumulador=1):
    if n == 0 or n == 1:
        return acumulador
    return fatorial_cauda(n - 1, acumulador * n)  # a chamada recursiva é a última coisa executada

print("5! =", fatorial_cauda(5))

# Cada chamada recursiva empilha um novo "quadro" de execução na memória (pilha de chamadas)
# Para n muito grande, isso pode causar RecursionError mesmo com o limite aumentado, ou estourar a memória disponível
# Nesses casos, a versão ITERATIVA do mesmo algoritmo costuma ser mais segura
def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print("5! =", fatorial_iterativo(5))