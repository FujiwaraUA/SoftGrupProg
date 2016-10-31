# Пошук стрічок, що містять 'From' на початку стрічки
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
