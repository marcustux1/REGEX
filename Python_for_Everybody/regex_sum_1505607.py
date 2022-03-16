# IMPORTA O MÓDULO REGEX
import re

# ARMAZENA O ARQUIVO DENTRO DE UMA VARIÁVEL
text = open('regex_sum_1505607.txt')

# CRIA UMA LISTA VAZIA QUE RECEBERÁ OS NÚMEROS ENCONTRADOS NO TEXTO
list = []

# ACESSANDO CADA LINHA DO TEXTO, E BUSCANDO VIA EXPRESSÃO TEXTO QUE CASE COM O SOLICITADO
for line in text:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for num in numbers:
        list.append(int(num))
        
# IMPRIME A LISTA DE NÚMEROS E A SOMA
print(list,'\nThe Sum is: ', sum(list))
