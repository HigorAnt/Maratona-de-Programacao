# Definição básica de função: def, nome, parâmetros entre parênteses, e o corpo indentado
def somar(a, b):
    return a + b

resultado = somar(3, 5)
print("Soma:", resultado)

# Funções sem retorno explícito retornam None por padrão
def exibir_mensagem(texto):
    print(texto)

valor_retornado = exibir_mensagem("Olá!")
print("Retorno:", valor_retornado) 

# Parâmetros com valor PADRÃO: usados automaticamente se o argumento correspondente não for passado
def saudacao(nome, cumprimento="Olá"):
    print(f"{cumprimento}, {nome}!")

saudacao("Maria")
saudacao("João", "Bom dia")

# Argumentos NOMEADOS (keyword arguments): permitem passar os valores em qualquer ordem, identificando pelo nome
def descrever_pessoa(nome, idade, cidade):
    print(f"{nome}, {idade} anos, de {cidade}")

descrever_pessoa(nome="Ana", cidade="Recife", idade=30)  # ordem diferente da definição, mas funciona

# CUIDADO: valores padrão MUTÁVEIS (lista, dicionário) são um erro clássico em Python
# O valor padrão é criado APENAS UMA VEZ, na definição da função, e reaproveitado entre chamadas
def adicionar_item_errado(item, lista=[]):  # lista=[] é perigoso!
    lista.append(item)
    return lista

print(adicionar_item_errado("a"))  # ['a']
print(adicionar_item_errado("b"))  # ['a', 'b']  <- inesperado! a lista "vazou" entre as chamadas

# Forma CORRETA de lidar com valor padrão mutável: usar None e criar a lista dentro da função
def adicionar_item_correto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(adicionar_item_correto("a"))  # ['a']
print(adicionar_item_correto("b"))  # ['b']  <- comportamento correto, sem "vazamento"

# *args: permite receber uma quantidade VARIÁVEL de argumentos posicionais, agrupados em uma tupla
def somar_varios(*args):
    print(type(args))  # <class 'tuple'>
    return sum(args)

print(somar_varios(1, 2, 3))
print(somar_varios(1, 2, 3, 4, 5))  # funciona com qualquer quantidade de argumentos

# **kwargs: permite receber uma quantidade VARIÁVEL de argumentos nomeados, agrupados em um dicionário
def exibir_informacoes(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="Carlos", idade=25, cidade="Fortaleza")

# É possível combinar parâmetros normais, *args e **kwargs na mesma função (nessa ordem obrigatoriamente)
def funcao_completa(obrigatorio, *args, **kwargs):
    print("Obrigatório:", obrigatorio)
    print("Args:", args)
    print("Kwargs:", kwargs)

funcao_completa(1, 2, 3, nome="Ana", idade=20)
# Obrigatório: 1
# Args: (2, 3)
# Kwargs: {'nome': 'Ana', 'idade': 20}

# Retorno múltiplo: uma função pode retornar vários valores separados por vírgula
# Por baixo dos panos, o Python empacota tudo em uma tupla automaticamente
def calcular_estatisticas(lista):
    return min(lista), max(lista), sum(lista) / len(lista)

menor, maior, media = calcular_estatisticas([4, 8, 15, 16, 23, 42])
print(f"Menor: {menor}. Maior: {maior}. Média: {media}")

# Se não desempacotar, o retorno múltiplo vem como uma tupla só
resultado_tupla = calcular_estatisticas([1, 2, 3])
print("Resultados:", resultado_tupla)

# Funções LAMBDA: funções anônimas de uma linha só, úteis para uso rápido (ex: como key em sort())
quadrado = lambda x: x ** 2
print("Quadrado de 5:", quadrado(5))

# Lambda com múltiplos parâmetros
soma_lambda = lambda a, b: a + b
print("Soma:", soma_lambda(3, 4)) 

# Funções como PARÂMETROS de outras funções (funções são "cidadãos de primeira classe" em Python)
def aplicar_operacao(lista, operacao):
    return [operacao(x) for x in lista]

numeros = [1, 2, 3, 4]
print(aplicar_operacao(numeros, quadrado)) 
print(aplicar_operacao(numeros, lambda x: x * 10))

# Escopo de variáveis: variáveis criadas DENTRO de uma função são LOCAIS a ela, não existem fora
def funcao_com_escopo():
    variavel_local = 10
    print(variavel_local)

funcao_com_escopo()
# print(variavel_local)  # geraria NameError, pois "variavel_local" não existe fora da função

# Variáveis GLOBAIS podem ser lidas normalmente de dentro de uma função, mas não modificadas sem a palavra "global"
contador_global = 0

def incrementar_errado():
    contador_global += 1  # geraria UnboundLocalError: tenta modificar sem declarar como global

def incrementar_correto():
    global contador_global  # declara que vai modificar a variável global, não criar uma local
    contador_global += 1

incrementar_correto()
print(contador_global)

# Funções recursivas
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))  # 120

# Docstring: string de documentação logo após a definição da função, explicando seu propósito
def calcular_area_retangulo(base, altura):
    """Calcula a área de um retângulo a partir da base e da altura."""
    return base * altura

print(calcular_area_retangulo(4, 5))
print(calcular_area_retangulo.__doc__)  # exibe a docstring da função