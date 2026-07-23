# String de exemplo
frase = "Ola, campus da UFC"

# split(): divide a string em uma lista, usando espaço como separador padrão
print(frase.split()) 

# split(separador): divide usando um separador customizado
csv = "10,20,30"
print(csv.split(","))  # ['10', '20', '30']

# split(separador, maxsplit): limita o número de divisões realizadas
print("a-b-c-d".split("-", 1))  

# join(lista): junta os elementos de uma lista em uma única string, usando a string chamadora como separador
palavras = ["Maratona", "de", "Programação"]
print(" ".join(palavras))  

# strip(): remove espaços em branco (e quebras de linha) do início e do fim da string
com_espacos = "   texto com espacos   "
print("Após formatação:", com_espacos.strip()) 

# lstrip() / rstrip(): removem espaços em branco apenas da esquerda ou apenas da direita
print("Após formatação:", com_espacos.lstrip())  
print("Após formatação:", com_espacos.rstrip())

# strip(caracteres): remove os caracteres especificados (não apenas espaços) das duas pontas
print("###titulo###".strip("#"))  # 'titulo'

# upper() / lower(): convertem a string inteira para maiúsculas ou minúsculas
print("Texto maiúsculo:", frase.upper())  
print("Texto minúsculo:", frase.lower()) 

# capitalize(): deixa apenas a primeira letra maiúscula, e força o restante para minúsculo
print("python é ótimo".capitalize()) 

# title(): deixa a primeira letra de CADA palavra em maiúscula
print("python é ótimo".title()) 

# replace(antigo, novo): substitui TODAS as ocorrências de um trecho por outro
print(frase.replace("a", "@")) 

# replace(antigo, novo, quantidade): limita quantas ocorrências serão substituídas, da esquerda para a direita
print("aaaa".replace("a", "b", 2))

# find(x): retorna o índice da primeira ocorrência de x, ou -1 se não encontrar (NÃO gera erro)
print(frase.find("a"))

# index(x): funciona como find(), mas gera ValueError se x não for encontrado cuidado ao escolher entre os dois: index() pode quebrar seu programa se você não tratar o erro
# print(frase.index("z"))  # geraria ValueError, pois "z" não existe em frase

# count(x): conta quantas vezes a substring x aparece na string
print(frase.count("a"))  # 7

# startswith(x) / endswith(x): verificam se a string começa ou termina com x
print(frase.startswith("Ola"))  # True
print(frase.endswith("cao"))    # True

# is*(): família de métodos que verificam o CONTEÚDO da string inteira
print("12345".isdigit())    # True  -- todos os caracteres são dígitos
print("abcXYZ".isalpha())   # True  -- todos os caracteres são letras
print("abc123".isalnum())   # True  -- todos os caracteres são letras OU números
print("   ".isspace())      # True  -- todos os caracteres são espaços em branco
print("PYTHON".isupper())   # True  -- todos os caracteres alfabéticos estão em maiúscula
print("python".islower())   # True  -- todos os caracteres alfabéticos estão em minúscula

# zfill(n): preenche a string com zeros à esquerda até atingir o tamanho n (útil para IDs/códigos)
print("7".zfill(3))  # '007'

# ord(c): retorna o código Unicode/ASCII de um caractere
print(ord("A")) 

# chr(n): converte um código Unicode/ASCII de volta para o caractere
print(chr(65))  