#    Потім перетворіть ці цифри в число з плаваючою комою 
#    і додайте його до nums
#    Нарешті роздрукувати кількість цих чисел і 
#    середнє арифметичне цих чисел
import re
fname = input('Enter file:')
hand = open('mbox-short.txt')
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
print(len(nums))
print(sum(nums)/len(nums))
