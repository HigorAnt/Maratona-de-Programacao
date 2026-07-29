# Exemplo 1: MINIMIZAR - menor capacidade de um caminhão para entregar todos os pacotes em D dias
# Cada dia, o caminhão carrega pacotes em sequência até que a capacidade não permita mais,
# então segue para o próximo dia. Queremos a MENOR capacidade que ainda cumpre o prazo de D dias.

def dias_necessarios(pesos, capacidade):
    # Função de verificação: dado uma capacidade, quantos dias seriam necessários para entregar tudo?
    dias = 1
    carga_atual = 0

    for peso in pesos:
        if carga_atual + peso > capacidade:
            dias += 1          # não cabe mais no dia atual, começa um novo dia
            carga_atual = 0
        carga_atual += peso

    return dias

def menor_capacidade(pesos, dias_maximos):
    # O espaço de busca vai do maior pacote isolado (capacidade mínima teoricamente possível)
    # até a soma de todos os pesos (capacidade máxima, entregando tudo em 1 dia só)
    esquerda = max(pesos)
    direita = sum(pesos)

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if dias_necessarios(pesos, meio) <= dias_maximos:
            # Essa capacidade já é suficiente - tenta uma capacidade AINDA MENOR
            direita = meio
        else:
            # Não é suficiente - precisa de uma capacidade maior
            esquerda = meio + 1

    return esquerda  # menor capacidade viável encontrada

pesos_pacotes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Menor capacidade para entregar os pacotes em 5 dias:", menor_capacidade(pesos_pacotes, 5))

# Exemplo 2: MAXIMIZAR - problema clássico "Aggressive Cows"
# Dado um conjunto de estábulos em posições variadas na reta numérica, e uma quantidade de vacas,
# posicione as vacas de forma que a MENOR distância entre quaisquer duas vacas seja a MAIOR possível.
def cabe_vacas(estabulos, quantidade_vacas, distancia_minima):
    # Função de verificação: com essa distância mínima, é possível posicionar todas as vacas?
    vacas_posicionadas = 1
    posicao_ultima_vaca = estabulos[0]

    for posicao in estabulos[1:]:
        if posicao - posicao_ultima_vaca >= distancia_minima:
            vacas_posicionadas += 1
            posicao_ultima_vaca = posicao

    return vacas_posicionadas >= quantidade_vacas

def maior_distancia_minima(estabulos, quantidade_vacas):
    estabulos = sorted(estabulos)

    # O espaço de busca vai de distância 1 até a maior distância possível (extremos do intervalo)
    esquerda = 1
    direita = estabulos[-1] - estabulos[0]
    resposta = 0

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if cabe_vacas(estabulos, quantidade_vacas, meio):
            # Essa distância é viável - tenta uma distância AINDA MAIOR
            resposta = meio
            esquerda = meio + 1
        else:
            # Não é viável - precisa de uma distância menor
            direita = meio - 1

    return resposta

posicoes_estabulos = [1, 2, 4, 8, 9]
print("Maior distância mínima entre as vacas:", maior_distancia_minima(posicoes_estabulos, 3))