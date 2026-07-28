# Activity Selection: máximo de intervalos não sobrepostos
def selecao_de_atividades(intervalos):
    if not intervalos:
        return []

    # Passo chave: ordenar por FIM (não por início!)
    intervalos = sorted(intervalos, key=lambda x: x[1])

    selecionados = [intervalos[0]]
    ultimo_fim = intervalos[0][1]

    for inicio, fim in intervalos[1:]:
        if inicio >= ultimo_fim:
            # Compatível com o último selecionado -> escolhe
            selecionados.append((inicio, fim))
            ultimo_fim = fim
        # Senão, descarta esse intervalo (é gulosamente pior)

    return selecionados

intervalos = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (11, 14), (15, 16)]
resultado = selecao_de_atividades(intervalos)
print("Atividades possíveis:", resultado)
print("Quantidade máxima de atividades:", len(resultado))