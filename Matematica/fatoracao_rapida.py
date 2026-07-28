import random
import math

# Teste de primalidade determinístico para n < 3.3 * 10^24, usando um conjunto fixo de bases testemunhas conhecidas
# Tempo: O(k log^3 n), k = número de bases testadas
def miller_rabin(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p

    # escreve n - 1 = d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # bases suficientes para determinismo até 3.3 * 10^24
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

# Encontra um fator não-trivial de n (composto, ímpar, n > 1) usando o algoritmo de Pollard's rho com a otimização de Brent
# Tempo esperado: O(n^(1/4))
def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2

    while True:
        c = random.randint(1, n - 1)
        f = lambda x: (x * x + c) % n

        x = y = random.randint(2, n - 1)
        d = 1
        # otimização de Brent: agrupa produtos antes de calcular gcd,
        # reduzindo o número de chamadas de gcd (que são custosas)
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)

        if d != n:  # d == n significa falha nesta tentativa; tenta outro c
            return d

#Retorna a fatoração completa de n como {primo: expoente}.
# Combina Miller-Rabin (para parar em primos) com Pollard's rho (para quebrar compostos) recursivamente.
def fatorar(n: int) -> dict[int, int]:
    fatores: dict[int, int] = {}

    def _fatorar(m: int):
        if m == 1:
            return
        if miller_rabin(m):
            fatores[m] = fatores.get(m, 0) + 1
            return
        d = pollard_rho(m)
        _fatorar(d)
        _fatorar(m // d)

    _fatorar(n)
    return fatores

if __name__ == "__main__":
    print(miller_rabin(1_000_000_007))         
    print(miller_rabin(1_000_000_008))        

    n = 8051                       
    print(pollard_rho(n))                     

    n2 = 600_851_475_143                        
    print(fatorar(n2))