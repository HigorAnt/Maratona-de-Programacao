import statistics

dados = [4, 8, 15, 16, 23, 42, 8, 4]

# mean(): calcula a média aritmética do conjunto de dados
print("Média =", statistics.mean(dados))

# median(): calcula a mediana - ordena os dados internamente antes de calcular
print("Mediana =", statistics.median(dados)) 

# Com quantidade PAR de elementos, a mediana é a média dos dois valores centrais
dados_pares = [1, 2, 3, 4]
print("Mediana =", statistics.median(dados_pares))

# mode(): retorna o valor mais frequente do conjunto, em caso de empate retorna só o primeiro encontrado
print("Moda =", statistics.mode(dados))

# multimode(): retorna TODOS os valores mais frequentes
print("Moda =", statistics.multimode(dados)) 

# pvariance(): variância POPULACIONAL, divide pela quantidade total de dados (n)
print("Variância populacional =", statistics.pvariance(dados))

# variance(): variância AMOSTRAL, divide por (n - 1)
print("Variância amostral =", statistics.variance(dados)) 

# pstdev(): desvio padrão POPULACIONAL (raiz quadrada da variância populacional)
print("Desvio padrão populacional =", statistics.pstdev(dados))

# stdev(): desvio padrão AMOSTRAL (raiz quadrada da variância amostral)
print("Desvio padrão amostral =", statistics.stdev(dados))

# Implementação manual da média
def media_manual(valores):
    return sum(valores) / len(valores)

print("Média manual =", media_manual(dados)) 

# Implementação manual do desvio padrão populacional
def desvio_padrao_manual(valores):
    media = media_manual(valores)
    soma_dos_quadrados = sum((x - media) ** 2 for x in valores)
    variancia = soma_dos_quadrados / len(valores)
    return variancia ** 0.5

print("Desvio padrão populacional manual =", desvio_padrao_manual(dados)) 