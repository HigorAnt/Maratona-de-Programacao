# & (AND): resulta em 1 apenas onde AMBOS os bits são 1
print(12 & 10)     # 8
print(bin(12), bin(10), bin(12 & 10))

# | (OR): resulta em 1 onde PELO MENOS UM dos bits é 1
print(12 | 10) 

# ^ (XOR): resulta em 1 onde os bits são DIFERENTES
print(12 ^ 10)

# ~ (NOT): inverte todos os bits (complemento). Em Python, ~n é equivalente a -(n+1)
print(~5)
print(~0)

# << (shift para a esquerda): desloca os bits para a esquerda, preenchendo com zeros
# Equivale a multiplicar por 2 elevado à quantidade de posições deslocadas
print(1 << 3)      
print(5 << 2)  

# >> (shift para a direita): desloca os bits para a direita, descartando os bits que "saem"
# Equivale a uma divisão inteira por 2 elevado à quantidade de posições deslocadas
print(20 >> 2)
print(7 >> 1)

# Verificar se um número é PAR ou ÍMPAR, olhando apenas o último bit (mais rápido que usar %)
def eh_par(n):
    return (n & 1) == 0

print(eh_par(10))
print(eh_par(7))

# Verificar se um número é uma POTÊNCIA DE 2
# Apenas potências de 2 têm exatamente 1 bit ligado, e "n & (n-1)" sempre desliga esse único bit, resultando em 0
def eh_potencia_de_2(n):
    return n > 0 and (n & (n - 1)) == 0

print("16 - potência de 2?", eh_potencia_de_2(16))
print("18 - potência de 2?", eh_potencia_de_2(18))
print("1 - potência de 2?", eh_potencia_de_2(1))

# Contar quantos bits estão LIGADOS (=1) em um número (conhecido como "popcount")
def contar_bits_ligados(n):
    contagem = 0
    while n > 0:
        contagem += n & 1
        n >>= 1
    return contagem

print("11 - quantos bits ligados?", contar_bits_ligados(11))
print("255 - quantos bits ligados?", contar_bits_ligados(255))

# Alternativa nativa e mais rápida, disponível a partir do Python 3.10
print((11).bit_count())

# Isolar o bit menos significativo ligado (lowest set bit) - truque muito usado em Fenwick Tree
def isolar_bit_menos_significativo(n):
    return n & (-n)

print("Bit menos significativo ligado:", isolar_bit_menos_significativo(12))

# Ligar (set) um bit específico em uma posição
def ligar_bit(n, posicao):
    return n | (1 << posicao)

print(bin(ligar_bit(0b1000, 1)))

# Desligar (clear) um bit específico em uma posição
def desligar_bit(n, posicao):
    return n & ~(1 << posicao)

print(bin(desligar_bit(0b1010, 1)))

# Verificar se um bit específico está ligado
def bit_esta_ligado(n, posicao):
    return (n & (1 << posicao)) != 0

print(bit_esta_ligado(0b1010, 1))
print(bit_esta_ligado(0b1010, 0))

# Trocar (alternar) o estado de um bit específico (toggle)
def alternar_bit(n, posicao):
    return n ^ (1 << posicao)

print(bin(alternar_bit(0b1010, 0)))