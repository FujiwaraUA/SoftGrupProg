# -*- coding: utf-8 -*-


import sys
import re

filename = 'babynames_girls.html'

def extract_names(filename):
    f = open(filename)
    while True:
        line = f.readline().encode()
        if len(line) == 0:
            break
        print(line)




extract_names(filename)