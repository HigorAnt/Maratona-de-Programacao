# Subsequência comum mais longa (LCS)
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

a = "ABCBDAB"
b = "BDCABA"
print("Maior subsequência:", lcs(a, b))

# Reconstruindo a subsequência (não só o tamanho)
def lcs_com_sequencia(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Percorre a tabela de trás para frente para reconstruir a subsequência
    i, j = n, m
    resultado = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            resultado.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[n][m], "".join(reversed(resultado))

tamanho, subsequencia = lcs_com_sequencia(a, b)
print("Maior subsequência:", tamanho, subsequencia)

# LCS com memoização (top-down), como alternativa à tabulação
from functools import lru_cache

def lcs_memo(a, b):
    @lru_cache(maxsize=None)
    def resolve(i, j):
        if i == len(a) or j == len(b):
            return 0
        if a[i] == b[j]:
            return 1 + resolve(i + 1, j + 1)
        return max(resolve(i + 1, j), resolve(i, j + 1))

    return resolve(0, 0)

print("Maior subsequência:", lcs_memo(a, b))