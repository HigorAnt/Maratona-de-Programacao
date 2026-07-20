# recebendo uma entrada do usuário 
# input("") além de receber valores também pode exibir uma mensagem no console
# por padrão toda entrada é string <class 'str'>
texto = input("Digite alguma entrada: ")
print("Tipo da entrada digitada: ", type(texto))

# para converter a entrada para inteiro usa-se int(input())
numero = int(input("Digite um número: "))
print("Tipo da entrada digitada: ", type(numero))

# corta a entrada "ao meio" pelo espaço e associa cada um a uma das variáveis
a, b = input("Digite duas entradas separadas por espaço: ").split()
print(f"A:{a}, B:{b}")

# corta a entrada em duas e converte ambas para inteiro
x, y = map(int, input("Digite dois números separados por espaço: ").split())
print(f"X:{x}, Y:{y}")

# a entrada é cortada em várias partes e cada uma armazenada em um ídice da lista
vetor = list(map(int, input("Digite números diversos separados por espaço: ").split()))
for i in range(len(vetor)):
    print(vetor[i])

# recebimento de n valores definidos previamente em uma lista
n = int(input("Quantos valores receber: "))
valores = []
for _ in range(n):
    valores.append(int(input()))

# impressão dos n valores recebidos
print("Valores digitados:")
for i in range(n):
    print(valores[i])