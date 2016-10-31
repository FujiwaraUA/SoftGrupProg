# -*- coding: utf-8 -*-
# 5. В середині

s = 'a b c d e f'
dov_na2 = len(s) // 2
s3 = s[2:dov_na2 + 1] + s[:2] + s[-1] + ' ' + s[dov_na2 + 1:-2]
print(s3)
