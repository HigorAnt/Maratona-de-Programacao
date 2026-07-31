# Exemplo 1: Janela deslizante de TAMANHO FIXO - soma máxima de um subarray de tamanho k
def soma_maxima_janela_fixa(lista, k):
    # Calcula a soma da primeira janela (os k primeiros elementos)
    soma_atual = sum(lista[:k])
    soma_maxima = soma_atual

    # Desliza a janela um elemento por vez: remove o que sai à esquerda, adiciona o que entra à direita
    for i in range(k, len(lista)):
        soma_atual += lista[i] - lista[i - k]
        soma_maxima = max(soma_maxima, soma_atual)

    return soma_maxima

print("Maior soma com janela de 3:", soma_maxima_janela_fixa([2, 1, 5, 1, 3, 2], 3))

# Exemplo 2: Janela deslizante de TAMANHO VARIÁVEL - menor subarray com soma >= alvo
def menor_subarray_com_soma_minima(lista, alvo):
    esquerda = 0
    soma_atual = 0
    menor_tamanho = float("inf")

    for direita in range(len(lista)):
        soma_atual += lista[direita]

        # Enquanto a soma da janela já atende (ou excede) o alvo, tenta encolher pela esquerda
        # para buscar o menor tamanho possível que ainda satisfaça a condição
        while soma_atual >= alvo:
            menor_tamanho = min(menor_tamanho, direita - esquerda + 1)
            soma_atual -= lista[esquerda]
            esquerda += 1

    return menor_tamanho if menor_tamanho != float("inf") else 0

print("Menor subvetor com soma igual a 7:", menor_subarray_com_soma_minima([2, 1, 5, 2, 3, 2], 7))

# Exemplo 3: Janela deslizante com CONJUNTO/CONTADOR - maior substring sem caracteres repetidos
def maior_substring_sem_repeticao(s):
    caracteres_na_janela = set()
    esquerda = 0
    maior_tamanho = 0

    for direita in range(len(s)):
        # Enquanto o caractere já estiver na janela, encolhe pela esquerda até removê-lo
        while s[direita] in caracteres_na_janela:
            caracteres_na_janela.remove(s[esquerda])
            esquerda += 1

        caracteres_na_janela.add(s[direita])
        maior_tamanho = max(maior_tamanho, direita - esquerda + 1)

    return maior_tamanho

print("Maior substring sem repetição:", maior_substring_sem_repeticao("abcabcbb"))

# VERSÕES QUE RETORNAM TAMBÉM O SUBVETOR QUE ATENDE AO REQUISITO

def soma_maxima_janela_fixa(lista, k):
    soma_atual = sum(lista[:k])
    soma_maxima = soma_atual
    inicio_melhor_janela = 0  # guarda o índice de início da melhor janela

    for i in range(k, len(lista)):
        soma_atual += lista[i] - lista[i - k]
        if soma_atual > soma_maxima:
            soma_maxima = soma_atual
            inicio_melhor_janela = i - k + 1  # início da nova janela após deslizar

    melhor_janela = lista[inicio_melhor_janela : inicio_melhor_janela + k]
    return soma_maxima, melhor_janela

print(soma_maxima_janela_fixa([2, 1, 5, 1, 3, 2], 3))

def menor_subarray_com_soma_minima(lista, alvo):
    esquerda = 0
    soma_atual = 0
    menor_tamanho = float("inf")
    melhor_esquerda, melhor_direita = -1, -1

    for direita in range(len(lista)):
        soma_atual += lista[direita]

        while soma_atual >= alvo:
            if direita - esquerda + 1 < menor_tamanho:
                menor_tamanho = direita - esquerda + 1
                melhor_esquerda, melhor_direita = esquerda, direita
            soma_atual -= lista[esquerda]
            esquerda += 1

    if menor_tamanho == float("inf"):
        return 0, []
    return menor_tamanho, lista[melhor_esquerda : melhor_direita + 1]

print(menor_subarray_com_soma_minima([2, 1, 5, 2, 3, 2], 7))

def maior_substring_sem_repeticao(s):
    caracteres_na_janela = set()
    esquerda = 0
    maior_tamanho = 0
    melhor_esquerda, melhor_direita = 0, 0

    for direita in range(len(s)):
        while s[direita] in caracteres_na_janela:
            caracteres_na_janela.remove(s[esquerda])
            esquerda += 1

        caracteres_na_janela.add(s[direita])

        if direita - esquerda + 1 > maior_tamanho:
            maior_tamanho = direita - esquerda + 1
            melhor_esquerda, melhor_direita = esquerda, direita

    return maior_tamanho, s[melhor_esquerda : melhor_direita + 1]

print(maior_substring_sem_repeticao("abcabcbb"))