# bin(): converte um número decimal para sua representação em BINÁRIO (string com prefixo "0b")
print("11 em binário:", bin(11))
print("255 em binário:", bin(255))

# oct(): converte um número decimal para OCTAL (prefixo "0o")
print("11 em octal:", oct(11))
print("255 em octal:", oct(255))

# hex(): converte um número decimal para HEXADECIMAL (prefixo "0x", letras minúsculas por padrão)
print("11 em hexadecimal:", hex(11))
print("255 em hexadecimal:", hex(255))

# Removendo o prefixo, caso deseje apenas os dígitos (fatiamento a partir do índice 2)
print("11 em binário com fatiamento:", bin(11)[2:])
print("255 em hexadecimal com fatiamento:", hex(255)[2:])

# int(string, base): converte uma string em outra base de volta para um número inteiro decimal
print("1011 para decimal:", int("1011", 2))
print("377 para decimal:", int("377", 8))
print("16 para decimal:", int("ff", 16))

# int() também aceita a string JÁ com o prefixo, desde que a base seja informada corretamente
print("0b1011 para decimal:", int("0b1011", 2))
print("0xff para decimal:", int("0xff", 16))

# int(string, 0): detecta AUTOMATICAMENTE a base a partir do prefixo presente na própria string
print("0b1011 para decimal:", int("0b1011", 0))
print("0o17 para decimal:", int("0o17", 0))
print("0xff para decimal:", int("0xff", 0))

# Formatação com f-string: converte para binário/octal/hexadecimal SEM os prefixos "0b"/"0o"/"0x"
numero = 255
print(f"{numero} em binário: {numero:b}")
print(f"{numero} em octal: {numero:o}")
print(f"{numero} em hexadecimal minúsculo: {numero:x}")
print(f"{numero} em hexadecimal maiúsculo: {numero:X}")

# format() é equivalente à f-string, usando a mesma sintaxe de especificador
print("255 em binário:", format(255, 'b'))
print("255 em hexadecimal:", format(255, 'x')) 

# Preenchendo com zeros à esquerda até um tamanho fixo (comum ao representar bits de forma padronizada)
print(f"Número 5 em binário com 8 digítos: {5:08b}")

# Conversão MANUAL de decimal para binário
def decimal_para_binario(n):
    if n == 0:
        return "0"
    digitos = []
    while n > 0:
        digitos.append(str(n % 2))  # pega o bit menos significativo (resto da divisão por 2)
        n //= 2
    return "".join(reversed(digitos))  # os dígitos foram obtidos na ordem inversa, por isso o reversed()

print("11 em binário:", decimal_para_binario(11))
print("0 em binário:", decimal_para_binario(0))

# Conversão MANUAL de binário para decimal, aplicando a fórmula de soma ponderada por potências de 2
def binario_para_decimal(binario):
    resultado = 0
    for digito in binario:
        resultado = resultado * 2 + int(digito)  # desloca o resultado acumulado e soma o novo bit
    return resultado

print("1011 para decimal:", binario_para_decimal("1011"))
print("11111111 para decimal:", binario_para_decimal("11111111"))

# Convertendo diretamente de uma base para outra (ex: binário para hexadecimal), passando pelo decimal
def converter_base(numero_str, base_origem, base_destino):
    valor_decimal = int(numero_str, base_origem)
    if base_destino == 2:
        return bin(valor_decimal)[2:]
    elif base_destino == 8:
        return oct(valor_decimal)[2:]
    elif base_destino == 16:
        return hex(valor_decimal)[2:]
    else:
        return str(valor_decimal)

print("1011 para hexadecimal:", converter_base("1011", 2, 16))
print("ff para binário:", converter_base("ff", 16, 2))