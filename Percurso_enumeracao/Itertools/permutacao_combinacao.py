from itertools import permutations, combinations, combinations_with_replacement

# permutations(iteravel): gera todas as PERMUTAÇÕES possíveis (todas as ordens), como tuplas
# A ordem importa: (1, 2, 3) é diferente de (3, 2, 1)
lista = [1, 2, 3]
todas_permutacoes = list(permutations(lista))
print("Permutações possíveis:", todas_permutacoes)

# permutations(iteravel, r): gera permutações de tamanho r (sem repetir elementos dentro de cada tupla)
permutacoes_de_2 = list(permutations(lista, 2))
print("Permutações com 2 elementos:", permutacoes_de_2)

# combinations(iteravel, r): gera todas as COMBINAÇÕES de tamanho r, SEM repetir elementos e SEM se importar com a ordem
# (1, 2) é considerado igual a (2, 1), então apenas uma das duas aparece
combinacoes_de_2 = list(combinations(lista, 2))
print("Combinações de 2 elementos:", combinacoes_de_2)

# combinations_with_replacement(iteravel, r): como combinations, mas PERMITE repetir o mesmo elemento
combinacoes_repeticao = list(combinations_with_replacement(lista, 2))
print("Combinações com repetição:", combinacoes_repeticao)

# permutação e combinação sem duplicadas
permutacoes = set(permutations([1, 1, 2], 2))
combinacoes = set(combinations([1, 1, 2], 2))

print("Permutações:", permutacoes)
print("Combinações:", combinacoes)

# Os geradores do itertools são "preguiçosos": as tuplas são geradas sob demanda.
# Isso permite interromper a busca assim que uma condição for satisfeita,
# sem gerar as permutações/combinações restantes - economiza tempo em força bruta.
for p in permutations(lista):
    if sum(p) == 6:
        print("Achou:", p)
        break

# Exemplo prático: gerar todos os subconjuntos possíveis de uma lista (todas as combinações de todos os tamanhos)
def todos_subconjuntos(lista):
    subconjuntos = []
    for tamanho in range(len(lista) + 1):
        subconjuntos.extend(combinations(lista, tamanho))
    return subconjuntos

print("Subconjuntos:", todos_subconjuntos([1, 2, 3]))

# Todas as funções retornam ITERADORES, não listas - por isso o list() é necessário para visualizar
# Isso é eficiente em memória: os valores são gerados um por um, sob demanda, sem armazenar tudo de uma vez
gerador = permutations(lista)
print(type(gerador))

# É possível percorrer o iterador diretamente em um for, sem precisar converter para lista
for p in permutations([1, 2, 3], 2):
    print(p)