# recebimento da entrada do usuário
entrada = input("Digire os números separados por espaço: ")

# conversão da entrada em tupla
tupla = tuple(map(int, entrada.split()))

# tuplas criadas diretamente
tupla_direta = (1, 2, 3, 3, 4)
tupla_sem_parenteses = 5, 6, 7, 8
tupla_unico_elemento = (15,)
tupla_vazia = ()

print(tupla)
print("Elemento do índice 0 da tupla: ", tupla[0])
print("Último elemento da tupla: ", tupla[-1])
print("Fatiamento da tupla: ", tupla[1:3])
print("Tupla invertida: ", tupla[::-1])

# count(x) retorna a quantidade de ocorrências do elemento de valor x
quantidade = tupla.count(3) 
print(f"O elemento 3 aparece {quantidade} vezes")

# index(x) retorna o índice da primeira ocorrência do elemento x
posicao = tupla.index(3)
print("A primeira ocorrência do elemento 3 é no índice ", posicao)

# retorna o tamanho da tupla (quantos elementos existem)
tamanho = len(tupla)
print(f"O tamanho da tupla é {tamanho} elementos")

print("A soma dos elementos da tupla é: ", sum(tupla))
print("O maior elemento da tupla é: ", max(tupla))
print("O menor elemento da tupla é: ", min(tupla))

print("O número 3 não está presente na tupla? ", 3 not in tupla)

# associa cada variável a um elemento da tupla
a, b, c = (1, 2, 3)
print("Os elementos associados a (a, b, c) respectivamente são: ", a, b, c)

# o asterisco captura o resto dos elementos em uma tupla
primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
print(f"Elemento primeiro ({primeiro}), meio ({meio}) e último ({ultimo})")

# para adicionar um elemento a uma tupla é necessário uma nova tupla
nova_tupla = tupla + (16,)
print("A nova tupla é: ", nova_tupla)

# concatenação de tuplas
tupla_a = (10, 20, 30)
tupla_b = 40, 50, 60
print("A tupla concatenada é: ", tupla_a + tupla_b)

print("A tupla repetida 3 vezes é: ", tupla * 3)

# para usar métodos da lista, converte-se a tupla em lista
lista_temp = list(tupla)
tupla = tuple(tupla)

# obtenção de uma tupla a partir de uma expressão geradora
quadrados = tuple(x ** 2 for x in tupla)
print("O quadrado de cada elemento da tupla é: ", quadrados)

# tupla usada como chave em um dicionário
coordenadas = {(0, 0): "origem", (1, 1): "diagonal"}
print("A coordenada (0, 0) é a ", coordenadas[(0, 0)])

# comparação de tuplas, feita de elemento a elemento, da esquerda para a direita
print((1, 2, 3) < (1, 2, 4))
print((1, 2) < (1, 2, 0))