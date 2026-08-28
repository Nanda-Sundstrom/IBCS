#Homework 1
#1
for a in range(7):
    print(a**3, end= ' ')
print('A')
#2
for b in range(37, 4, -1):
    if b%2 != 0:
        print(b, end= ' ')
print('B')
#3
for c in range(21):
    if c%3 == 0:
        print('a', end= ' ')
    elif (1+c)%3 == 0:
        print('c', end= ' ')
    else:
        print('b', end= ' ')
print('C')

#Homework 2
d = str(input('please give a string: '))
e= enumerate(d)
print(e)

#Homework 3
#1
import random
