import math

# ** (potenciação): operador nativo do Python, mais rápido e retorna int se base e expoente forem int
print("2^10 =", 2 ** 10)

# math.pow(x, y): equivalente a **, mas SEMPRE retorna float, mesmo com inteiros
print("2^10 =", math.pow(2, 10))

# pow(base, expoente, mod): exponenciação modular rápida (O(log expoente)), muito usada em problemas com resposta "módulo 10**9 + 7"
print("(2**10) % 1000 =", pow(2, 10, 1000))  # muito mais eficiente para expoentes grandes

# math.sqrt(x): raiz quadrada, sempre retorna float (pode causar erro de precisão em números muito grandes)
print("Raiz quadrada de 12:", math.sqrt(16))

# math.isqrt(x): raiz quadrada INTEIRA exata (parte inteira da raiz), sem erro de precisão de ponto flutuante — preferível a int(math.sqrt(x)) para números grandes
print("Raiz quadrada inteira de 50:", math.isqrt(50))

# math.log(x): logaritmo natural (base e)
print("Logaritmo natural na base e:", math.log(math.e))

# math.log(x, base): logaritmo de x em uma base customizada
print("Log(8, 2) =", math.log(8, 2)) 

# math.log2(x) / math.log10(x): versões mais precisas e diretas para base 2 e base 10
print(math.log2(8))     
print(math.log10(1000)) 

# Log é útil, por exemplo, para calcular a quantidade de dígitos de um número, ou o número de divisões de uma busca binária
n = 1000000
print("Quantidade de digitos de N:", math.floor(math.log10(n)) + 1) 