# Verificação de sobreposição e interseção entre dois intervalos
def sobrepoe(intervalo1, intervalo2):
    a1, b1 = intervalo1
    a2, b2 = intervalo2
    return a1 <= b2 and a2 <= b1

def intersecao(intervalo1, intervalo2):
    a1, b1 = intervalo1
    a2, b2 = intervalo2
    if not sobrepoe(intervalo1, intervalo2):
        return None
    return (max(a1, a2), min(b1, b2))

print("Sobreposição de (1, 5)-(4, 8):", sobrepoe((1, 5), (4, 8)))
print("Sobreposição de (1, 5)-(6, 8):", sobrepoe((1, 5), (6, 8))) 
print("Sobreposição de (1, 5)-(4, 8):", sobrepoe((1, 5), (5, 8))) 
print("Interseção de (1, 5), (4, 8):", intersecao((1, 5), (4, 8)))
print("Interseção de (1, 5), (6, 8):", intersecao((1, 5), (6, 8)))