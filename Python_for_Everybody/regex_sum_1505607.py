import re
text = open('Regex/regex_sum_1505607.txt')
list = []
for line in text:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for num in numbers:
        list.append(int(num))

print(list,'\nThe Sum is: ', sum(list))