from collections import defaultdict

# Cria um defaultdict que usa int como fábrica de valores padrão (int() retorna 0)
contador = defaultdict(int)

# Diferente de um dicionário comum, acessar uma chave inexistente NÃO gera erro: ela é criada automaticamente com o valor padrão (0)
contador["a"] += 1
contador["a"] += 1
contador["b"] += 1
print("Defaultdict:", contador)  

# Exemplo prático: contar frequência de elementos de uma lista, sem precisar checar se a chave já existe
lista = [1, 2, 2, 3, 3, 3]
frequencia = defaultdict(int)
for valor in lista:
    frequencia[valor] += 1
print("Frequência dos elementos da lista:", frequencia)

# defaultdict(list): usa list como fábrica, então cada chave nova começa com uma lista vazia
grupos = defaultdict(list)

# append() direto na chave, sem precisar inicializar a lista manualmente antes
grupos["pares"].append(2)
grupos["pares"].append(4)
grupos["impares"].append(1)
print("Grupos:", grupos)

# Exemplo prático: construir uma lista de adjacência de grafo sem checagem manual de chave
grafo = defaultdict(list)
arestas = [(1, 2), (1, 3), (2, 3)]
for u, v in arestas:
    grafo[u].append(v)
    grafo[v].append(u)  # grafo não direcionado
print("Lista de adjacência do grafo:", grafo)

# defaultdict(set): usa set como fábrica, útil quando não se quer vizinhos duplicados
grafo_sem_duplicatas = defaultdict(set)
for u, v in arestas:
    grafo_sem_duplicatas[u].add(v)
    grafo_sem_duplicatas[v].add(u)
print("Remoção das duplicatas:", grafo_sem_duplicatas)

# defaultdict com uma função lambda customizada como fábrica, para valores padrão diferentes de int/list/set
notas = defaultdict(lambda: "sem nota")
notas["joao"] = 8.5
print("Nota de João:", notas["joao"])
print("Nota de Maria:", notas["maria"])

# Comparação: o mesmo agrupamento feito com dict comum exigiria checagem manual da chave
grupos_manual = {}
for valor in lista:
    if valor not in grupos_manual:
        grupos_manual[valor] = []
    grupos_manual[valor].append(valor)
print(grupos_manual)

# Cuidado: apenas ACESSAR uma chave em um defaultdict já a cria (mesmo sem atribuir valor), o que pode inflar o dicionário sem querer
d = defaultdict(int)
if d["chave_nunca_usada"] == 0:  # essa chave já foi criada só por ter sido acessada aqui
    pass
print("Defaultdict após inflar:", list(d.keys()))

# Para verificar existência sem criar a chave acidentalmente, use "in" em vez de acessar diretamente
d2 = defaultdict(int)
print("x está presente?", "x" in d2) 

# Convertendo de volta para dicionário comum, se necessário (ex: para evitar criação acidental de chaves depois)
dict_normal = dict(grupos)
print("Conversão para dicionário:", dict_normal)