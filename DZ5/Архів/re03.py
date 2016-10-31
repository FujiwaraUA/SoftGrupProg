# Пошук стрічок, які починаються з 'F', 
#    а потім 2-х символів, а потім 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)
