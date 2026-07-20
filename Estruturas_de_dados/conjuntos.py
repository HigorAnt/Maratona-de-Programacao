# conjunto criado diretamente
conjunto = {1, 2, 3, 4, 5}
print("O conjunto é: ", conjunto)

# lista com valores duplicados (o conjunto remove a duplicatas)
lista_com_duplicatas = [1, 2, 2, 3, 3, 4, 4, 4, 4]
conjunto_sem_duplicadas = set(lista_com_duplicatas)
print("Conjunto sem valores duplicados: ", conjunto_sem_duplicadas)

# criação de conjunto vazio
conjunto_vazio = set()

# recebendo os valores do usuário
entrada = input("Digite os números separados por espaço: ")
conjunto_entrada = set(map(int, entrada.split()))
print("O conjunto inserido é: ", conjunto_entrada)

# adiciona o valor 10
conjunto.add(10)
print("Conjunto após inserir o elemento 10: ", conjunto)

# insere vários valores
conjunto.update([8, 9, 11])
print("Conjunto após inserções: ", conjunto)

# remove o valor 3
conjunto.remove(3)
print("Conjunto após remoção do elemento 3: ", conjunto)

# remove o valor 100 e não retorna erro caso o valor não exista
conjunto.discard(100)
print("Conjunto após remoção do elemento 100: ", conjunto)

# retorna e remove o elemento
elemento_removido = conjunto.pop()
print("Elemento removido do conjunto: ", elemento_removido)

# verifica se o elemento existe ou não no conjunto
print(5 in conjunto)
print(120 not in conjunto)

# retorna o tamanho do elemento
print("Tamanho do conjunto: ", len(conjunto))

# retorna um novo conjunto com todos os elementos de ambos, removendo duplicatas
a = {1, 2, 3}
b = {3, 4, 5}
print("União dos conjuntos (a) e (b): ", a.union(b))
print(a | b)

# retorna um novo conjunto apenas com os elementos presentes em ambos
print("Elementos presentes em ambos os conjuntos: ", a.intersection(b))
print(a & b)

# retorna os elementos presentes em a que não estão em b
print("Elementos que estão em (a) mas não em (b): ", a.difference(b))
print(a - b)

# retorna os elementos que estão presentes em apenas um dos dois conjuntos
print("Elementos presentes em apenas um dos conjuntos: ", a.symmetric_difference(b))
print(a ^ b)

# update "in place" das operações acima: |=, &=, -=, ^= modificam o próprio conjunto em vez de criar um novo
c = {1, 2, 3}
c |= {4, 5}   # equivalente a c = c.union({4, 5})
print(c)

# issubset(outro) ou <=: verifica se todos os elementos do conjunto estão presentes em "outro"
d = {1, 2}
print(d.issubset(a))
print(d <= a)

# issuperset(outro) ou >=: verifica se o conjunto contém todos os elementos de "outro"
print(a.issuperset(d))
print(a >= d)

# isdisjoint(outro): retorna True se os dois conjuntos não têm nenhum elemento em comum
print(a.isdisjoint({10, 20}))

# Comparação de igualdade: dois conjuntos são iguais se têm os mesmos elementos, independente da ordem
print({1, 2, 3} == {3, 2, 1})

# clear(): remove todos os elementos, deixando o conjunto vazio
copia = a.copy()
copia.clear()
print(copia)

# Percorrendo um conjunto (a ordem de iteração não é garantida)
print("Elementos do conjunto a: ")
for elemento in a:
    print(elemento)

# Set Comprehension: cria um novo conjunto a partir de outro iterável, aplicando transformação e/ou filtro
quadrados = {x ** 2 for x in a}
print("Quadrado de cada elemento do conjunto a: ", quadrados)

# frozenset(): versão imutável de um conjunto. Não permite add/remove, mas pode ser usado como chave de dicionário ou elemento de outro conjunto
imutavel = frozenset([1, 2, 3])
# imutavel.add(4)  # geraria AttributeError, pois frozenset não tem esse método

# remover duplicatas de uma lista preservando o restante como lista novamente
lista_original = [1, 3, 2, 3, 1, 4]
lista_sem_duplicatas = list(set(lista_original))
print(lista_sem_duplicatas)  # atenção: a ordem original pode não ser preservada