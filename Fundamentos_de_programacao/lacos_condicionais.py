# if é atendido se a condição for verdaderia
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("É maior de idade")
else:
    print("É menor de idade")

# é possível testar múltiplas condições em sequência, na ordem que aparecem
# operadores lógicos podem ser utilizados (and, or, not)
nota = float(input("Digite sua nota: "))
if nota >= 7:
    print("Passou direto")
elif nota >= 4 and nota < 7:
    print("Avaliação final")
else:
    print("Reprovação")

# operadores de comparação
# == (igual), != (diferente), <, >, <=, >=
a = 10
b = 15
print(a == b)
print(a != b)
print(a > b)

# operador ternário: valor_se_verdadeiro IF condição ELSE valor_se_falso
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

status = "Passou direto" if nota >= 7 else "Avaliação final" if nota >= 4 and nota < 7 else "Reprovado"
print(status)

# são considerados "falsos": string vazias, 0, 0.0, [], {}, set() e None
lista_vazia = []
if lista_vazia:
    print("A lista têm elementos")
else:
    print("A lista não tem elementos")

# encadeamento de comparações
idade = 21
print(0 < 21 <25) # True

# comparação entre diferentes tipos numéricos
print(5 == 5.0)

# a comparação de igualdade entre float pode ter problemas de precisão
print(0.1 + 0.2 == 0.3)  # False! (erro de arredondamento em ponto flutuante)
# Para comparar floats com segurança, usa-se uma margem de tolerância
print(abs((0.1 + 0.2) - 0.3) < 1e-9)  # True, forma correta de comparar

# match/case: alternativa ao if/elif encadeado para múltiplos valores fixos
comando = "iniciar"

match comando:
    case "iniciar":
        print("Iniciando o programa")
    case "pausar":
        print("Pausando o programa")
    case "parar":
        print("Parando o programa")
    case _:  # underscore funciona como o "else" - caso nenhum dos anteriores corresponda
        print("Comando desconhecido")