# Пошук стрічок, які починаються 'X',
#    за яким слідують будь-які символи НЕ пробільні і ':',
#    тоді вивести першу групу після цього, 
#    що не є символами прогалин.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: (\S+)', line)
    if not x: continue
    print(x)
