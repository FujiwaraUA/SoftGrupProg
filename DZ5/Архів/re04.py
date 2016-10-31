# Пошук стрічки, які починаються з From 
#   і мають ще один довільний символ перед @
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
