# Пошук стрічок, які починаються 'X',
#    за яким слідують будь-які символи НЕ пробільні і ':',
#    потім пробіл і будь-яке число. 
#    Число може включати десяткову крапку.

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
