# Пошук стрічок, які починаються з 'From' на початку рядка 
#    і довільної кількості символів з 
#    подальшим двозначним числом від 00 до 99 і ':'
#    Потім роздрукуйте число, якщо воно є
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)
