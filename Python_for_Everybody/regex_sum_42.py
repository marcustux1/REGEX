import re
texto = open('Regex/regex_sum_42.txt')
lista = []
for line in texto:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for num in x:
        lista.append(int(num))

print(sum(lista))