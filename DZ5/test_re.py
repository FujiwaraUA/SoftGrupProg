# -*- coding: utf-8 -*-

# 1. Написати просту програму для імітації роботи команди  Unix - grep.
# (Програма командного рядка, вбудована в Unix називається grep
# (Generalized Regular Expression Parser), що робить майже таке саме,
# як приклади з search().)
#
# Попросіть користувача ввести регулярний вираз і підрахувати кількість рядків,
# які відповідають регулярному виразу:
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
#
# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-
#
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

import re

def zavdanna1():
    filename = input('Enter a file name: ')
    pattern = input('Enter a regular expression: ')
    fail1 = open(filename)
    n = 0

    for line in fail1:
        if re.search(pattern, line):
            print(line)
            n += 1
    print(' {0} had {1} lines that matched {2}'.format(filename, n, pattern))

zavdanna1()