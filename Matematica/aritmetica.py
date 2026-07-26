# / (divisão) sempre retorna float, mesmo entre dois inteiros
print("10 / 3 =", 10 / 3)

# // (divisão inteira) arredonda para BAIXO (floor), não trunca — cuidado com números negativos
print("Arredondamento de 7 / 2 =", 7 // 2)
print("Arredondamento de -7 / 2 =", -7 // 2)

# % (módulo/resto) segue a mesma lógica de arredondamento para baixo, então também muda de sinal com negativos
print("Resto de 7 / 2 =", 7 % 2) 
print("Resto de -7 / 2 =", -7 % 2)    # o resultado do módulo sempre tem o mesmo sinal do divisor

# divmod(a, b): retorna (quociente, resto) de uma vez, evitando calcular // e % separadamente
quociente, resto = divmod(17, 5)
print(f"17 / 5 quociente {quociente} resto = {resto}")

# abs(x): valor absoluto, funciona com int e float
print("Valor absoluto de -7.5:", abs(-7.5))

# round(x): arredonda para o inteiro mais próximo. Atenção: usa "round half to even" (arredondamento bancário) em casos de empate
print("Arredondamento:", round(2.5))  # arredonda para o par mais próximo
print("Arredondamento:", round(3.5))

# round(x, casas): arredonda para um número específico de casas decimais
print("Arredondamento com duas casas:", round(3.14159, 2))

# math.floor(x) / math.ceil(x): arredondam para baixo/para cima, sempre retornando int
import math
print("Arredondando 3,7 pra cima:", math.floor(3.7))
print("Arredondando 3,2 pra baixo:", math.ceil(3.2)) 

# math.gcd(a, b): máximo divisor comum (MDC) entre dois números
print("MDC(54, 240:", math.gcd(54, 24))

# math.gcd aceita múltiplos argumentos, retornando o MDC entre todos eles
print("MDC(48, 60, 36):", math.gcd(48, 60, 36))

# MMC (mínimo múltiplo comum) não tem função pronta em versões antigas, mas é calculado a partir do MDC
def mmc(a, b):
    return a * b // math.gcd(a, b)

print("MMC(4,6):", mmc(4, 6))

# math.lcm(a, b, ...): calcula o MMC diretamente, aceitando múltiplos argumentos
print("MMC(4, 6):", math.lcm(4, 6))       
print("MMC(4, 6, 8):", math.lcm(4, 6, 8))   