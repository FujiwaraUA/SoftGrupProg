from functools import reduce
# D. Сума цифр в числі 100!
# n! означає n * (n-1) * ... * 3 * 2 * 1
# Знайдіть суму цифр в числі 100!
n = 100
l = [i for i in range(1,101)]
fact_n = reduce(lambda a,b: a * b, l)
print(sum([int(i) for i in str(fact_n)]))