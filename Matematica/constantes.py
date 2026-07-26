import math

# Constantes matemáticas prontas no módulo math
print("pi =", math.pi)
print("e =", math.e)

# math.inf: representa infinito, muito útil para inicializar "menor distância"/"menor valor" em algoritmos (Dijkstra, Kadane, etc), sem precisar de um número mágico grande
menor_distancia = math.inf
distancias_teste = [10, 3, 7]
for d in distancias_teste:
    if d < menor_distancia:
        menor_distancia = d
print("Menor distância:", menor_distancia)

# float("inf") é equivalente a math.inf e também é muito usado com o mesmo propósito
outro_infinito = float("inf")
print("Infinito maior que 10 ** 18?", outro_infinito > 10 ** 18)

# math.nan: representa "não é um número" (Not a Number), resultado de operações matematicamente indefinidas
nao_numero = math.nan
print(nao_numero == nao_numero)  # nan nunca é igual a si mesmo, nem a nada
print(math.isnan(nao_numero))    # forma correta de verificar se um valor é nan