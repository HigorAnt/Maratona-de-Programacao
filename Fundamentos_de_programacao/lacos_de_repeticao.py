# laço for percorre 1 a 1 dos elementos de um iterável
for i in range(4):
    print(i)

# range(incício, fim): gera números de "início" até fim-1
for i in range(2, 5):
    print(i)

# range(início, fim, passo): define o tamanho do incremento/passo
for i in range(0, 10, 2):
    print(i)

# impressão descrescente, com passo -1
for i in range(5, 0, -1):
    print(i)

# percorrendo elementos de uma lista
pessoas = ["Higor", "Vitor", "Dagoberto"]
for pessoa in pessoas:
    print(pessoa)

# for com enumerate() percorre a lista e retorna o índice e valor
for indice, pessoa in enumerate(pessoas):
    print(indice, pessoa)

# start define o valor inicial da contagem (padrão é 0)
for indice, pessoa in enumerate(pessoas, start=1):
    print(indice, pessoa)

# percorrer cada caracter de uma string
for letra in "Higor":
    print(letra)

# while: repete o bloco enquanto uma condição for verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# a condição de parada encontra-se no bloco dentro do while (break)
while True:
    valor = int(input("Digite um número (0 para sair): "))
    if valor == 0:
        break
    print(f"Valor digitado: {valor}")

# continue: ignora os comandos seguintes do bloco e pula para a próxima iteração
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# for aninhados. break e continue agem apenas no for mais interno a eles
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(f"i={i}, j={j}")

# list comprehension (geralmente mais rápido)
quadrados_compreensao = [x ** 2 for x in range(5)]
print(quadrados_compreensao)

# range() não criar um lista de fato - é apenas um objeto "preguiçoso" (gera valores sob demanada), economizando memória
print(type(range(10)))
print(list(range(5)))