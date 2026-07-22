# Lista de strings a serem concatenadas
palavras = ["Vitor", "Emanoel", "de", "Sousa"]

# FORMA INEFICIENTE: concatenar com += dentro de um loop
# Como strings são imutáveis, cada += cria uma string NOVA na memória e descarta a anterior
# ou seja, a cada iteração o Python copia tudo que já foi construído até ali
# Para N palavras, isso resulta em complexidade O(n²) no pior caso, não O(n)
resultado_ineficiente = ""
for palavra in palavras:
    resultado_ineficiente += palavra + " "
print("String gerada ineficientemente:", resultado_ineficiente)

# FORMA EFICIENTE: acumular as partes em uma lista e juntar tudo de uma vez no final com join()
# append() em lista é O(1) amortizado, e join() percorre as partes uma única vez
# o processo inteiro fica O(n), proporcional ao tamanho total do texto
partes = []
for palavra in palavras:
    partes.append(palavra)
resultado_eficiente = " ".join(partes)
print("String gerada eficientemente:", resultado_eficiente)  # 'maratona de programacao'

# A mesma lógica vale para transformações caractere a caractere: gerar uma string nova caractere por caractere com += também é ineficiente pelo mesmo motivo
frase_original = "Maratona de Programacao"

# Nesse caso, uma expressão geradora dentro do join() resolve com boa performance
maiuscula = "".join(c.upper() for c in frase_original)
print(maiuscula) 
# Regra prática: sempre que for construir uma string dentro de um loop com muitas repetições,
# prefira acumular em uma lista (ou usar uma expressão geradora) e chamar join() apenas no final