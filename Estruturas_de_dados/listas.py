#recebimento da entrada do usuário
entrada = input("Digite os número separados por espaço: ")

#conversão da entrada em lista
lista = list(map(int, entrada.split()))

print("Lista: ", lista)
print("Primeiro elemento da lista: ", lista[0])
print("Último elemento da lista: ", lista[-1])
print("Elementos do índice 1 até 3: ", lista[1:4])
print("Elementos até o índice 1: ", lista[:2])
print("Lista invertida: ", lista[::-1])

lista[0] = 16
print("Lista após trocar o valor de índice 0: ", lista)

# adiciona ao fina da lista
lista.append(11)
print("Lista após adicionar 11 ao final: ", lista)

# insert(i, x) insere o valor x no índice i
lista.insert(4, 12)
print("Lista após inserir o valor 12 no índice 4: ", lista)

lista_auxiliar = [13, 14, 13, 13, 15]

# adiciona cada elemento da lista auxiliar após o último elemento da lista original
lista.extend(lista_auxiliar)
print("Lista após adicionar cada elemento da lista auxiliar: ", lista)

# remove(x) remove a primeira ocorrência de x
lista.remove(13)
print("Lista após remover a primeira ocorrência do valor 13 ", lista)

# remove e retorna o último valor da lista
removido = lista.pop()
# remore e retorna o valor da posição de índice 3
removido_i = lista.pop(3)
print(f"Último elemento da lista de valor {removido} removido, e {removido_i} removido do índice 3")
print("Lista após remoções: ", lista)

# index(x) retorna o índice da primeira ocorrência do elemento x
posicao = lista.index(7)
print("Posição do elemento 7 na lista: ", posicao)

# retorna todas as ocorrências do elemento 7
indices = [i for i, valor in enumerate(lista) if valor == 7]
print(indices)  

# procura a primeira ocorrência e começa a busca posterior a ela
primeira = lista.index(7)          
segunda = lista.index(7, primeira + 1) 
print("Índice da primeira e segunda ocorrência:", primeira, " ", segunda)

# count(x) retorna a quantidade de ocorrências do elemento de valor x
quantidade = lista.count(13)
print("Quantidade de ocorrências do elemento 13 na lista: ", quantidade)

# ordena de forma crescente os elementos da lista
lista.sort()
print("Lista ordenada de forma crescente: ", lista)

# ordena de forma descrescente os elementos da lista
lista.sort(reverse=True)
print("Lista ordenada de forma descrescente: ", lista)

# ordena a lista, mas utiliza a função lambda como parâmetro para isso
lista.sort(key=lambda x: abs(x))
print("Valores absolutos da lista ordenados crescentemente: ", lista)

# inverte as posições dos elemento da lista ( 0<->N-1, 1<->N-2...)
lista.reverse()
print("Lista após inverter as posições: ", lista)

# retorna o tamanho da lista (quantos elementos existem)
print("Tamanho da lista: ", len(lista))

# retorna a soma de todos os elementos da lista
print("Soma de todos os elementos da lista: ", sum(lista))

# retorna o valor do maior elemento da lista
print("Maior valor da lista: ", max(lista))

# retorna o valor do menor elemento da lista
print("Menor valor da lista: ", min(lista))

# retorna uma cópia independente da lista
copia = lista.copy()
print("Cópia da lista: ", copia)

#remove todos os elementos da lista
copia.clear()
print("Cópia após remover todos os itens: ", copia)

# retorna o quadrado de todos os elementos da lista
quadrados = [x ** 2 for x in lista]
print("Quadrado de cada elemento da lista: ", quadrados)

# retorna os elementos pares da lista
pares = [x for x in lista if x % 2 == 0]
print("Elementos pares da lista: ", pares)

# booleano - o elemento está presente ou não
print("20 está presente na lista? ", 20 in lista)