# Retorna o maior substring palindrômico de 's' em O(n)
# Usa a transformação com separadores para unificar centros pares e ímpares, evitando dois algoritmos separados
def manacher(s: str) -> str:
    if len(s) < 2:
        return s

    # Transforma "abc" em "^#a#b#c#$"
    # '^' e '$' são sentinelas para evitar checagem de limites no while
    t = ['^']
    for c in s:
        t.append('#')
        t.append(c)
    t.append('#')
    t.append('$')

    n = len(t)
    raio = [0] * n
    centro = direita = 0

    for i in range(1, n - 1):
        espelho = 2 * centro - i

        if i < direita:
            raio[i] = min(direita - i, raio[espelho])

        # tenta expandir além do que já foi aproveitado por simetria
        while t[i + raio[i] + 1] == t[i - raio[i] - 1]:
            raio[i] += 1

        # atualiza o centro/direita se este palíndromo foi o mais à direita até agora
        if i + raio[i] > direita:
            centro, direita = i, i + raio[i]

    # encontra o maior raio e reconstrói a resposta na string original
    max_raio, centro_max = max((r, i) for i, r in enumerate(raio))
    inicio = (centro_max - max_raio) // 2  # converte índice da string transformada de volta
    return s[inicio: inicio + max_raio]

def main():
    print("Maior substring palíndromo em 'babad':", manacher("babad"))
    print("Maior substring palíndromo em 'cbbd':", manacher("cbbd"))
    print("Maior substring palíndromo em 'a':", manacher("a"))
    print("Maior substring palíndromo em '':", manacher(""))

main()