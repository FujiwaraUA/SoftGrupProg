# Пошук стрічок, що містять слово 'Author:',
#    за яким слідують будь-які символи, знак @, і будь-який 
#    не пробільний символ
#    Потім надрукувати символи групи, яка слідує за символом
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Author:.*@(\S+)', line)
    if not x: continue
    print(x)
