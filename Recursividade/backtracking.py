# Backtracking: tenta uma escolha, avança recursivamente, e se necessário DESFAZ a escolha para tentar outra
# Padrão geral: escolher -> explorar -> desfazer
# Gerar todos os SUBCONJUNTOS de uma lista, implementado na mão (sem itertools)
def todos_subconjuntos(lista):
    resultado = []

    def backtrack(indice, subconjunto_atual):
        # Caso base: percorreu todos os elementos, salva uma cópia do subconjunto formado até aqui
        if indice == len(lista):
            resultado.append(subconjunto_atual.copy())
            return

        # Escolha 1: NÃO incluir o elemento atual, avança para o próximo
        backtrack(indice + 1, subconjunto_atual)

        # Escolha 2: incluir o elemento atual
        subconjunto_atual.append(lista[indice])
        backtrack(indice + 1, subconjunto_atual)
        subconjunto_atual.pop()  # desfaz a escolha (backtrack), para testar outros ramos sem o elemento atual

    backtrack(0, [])
    return resultado

print("Subconjuntos:", todos_subconjuntos([1, 2, 3]))

# Gerar todas as PERMUTAÇÕES de uma lista, implementado na mão (sem itertools)
def todas_permutacoes(lista):
    resultado = []

    def backtrack(permutacao_atual, restantes):
        # Caso base: não há mais elementos restantes, a permutação está completa
        if len(restantes) == 0:
            resultado.append(permutacao_atual.copy())
            return

        # Tenta cada elemento restante como o próximo da permutação
        for i in range(len(restantes)):
            elemento = restantes[i]

            # Escolhe o elemento: adiciona à permutação atual e remove dos restantes
            permutacao_atual.append(elemento)
            novos_restantes = restantes[:i] + restantes[i + 1:]

            backtrack(permutacao_atual, novos_restantes)

            # Desfaz a escolha (backtrack), para testar os outros elementos nessa posição
            permutacao_atual.pop()

    backtrack([], lista)
    return resultado

print("Permutações:", todas_permutacoes([1, 2, 3]))

# Problema das N-Rainhas: posicionar N rainhas em um tabuleiro NxN sem que nenhuma ataque a outra
# (não podem estar na mesma linha, coluna ou diagonal)
def n_rainhas(n):
    solucoes = []
    colunas_ocupadas = set()
    diagonais_principais = set()   # diferença (linha - coluna) é constante em uma diagonal principal
    diagonais_secundarias = set()  # soma (linha + coluna) é constante em uma diagonal secundária

    def backtrack(linha, posicoes_atuais):
        # Caso base: todas as linhas foram preenchidas com uma rainha válida
        if linha == n:
            solucoes.append(posicoes_atuais.copy())
            return

        for coluna in range(n):
            # Poda: verifica se a posição é válida ANTES de continuar (evita explorar ramos inválidos)
            if coluna in colunas_ocupadas or (linha - coluna) in diagonais_principais or (linha + coluna) in diagonais_secundarias:
                continue  # posição inválida, pula para a próxima coluna

            # Escolhe: marca a posição como ocupada
            colunas_ocupadas.add(coluna)
            diagonais_principais.add(linha - coluna)
            diagonais_secundarias.add(linha + coluna)
            posicoes_atuais.append(coluna)

            # Explora: avança para a próxima linha
            backtrack(linha + 1, posicoes_atuais)

            # Desfaz a escolha (backtrack), liberando a posição para outras tentativas
            colunas_ocupadas.remove(coluna)
            diagonais_principais.remove(linha - coluna)
            diagonais_secundarias.remove(linha + coluna)
            posicoes_atuais.pop()

    backtrack(0, [])
    return solucoes

solucoes_encontradas = n_rainhas(4)
print("Quantidade de soluções:", len(solucoes_encontradas))  # 2 soluções para um tabuleiro 4x4
print("Soluções:", solucoes_encontradas)  # cada solução é uma lista onde o índice é a linha e o valor é a coluna da rainha