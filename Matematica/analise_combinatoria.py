import math

# math.factorial(n): calcula n! (fatorial)
print("5! =", math.factorial(5))

# Princípio Fundamental da Contagem (PFC): se uma decisão pode ser tomada de "a" formas
# e uma segunda decisão, independente da primeira, pode ser tomada de "b" formas,
# então as duas juntas podem ocorrer de a * b formas
letras_possiveis = 26
numeros_possiveis = 10
total_placas = (letras_possiveis ** 3) * (numeros_possiveis ** 4)
print("Quantidade de placas possíveis:", total_placas)

# math.perm(n, k): arranjo A(n, k) — de quantas formas escolher e ORDENAR k itens de n
print("Arranjo(5, 2):", math.perm(5, 2))

# math.perm(n): sem o segundo argumento, equivale ao próprio fatorial de n
print("5! =", math.perm(5))

# math.comb(n, k): combinação C(n, k) — de quantas formas escolher k itens de n, sem se importar com a ordem
print("Combinação(5, 2):", math.comb(5, 2))

# Relação entre combinação e arranjo: C(n, k) = A(n, k) / k!
n, k = 5, 2
print(math.perm(n, k) // math.factorial(k)) 