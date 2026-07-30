from itertools import product

# product(iteravel1, iteravel2, ...): gera o PRODUTO CARTESIANO entre os iteráveis, equivalente a laços aninhados
cores = ["azul", "verde"]
tamanhos = ["P", "M", "G"]
combinacoes_produto = list(product(cores, tamanhos))
print("Produto cartesiano:", combinacoes_produto)

# product(iteravel, repeat=n): repete o MESMO iterável n vezes no produto cartesiano
# útil para gerar todas as combinações de bits, dígitos, ou estados possíveis
todas_combinacoes_binarias = list(product([0, 1], repeat=3))
print("Produto cartesiano:", todas_combinacoes_binarias)

# Via product: mais legível, gera tuplas prontas
for estado in product([0, 1], repeat=2):
    print("Estados possíveis:", estado)

# Via bitmask: mais rápido, mas exige extrair os bits manualmente
for mascara in range(2**3):
    bits = tuple((mascara >> i) & 1 for i in range(3))

# o product varia o último iterável mais rápido, como um hodômetro (dígito da direita muda primeiro):
print("Elementos:", list(product([1,2], [3,4])))