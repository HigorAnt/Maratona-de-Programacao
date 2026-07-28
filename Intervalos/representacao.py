# Representação e ordenação de intervalos
# Um intervalo é representado como uma tupla (inicio, fim)
intervalos = [(5, 10), (1, 3), (1, 2), (8, 9), (2, 6), (15, 18)]

# 1) Ordenar por início (uso mais comum: merge de sobrepostos, sweep de eventos)
por_inicio = sorted(intervalos, key=lambda x: x[0])
print("Ordenado por início:", por_inicio)

# 2) Ordenar por fim (uso mais comum: greedy de seleção de atividades)
por_fim = sorted(intervalos, key=lambda x: x[1])
print("Ordenado por fim:", por_fim)

# Observação: sorted() em tupla, sem key, já ordena por inicio e depois por fim como desempate (ordem lexicográfica):
padrao = sorted(intervalos)
print("Ordenação padrão (lexicográfica):", padrao)