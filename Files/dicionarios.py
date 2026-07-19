# dicionário criado diretamente
dicionario = {"nome": "Higor", "idade": 21, "cidade": "Crateús"}
print(dicionario)
print(dicionario["nome"])

# get(chave, padrão) acessa o valor pela chave e retorna padrão se ela não existir
print(dicionario.get("profissao", "N/A"))

# inserção de cada par chave-valor por linha, com um n definido anteriormente
n = int(input("Quantos pares serão inseridos? "))
dicionario_dinamico = {}
for _ in range(n):
    chave, valor = input("Digite a chave e valor separados por espaço: ").split()
    dicionario_dinamico[chave] = valor

print(dicionario_dinamico)

# criação de dicionários a partir de chave=valor e lista de tuplas, respectivamente
dicionario_alternativo = dict(a=1, b=2, c=3)
dicionario_lista_de_tuplas = dict([("x", 10), ("y",20)])

# adiciona um par chave-valor ou atualiza o valor se a chave já existir
dicionario["profissao"] = "Estudante"
print("Dicionário após inserir a profissão: ", dicionario)

# verifica se uma chave existe no dicionário
print("formacao" in dicionario)

# retorna um onject view com todas as chaves (pode ser percorrido ou convertido em lista)
print("Todas as chaves do dicionário: ", list(dicionario.keys()))

# retorna um object view com todos os valores
print("Todos os valores do dicionário: ", list(dicionario.values()))

# retorna um object view com tuplas (chave-valor)
print("Tuplas dos pares chave-valor do dicionário: ", list(dicionario.items()))

# remove a chave e retorna o valor associado. Se não existir retorna o valor padrão (0)
idade_removida = dicionario.pop("idade", 0)
print("Idade removida: ", idade_removida)
print("Dicionário após remoção da idade: ", dicionario)

# popitem() remove e retorna o último par chave-valor inserido
ultimo_par = dicionario.popitem()
print("Último par chave-valor inserido: ", ultimo_par)

# update() mescla outro dicionário no atual, sobrescrevendo chaves repetidas
dicionario.update({"nome": "Antonio", "cidade": "Ipaporanga"})
print("Dicionário após ser sobrescrito: ", dicionario)

# setdefautl(chave, valor), retorna o valor da chave se ela existir, se não insere a chave com o valor padrão
dicionario.setdefault("idade", 21)
print("Dicionário após operação: ", dicionario)

# retorna a quantidade de pares chave-valor no dicionário
print("Quantidade de pares chave-valor no dicionário: ", len(dicionario))

# percorre apenas as chaves do dicionário
print("Chaves do dicionário:")
for chave in dicionario:
    print(chave)

# percorre os pares chave-valor do dicionário
print("Pares chave-valor do dicionário:")
for chave, valor in dicionario.items():
    print(chave, valor)

# cria um novo dicionário a partir de outro aplicando uma transformação e/ou filtro
maiusculas = {chave: valor.upper() for chave, valor in dicionario.items() if isinstance(valor, str)}
print("Dicionário após aplicar o filto: ", maiusculas)

# inverte chave e valor de um dicionário (valores repetidos são sobrescrevidos)
invertido = {valor: chave for chave, valor in dicionario.items()}
print("Dicionário após inversão dos valores: ", invertido)

# cria uma cópia do dicionário e remove todos os pares chave-valor
copia = dicionario.copy()
copia.clear()
print("Dicionário após remover todos os pares: ", copia)

# cria um novo dicionário com as chaves do iterável, todas com o mesmo valor inicial
contador = dict.fromkeys(["a", "b", "c"], 0)
print(contador)

# dicionários aninhados, onde os valores podem ser outros dicionários
alunos = {
    "Vitor": {"nota": 7.0, "idade": 21},
    "Dagoberto": {"nota": 8.5, "idade": 22}
}
print(alunos["Vitor"]["nota"])
print(alunos["Dagoberto"]["idade"])

# zip(chave, valor) recebe dois ou mais iteráveis e os entrelaça. Caso um seja maior que o outro, descarta os excedentes
chaves = ["nome", "idade", "cidade", "estado"]
valores = ["Maria", 25, "Recife"]
dict_via_zip = dict(zip(chaves, valores))
print(dict_via_zip) 