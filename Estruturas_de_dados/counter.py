from collections import Counter

# Cria um Counter a partir de um iterável (lista, string, etc), contando automaticamente as ocorrências de cada elemento
minha_lista = [1, 2, 2, 3, 3, 3, 4]
contagem = Counter(minha_lista)
print("Ocorrência de cada elemento:", contagem) 

# Funciona também diretamente em strings, contando cada caractere
contagem_string = Counter("abracadabra")
print("Ocorrência de cada caracter:", contagem_string)

# Criação a partir de entrada do usuário
entrada = input("Digite números separados por espaço: ")
contagem_entrada = Counter(entrada.split())
print("Ocorrência de cada elemento:", contagem_entrada)

# Counter também pode ser criado a partir de um dicionário já pronto
contagem_manual = Counter({"a": 3, "b": 1})
print(contagem_manual)

# Acessa a contagem de um elemento como se fosse um dicionário
print(contagem["3"] if "3" in contagem else contagem[3])

# Diferente de um dicionário comum, acessar uma chave inexistente NÃO gera erro: retorna 0
print(contagem[999])

# most_common(): retorna todos os elementos ordenados do mais frequente para o menos frequente, como lista de tuplas (elemento, contagem)
print("Ocorrência ordenada dos elementos:", contagem.most_common())

# most_common(n): retorna apenas os n elementos mais frequentes
print("Elementos mais freuqentes:", contagem.most_common(2))

# Incrementa a contagem de um elemento manualmente (soma 1 ao valor atual, criando a chave se não existir)
contagem[10] += 1
print(contagem)

# update(iteravel): adiciona novas ocorrências às contagens já existentes, em vez de substituir
contagem.update([1, 1, 2])
print("Ocorrências com adição do [1, 1, 2]:", contagem)

# subtract(iteravel): subtrai ocorrências das contagens existentes (pode gerar valores negativos)
contagem.subtract([1, 1])
print("Ocorrências com eliminação do [1, 1]:", contagem)

# elements(): retorna um iterador que repete cada chave de acordo com sua contagem (contagens <= 0 são ignoradas)
c = Counter(a=3, b=1, c=0)
print("Resultado da iretação:", list(c.elements())) 

# Operações aritméticas entre dois Counters: soma, subtração, interseção (mínimo) e união (máximo)
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print("Soma das contagens:", c1 + c2) 
print("Subtração das contagens:", c1 - c2)  # remove resultados <= 0
print("Menor valor de cada chave:", c1 & c2) 
print("Maior valor de cada chave:", c1 | c2)  

# total(): retorna a soma de todas as contagens (disponível a partir do Python 3.10)
print("Soma de todas as contagens:", contagem_string.total())

# Convertendo de volta para dicionário comum, se necessário
dict_normal = dict(contagem_string)
print(dict_normal)

# Exemplo prático: encontrar o elemento mais frequente de uma lista
def mais_frequente(lista):
    return Counter(lista).most_common(1)[0][0]

print("Elemento mais frequente:", mais_frequente([1, 3, 3, 2, 3, 1])) 