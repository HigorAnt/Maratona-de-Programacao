# Calcula o array de falha (prefix function) de 'padrao' em O(m)
# pi[i] = tamanho do maior prefixo próprio de padrao[0..i], que também é sufixo de padrao[0..i]
def prefix_function(padrao: str) -> list[int]:
    m = len(padrao)
    pi = [0] * m
    k = 0
    for i in range(1, m):
        ci = padrao[i]
        while k > 0 and ci != padrao[k]:
            k = pi[k - 1]
        if ci == padrao[k]:
            k += 1
        pi[i] = k
    return pi

# Retorna os índices (0-based) onde 'padrao' ocorre em 'texto'
# Tempo: O(n + m). Espaço: O(m) além da entrada
def kmp_busca(texto: str, padrao: str) -> list[int]:
    m = len(padrao)
    if m == 0 or m > len(texto):
        return []

    pi = prefix_function(padrao)
    ocorrencias = []
    k = 0

    for i, c in enumerate(texto):
        while k > 0 and c != padrao[k]:
            k = pi[k - 1]
        if c == padrao[k]:
            k += 1
        if k == m:
            ocorrencias.append(i - m + 1)
            k = pi[k - 1]  # continua buscando sobreposições

    return ocorrencias

def main():
    texto = "ababcababcabc"
    padrao = "abc"
    retorno = kmp_busca(texto, padrao)
    print("Quantidade de ocorrências:", len(retorno))
    print("Índice das ocorrências:", retorno)

main()