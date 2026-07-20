# impressão padrão com quebra de linha no final
print("Olá, mundo!")

# impressão de múltimplos valores (separados por espaço automaticamente)
print("Idade:", 21)

# sep: define o separador entre os valores (o padrão é o espaço)
print(1, 2, 3, sep="-")

# end: define o que é impresso no final (padrão é a quebra de linha)
print("Sem quebrar linha,", end=" ")
print("o texto continua")

# formatando saída para delimitar a quantidade de casas decimais
media = 8.9483
print(f"A média é: {media:.2f}")

# o asterisco imprime a lista separando os elementos (desempacota colocando espaços)
vetor = [1, 2, 3, 4, 5, 6]
print(*vetor)

# equivalente a linha anterior, mas usando o join()
print(" ".join(map(str, vetor)))

# impressão de cada elemento em uma linha separada
for elemeto in vetor:
    print(elemeto)