# Definindo uma string de exemplo
nome = "Dagoberto"

# Acesso a um caractere por índice positivo (semelhante a um vetor)
print("Primeiro caracter:", nome[0])  

# Índice negativo acessa a partir do final da string (-1 é sempre o último caractere)
print("Último caracter:", nome[-1])

# Fatiamento no formato [inicio:fim] retorna uma substring do índice inicio até fim-1
print("Nome fatiado:", nome[0:4])  

# Omitir o início ou o fim faz o fatiamento ir até a borda correspondente da string
print(nome[:4])  
print(nome[4:]) 

# Fatiamento com passo [inicio:fim:passo] pula caracteres de acordo com o passo informado
print("String pulando caracteres com passo 2:", nome[::2])

# Passo negativo percorre a string de trás para frente; com [::-1], obtemos a string invertida
print("String inverdida:", nome[::-1]) 

# len(): retorna a quantidade de caracteres da string
print(f"O nome tem {len(nome)} caracteres")  

# Strings são imutáveis em Python: não é possível alterar um caractere específico por atribuição direta
# palavra[0] = "M"  # gera TypeError: 'str' object does not support item assignment
# Para "alterar" uma string, é preciso construir uma NOVA string a partir de partes da original
novo_nome = "João" + nome[4:]
print("Novo nome:", novo_nome) 

# Cada fatiamento ou concatenação acima cria uma nova string na memória, sem modificar a original 