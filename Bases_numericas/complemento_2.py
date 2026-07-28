# Em Python, bin() de um número NEGATIVO mostra o sinal separado com um "-", não o complemento de dois real
print(bin(-5)) 
print(bin(5))
# Isso acontece porque os inteiros do Python têm precisão ARBITRÁRIA (não usam um número fixo de bits,
# como 8, 16, 32 ou 64 bits, diferente de linguagens como C ou Java)

# Para obter a representação em COMPLEMENTO DE DOIS de um número negativo, é preciso definir quantos bits serão usados (ex: 8 bits) - Python não faz isso automaticamente
def complemento_de_dois(n, bits=8):
    if n < 0:
        n = (1 << bits) + n  # soma 2^bits ao número negativo, "dando a volta" no intervalo
    return n

print(bin(complemento_de_dois(-5, 8)))
print(bin(complemento_de_dois(5, 8)))

# Em 8 bits, o intervalo de valores representáveis vai de -128 a 127
# -5 em complemento de dois (8 bits) corresponde a 251 em decimal (256 - 5)
print(complemento_de_dois(-5, 8))

# Formatando diretamente com zeros à esquerda, para visualizar os 8 bits completos
print(f"{complemento_de_dois(-5, 8):08b}")
print(f"{complemento_de_dois(5, 8):08b}")

# Convertendo de VOLTA: interpretando uma sequência de bits (já em complemento de dois) como um número COM sinal
def bits_para_inteiro_com_sinal(bits_str):
    valor = int(bits_str, 2)
    bits_totais = len(bits_str)

    # Se o bit mais significativo (o primeiro) for 1, o número é negativo
    if bits_str[0] == '1':
        valor -= (1 << bits_totais)

    return valor

print(bits_para_inteiro_com_sinal('11111011'))
print(bits_para_inteiro_com_sinal('00000101'))

# Demonstração de OVERFLOW (estouro) em uma representação de tamanho fixo:
# somar dois números cujo resultado ultrapassa o maior valor positivo representável "dá a volta" para negativo
def somar_com_overflow(a, b, bits=8):
    limite = 1 << bits
    resultado = (a + b) % limite

    # Se o resultado ultrapassar a metade do intervalo, interpreta como negativo
    if resultado >= limite // 2:
        resultado -= limite

    return resultado

print(somar_com_overflow(127, 1, 8))    # -128, overflow: "deu a volta" ao ultrapassar o limite de 8 bits
print(somar_com_overflow(100, 50, 8))   # -106, 150 ultrapassa 127 (o máximo positivo em 8 bits) e estoura

# Operações bit a bit do Python (~, &, |, ^) já funcionam corretamente com números negativos,
# pois o Python simula internamente um número "infinito" de bits à esquerda preenchidos com 1's
# para representar valores negativos (diferente da representação de tamanho fixo usada em C/Java)
print(~5)         # -6, resultado correto, sem qualquer ajuste manual necessário
# Mascarar com 0xFF simula a VISUALIZAÇÃO de um número negativo como se estivesse em 8 bits
print(-5 & 0xFF)  # 251, mesmo valor obtido manualmente com complemento_de_dois(-5, 8)