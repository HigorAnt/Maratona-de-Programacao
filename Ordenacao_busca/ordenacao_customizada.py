from functools import cmp_to_key
from operator import itemgetter

# sorted() cria uma NOVA lista ordenada, sem alterar a lista original
lista_original = [5, 2, 9, 1, 5, 6]
lista_ordenada = sorted(lista_original)
print("Lista ordenada:", lista_ordenada) 
print("Lista original:", lista_original)

# sort() ordena a própria lista "in place" (modifica a original, não retorna nada de novo)
lista_original.sort()
print("Lista original ordenada:", lista_original)

# reverse=True inverte o critério de ordenação, deixando em ordem decrescente
print("Lista decrescente:", sorted([5, 2, 9, 1], reverse=True))

# key=: ordena com base no resultado de uma função aplicada a cada elemento, não no valor bruto
palavras = ["banana", "abacaxi", "uva", "melancia"]
print("Lista ordenada pelo tamanho da palavra:", sorted(palavras, key=len))

# key= com lambda para um critério customizado (ex: ordenar por valor absoluto)
numeros = [-5, 3, -2, 8, -1]
print("Lista ordenada por valor absoluto:", sorted(numeros, key=lambda x: abs(x)))

# Ordenando uma lista de tuplas por um elemento específico
alunos = [("Ana", 8.5), ("Bruno", 7.0), ("Carla", 9.2)]
print("Lista ordenada pelas notas:", sorted(alunos, key=lambda aluno: aluno[1]))

# Ordenando por MÚLTIPLOS critérios: a tupla retornada pelo key= é comparada posição a posição
# (primeiro critério decide, e o segundo serve de "desempate")
pessoas = [("Ana", 25), ("Bruno", 30), ("Carla", 25), ("Davi", 20)]
print("Lista ordenada pela idade depois nome:", sorted(pessoas, key=lambda pessoa: (pessoa[1], pessoa[0])))

# Ordenar um critério DECRESCENTE e outro CRESCENTE ao mesmo tempo: usa-se o sinal negativo
# no critério numérico que deve ser decrescente (só funciona diretamente com números)
produtos = [("Caneta", 5, 10), ("Caderno", 15, 3), ("Mochila", 80, 3)]
print(sorted(produtos, key=lambda p: (-p[2], p[1])))

# itemgetter (do módulo operator) como alternativa ao lambda: mais rápido em listas muito grandes,
# pois evita a sobrecarga de chamar uma função Python a cada comparação
print(sorted(alunos, key=itemgetter(1)))  # equivalente a key=lambda aluno: aluno[1]

# cmp_to_key: usado quando o critério de ordenação não é uma "chave" simples, mas sim uma
# função de COMPARAÇÃO entre dois elementos (deve retornar negativo, zero ou positivo)
def comparar(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

print(sorted([5, 2, 9, 1], key=cmp_to_key(comparar)))

# Exemplo prático de cmp_to_key: ordenar strings numéricas para formar o MAIOR número possível
# ao concatená-las - não é possível expressar isso com uma key= simples, pois depende do PAR comparado
def comparar_concatenacao(a, b):
    if a + b > b + a:
        return -1  # "a" deve vir antes de "b"
    else:
        return 1

numeros_str = ["3", "30", "34", "5", "9"]
resultado = sorted(numeros_str, key=cmp_to_key(comparar_concatenacao))
print("".join(resultado))

# min() e max() também aceitam key=, retornando o ELEMENTO (não o valor da chave)
print(max(alunos, key=lambda aluno: aluno[1]))
print(min(alunos, key=lambda aluno: aluno[1]))

# Ordenação ESTÁVEL: o sort()/sorted() do Python preserva a ordem relativa original
# entre elementos que possuem a MESMA chave de ordenação
dados = [("a", 1), ("b", 1), ("c", 2), ("d", 1)]
print(sorted(dados, key=lambda x: x[1]))