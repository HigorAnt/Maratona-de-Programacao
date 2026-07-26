# Retorna (g, x, y) tais que a*x + b*y = g = gcd(a, b). Implementação iterativa para evitar overhead de recursão em Python.
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t  # g, x, y

# Combina x ≡ a1 (mod m1) e x ≡ a2 (mod m2) em uma única congruência 
# x ≡ a (mod m), com m = mmc(m1, m2). Funciona mesmo se m1, m2 não
# forem coprimos (CRT generalizado); retorna None se não houver solução.
def crt_combinar(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int] | None:
    g, p, _ = extended_gcd(m1, m2)

    if (a2 - a1) % g != 0:
        return None  # sistema incompatível, sem solução

    lcm = m1 // g * m2
    # x = a1 + m1 * t, onde t é escolhido para satisfazer a segunda congruência
    tmp = (a2 - a1) // g * p % (m2 // g)
    x = (a1 + m1 * tmp) % lcm

    return x, lcm

# Resolve um sistema de congruências [(a1, m1), (a2, m2), ...].
# Retorna (x, M) onde x é a solução única módulo M, ou None se o sistema for incompatível.
# Tempo: O(k log(max(m_i))).
def crt(congruencias: list[tuple[int, int]]) -> tuple[int, int] | None:
    x, m = congruencias[0]
    x %= m

    for a, mod in congruencias[1:]:
        resultado = crt_combinar(x, m, a % mod, mod)
        if resultado is None:
            return None
        x, m = resultado

    return x, m

if __name__ == "__main__":
    # x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7) -> x = 23
    print(crt([(2, 3), (3, 5), (2, 7)]))

    # Módulos não coprimos, mas compatíveis: x ≡ 4 (mod 6), x ≡ 4 (mod 10)
    print(crt([(4, 6), (4, 10)]))

    # Sistema incompatível
    print(crt([(1, 4), (2, 6)]))