import math

a, b, c = 29, 100, 11
# Teste de primalidade simples: verifica se um número isolado é primo, testando divisores até a raiz quadrada
def primalidade(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Só é necessário testar divisores ímpares até math.isqrt(n), pois se n tem um divisor maior que sua raiz, o divisor correspondente é menor que ela
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

print("29 é primo?", primalidade(a))  
print("100 é primo?", primalidade(b)) 

# Crivo de Eratóstenes: gera todos os números primos até N de forma eficiente (O(n log log n)), muito melhor que testar primalidade de cada número isoladamente
def crivo_eratostenes(n):
    # Cria uma lista booleana, assumindo inicialmente que todos os números são primos
    eh_primo_lista = [True] * (n + 1)
    eh_primo_lista[0] = eh_primo_lista[1] = False  # 0 e 1 não são primos

    for i in range(2, math.isqrt(n) + 1):
        if eh_primo_lista[i]:
            # Marca todos os múltiplos de i (a partir de i*i) como não primos
            # Começar em i*i é uma otimização: múltiplos menores já foram marcados por primos anteriores
            for multiplo in range(i * i, n + 1, i):
                eh_primo_lista[multiplo] = False

    return eh_primo_lista

# Uso do crivo: a lista retornada funciona como uma tabela de consulta O(1) para saber se um número é primo
limite = 50
primos_ate_limite = crivo_eratostenes(limite)
print(f"{a} é primo?", primos_ate_limite[a])
print(f"{c} é primo?", primos_ate_limite[c])  

# Extraindo a lista de números primos a partir da tabela booleana do crivo
lista_de_primos = [i for i in range(2, limite + 1) if primos_ate_limite[i]]
print("Lista de primos de 0 a 50:", lista_de_primos)

# Fatoração em números primos: decompõe um número em seus fatores primos, com suas respectivas potências
def fatorar(n):
    fatores = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            fatores[divisor] = fatores.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    # Se restou algum valor maior que 1, ele próprio é um fator primo (o último, maior que a raiz do n original)
    if n > 1:
        fatores[n] = fatores.get(n, 0) + 1
    return fatores

print("360 em fatores primos:", fatorar(360))

# Contagem de divisores de um número, a partir da fatoração (produto das potências + 1 de cada fator primo)
def quantidade_divisores(n):
    fatores = fatorar(n)
    resultado = 1
    for expoente in fatores.values():
        resultado *= (expoente + 1)
    return resultado

print("Quantidade de divisores de 360:", quantidade_divisores(360)) 

# Crivo de menor fator primo (smallest prime factor): variação do crivo que guarda, para cada número, seu menor fator primo
# Permite fatorar números repetidamente em O(log n), muito mais rápido que fatorar do zero a cada consulta
def crivo_menor_fator_primo(n):
    menor_fator = list(range(n + 1))  # inicialmente, cada número é seu próprio "menor fator"
    for i in range(2, math.isqrt(n) + 1):
        if menor_fator[i] == i:  # i ainda não foi marcado, logo é primo
            for multiplo in range(i * i, n + 1, i):
                if menor_fator[multiplo] == multiplo:
                    menor_fator[multiplo] = i
    return menor_fator

# Fatoração rápida usando a tabela de menor fator primo pré-computada
def fatorar_rapido(n, menor_fator):
    fatores = {}
    while n > 1:
        p = menor_fator[n]
        fatores[p] = fatores.get(p, 0) + 1
        n //= p
    return fatores

# Exemplo: reaproveitando a tabela para fatorar VÁRIOS números rapidamente
tabela_menor_fator = crivo_menor_fator_primo(1000)
for numero in [360, 100, 999, 512]:
    print(numero, "->", fatorar_rapido(numero, tabela_menor_fator))
    
# Crivo com marcação em intervalo (segmentado) não é abordado aqui, mas vale saber que existe
# para quando N é muito grande (ex: 10**12) e não cabe gerar o crivo completo até N

# Verificação de primalidade para números grandes isolados (quando gerar um crivo até N não é viável)
# usa o mesmo princípio da primalidade(), testando apenas até a raiz quadrada
print(primalidade(999999937))  # número grande, mas testado em tempo aceitável, O(sqrt(n))
# Gerar um crivo até 999999937 consumiria memória excessiva (quase 1 bilhão de posições)
# Por isso, para verificar um único número grande, o teste isolado O(sqrt(n)) é a abordagem correta