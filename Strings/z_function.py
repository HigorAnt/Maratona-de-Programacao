# Calcula a Z-function de 's' em O(n). 
# z[i] = tamanho do maior prefixo de s que também é prefixo de s[i:]. z[0] não tem significado útil (definido como 0 aqui).
def z_function(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    l, r = 0, 0  # janela [l, r) do prefixo coincidente mais à direita já conhecido

    for i in range(1, n):
        if i < r:
            # aproveita o valor já calculado da posição espelhada
            z[i] = min(r - i, z[i - l])

        # tenta estender além do que já foi aproveitado
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # atualiza a janela se este prefixo coincidente foi o mais à direita até agora
        if i + z[i] > r:
            l, r = i, i + z[i]

    return z

# Busca todas as ocorrências de 'padrao' em 'texto' usando Z-function. Retorna índices 0-based relativos ao 'texto'
# Tempo: O(n + m). Espaço: O(n + m)
def busca_com_z(texto: str, padrao: str) -> list[int]:
    m = len(padrao)
    if m == 0 or m > len(texto):
        return []

    sep = '\x00'  # caractere de separação garantidamente ausente em texto/padrao
    combinada = padrao + sep + texto
    z = z_function(combinada)

    ocorrencias = []
    offset = m + 1  # posição onde o texto começa dentro de 'combinada'
    for i in range(offset, len(combinada)):
        if z[i] == m:
            ocorrencias.append(i - offset)

    return ocorrencias

def main():
    texto = "ababcababcabc"
    padrao = "abc"
    retorno = busca_com_z(texto, padrao)
    print("Quantidade de ocorrências:", len(retorno))
    print("Ocorrências:", retorno)

main()