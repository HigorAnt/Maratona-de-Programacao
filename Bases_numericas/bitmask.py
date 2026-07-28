# Verifica se o bit i (0-indexed, da direita p/ esquerda) está ligado. O(1).
def bit_ligado(n: int, i: int) -> bool:
    return (n & (1 << i)) != 0

# Liga o bit i, sem afetar os demais. O(1).
def ligar_bit(n: int, i: int) -> int:
    
    return n | (1 << i)

# Desliga o bit i, sem afetar os demais. O(1).
def desligar_bit(n: int, i: int) -> int:
    return n & ~(1 << i)

# Inverte (toggle) o bit i: liga se estava desligado, desliga se estava ligado. O(1).
def inverter_bit(n: int, i: int) -> int:
    return n ^ (1 << i)

# Isola o bit ligado menos significativo (mais à direita). Usado em Fenwick Tree. O(1).
def isolar_bit_menos_significativo(n: int) -> int:
    return n & (-n)

#Conta quantos bits estão ligados (popcount).
# Em Python 3.10+, prefira n.bit_count() -- implementado em C, mais rápido que bin(n).count("1"), que precisa construir uma string primeiro.
def contar_bits_ligados(n: int) -> int:
    return n.bit_count()  # fallback para versões antigas: bin(n).count("1")

# Enumerar todos os subconjuntos de um conjunto via bitmask
# Gera todos os 2^n subconjuntos de 'itens' usando máscaras de bits.
# Cada máscara de 0 a 2^n - 1 representa um subconjunto único.
# Tempo: O(n * 2^n). Viável até n ~ 20.
def todos_subconjuntos_bitmask(itens: list) -> list[list]:
    n = len(itens)
    subconjuntos = []
    for mascara in range(1 << n):
        subconjunto = [itens[i] for i in range(n) if mascara & (1 << i)]
        subconjuntos.append(subconjunto)
    return subconjuntos

# Iterar apenas os SUBMÁSCARAS de uma máscara (submasks enumeration)
# Técnica avançada: útil quando o problema pede algo como "para cada subconjunto, itere sobre todos os seus sub-subconjuntos"
# Gera, em ordem decrescente, todas as submáscaras de 'mascara' (incluindo 0 e a própria máscara). 
# Tempo total sobre todas as máscaras de n bits: O(3^n), bem melhor que o O(4^n) ingênuo de testar todo par (mascara, sub) separadamente.
def submascaras(mascara: int):
    sub = mascara
    while True:
        yield sub
        if sub == 0:
            break
        sub = (sub - 1) & mascara

if __name__ == "__main__":
    # Verificação de bits individuais
    n = 12
    print(bit_ligado(n, 2))
    print(bit_ligado(n, 0))

    print(bin(ligar_bit(n, 0)))
    print(bin(desligar_bit(n, 2)))
    print(bin(inverter_bit(n, 1)))

    print(isolar_bit_menos_significativo(12))
    print(contar_bits_ligados(12))

    # Enumeração de subconjuntos
    print(todos_subconjuntos_bitmask([1, 2, 3]))

    # Enumeração de submáscaras
    print(list(submascaras(0b101)))