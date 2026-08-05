from bisect import bisect_left

# Versao 1: retorna apenas o tamanho da LIS
def lis_tamanho(v):
    tails = []

    for x in v:
        # bisect_left encontra a primeira posição em "tails" onde x poderia ser inserido mantendo a ordem crescente
        pos = bisect_left(tails, x)

        if pos == len(tails):
            # x é maior que todos os valores em tails -> aumenta o tamanho da maior subsequência encontrada ate agora
            tails.append(x)
        else:
            # x substitui o valor em tails[pos], pois x é menor ou igual -> mantem tails com os "melhores" (menores) valores finais possiveis para cada tamanho
            tails[pos] = x

    # o tamanho da LIS é simplesmente o tamanho final de tails
    return len(tails)

# Versao 2: retorna o tamanho e a sequência reconstruída
def lis_com_sequencia_otimizada(v):
    n = len(v)
    tails = [] # valores (igual a versao 1)
    tails_idx = [] # índices dos elementos em "tails"
    anterior = [-1] * n # índice do predecessor de cada elemento

    for i, x in enumerate(v):
        pos = bisect_left(tails, x)

        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos] = x
            tails_idx[pos] = i

        # se x não é o primeiro elemento de uma subsequência, seu predecessor e o elemento que estava logo antes dele em "tails" (posição pós - 1) no momento da inserção
        if pos > 0:
            anterior[i] = tails_idx[pos - 1]

    # reconstroi a sequência "andando para trás" a partir do último índice guardado em tails_idx (fim da LIS)
    tamanho = len(tails)
    sequencia = []
    idx = tails_idx[-1]

    while idx != -1:
        sequencia.append(v[idx])
        idx = anterior[idx]

    sequencia.reverse() # foi construída de trás para frente

    return tamanho, sequencia

if __name__ == "__main__":
    v = [10, 9, 2, 5, 3, 7, 101, 18]
    tamanho, sequencia = lis_com_sequencia_otimizada(v)

    print("Tamanho da LIS:", lis_tamanho(v))
    print("Tamanho da LIS (com reconstrução):", tamanho)
    print("Sequencia:", sequencia)