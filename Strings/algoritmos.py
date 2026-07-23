from collections import Counter

nome1, nome2, nome3 = ["Higor", "ana", "Antonio Higor"]
frase1 = "Socorram me subi no onibus em marrocos"
# ========== 1. Palíndromo ==========
# Verifica se uma string é igual à sua versão invertida, usando dois ponteiros de fora para dentro
def palindromo(s):
    esquerda = 0
    direita = len(s) - 1
    while esquerda < direita:
        if s[esquerda] != s[direita]:
            return False
        esquerda += 1
        direita -= 1
    return True

print(f"{nome1} é palíndromo:", palindromo(nome1))  
print(f"{nome2} é palíndromo:", palindromo(nome2)) 

# Versão que ignora espaços, pontuação e diferenças de maiúscula/minúscula
def palindromo_normalizado(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
print("Frase 1 é palindromo:", palindromo_normalizado(frase1)) 

# ========== 2. Anagrama ==========
# Duas strings são anagramas se possuem exatamente os mesmos caracteres, na mesma quantidade

# Abordagem 1: ordenando os caracteres de ambas e comparando o resultado
def sao_anagramas_sorted(s1, s2):
    return sorted(s1) == sorted(s2)

# Abordagem 2: comparando a contagem de cada caractere (mais eficiente para strings longas)
def sao_anagramas_counter(s1, s2):
    return Counter(s1) == Counter(s2)

print(sao_anagramas_sorted("roma", "amor"))    
print(sao_anagramas_counter("roma", "amor"))    
print(sao_anagramas_counter("roma", "carro"))  

# ========== 3. Rotação de String ==========
# Verifica se "s2" é uma rotação de "s1", concatenando "s1" com ele mesmo e buscando "s2" dentro
def eh_rotacao(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

print(eh_rotacao("abcde", "cdeab"))  # True
print(eh_rotacao("abcde", "abced"))  # False

# ========== 4. Cifra de César ==========
# Desloca cada letra do alfabeto em uma quantidade fixa de posições, usando translate() + maketrans()
def cifra_de_cesar(texto, deslocamento):
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = alfabeto_minusculo.upper()

    deslocado_minusculo = alfabeto_minusculo[deslocamento:] + alfabeto_minusculo[:deslocamento]
    deslocado_maiusculo = alfabeto_maiusculo[deslocamento:] + alfabeto_maiusculo[:deslocamento]

    tabela = str.maketrans(
        alfabeto_minusculo + alfabeto_maiusculo,
        deslocado_minusculo + deslocado_maiusculo
    )
    return texto.translate(tabela)

texto_cifrado = cifra_de_cesar(nome3, 3)
print("Nome crifrado:", texto_cifrado)                      
print("Nome descifrado:", cifra_de_cesar(texto_cifrado, -3))    

# ========== 5. Compressão de String (Run-Length Encoding) ==========
# Compacta sequências de caracteres repetidos, no formato "caractereQuantidade"
def compressao_rle(s):
    if not s:
        return ""

    resultado = []
    caractere_atual = s[0]
    contagem = 1

    for c in s[1:]:
        if c == caractere_atual:
            contagem += 1
        else:
            resultado.append(caractere_atual + str(contagem))
            caractere_atual = c
            contagem = 1

    resultado.append(caractere_atual + str(contagem))  
    return "".join(resultado)

print("aaabbc:", compressao_rle("aaabbc"))      
print("abcd", compressao_rle("abcd"))         
print("aaaaaaaaaa", compressao_rle("aaaaaaaaaa")) 

# ========== 6. Verificação de parênteses balanceados ==========
# Usa uma pilha (lista) para garantir que cada fechamento corresponda à abertura mais recente
def parenteses_balanceados(s):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in "([{":
            pilha.append(c)
        elif c in ")]}":
            if not pilha or pilha.pop() != pares[c]:
                return False  # fechamento sem abertura correspondente, ou na ordem errada

    return len(pilha) == 0  # a pilha precisa estar vazia ao final (tudo foi devidamente fechado)

print("({[]}) é balanceado:", parenteses_balanceados("({[]})")) 
print("({[}]) é balanceado:", parenteses_balanceados("({[}])"))  
print("(() é balancedo:", parenteses_balanceados("(()"))     

# ========== 7. Maior Prefixo Comum entre uma Lista de Strings ==========
# Compara caractere a caractere a primeira string com as demais, até encontrar uma diferença
def maior_prefixo_comum(lista_strings):
    if not lista_strings:
        return ""

    prefixo = lista_strings[0]

    for palavra in lista_strings[1:]:
        while not palavra.startswith(prefixo):
            prefixo = prefixo[:-1]  # encolhe o prefixo removendo o último caractere
            if not prefixo:
                return ""

    return prefixo

print(maior_prefixo_comum(["flor", "florescer", "floresta"]))
print(maior_prefixo_comum(["cachorro", "gato", "pato"]))      