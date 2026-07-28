# Merge de intervalos sobrepostos
def merge_interv(intervalos):
    if not intervalos:
        return []

    # Passo 1: ordenar por início
    intervalos = sorted(intervalos, key=lambda x: x[0])

    mesclados = [intervalos[0]]

    for inicio, fim in intervalos[1:]:
        ultimo_inicio, ultimo_fim = mesclados[-1]

        if inicio <= ultimo_fim:
            # Há sobreposição (ou encostam exatamente) -> funde
            mesclados[-1] = (ultimo_inicio, max(ultimo_fim, fim))
        else:
            # Não sobrepõe -> começa um novo grupo
            mesclados.append((inicio, fim))

    return mesclados

intervalos = [(5, 10), (1, 3), (8, 9), (2, 6), (15, 18)]
print(f"Intervalos: {intervalos}")
print("Merge de intervalos sobrepostos:", merge_interv(intervalos))