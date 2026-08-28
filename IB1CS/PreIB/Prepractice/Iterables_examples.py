#1
for n in range(10):
    print(n, end=' ')
print('A')
#2
for a in range(10,0,-1):
    print(a, end=' ')
print('B')
#3
for b in range(1, 16, 2): #1, 3, ..., 15
    print(b**2, end=' ')
print('C')
#4
for j in range(14): #0, 1, ..., 13 (every other even and odd like x0,y1,x2,y3,x4,y5)
    if j % 2 == 0:
        print('x', end= ' ')
    else: 
        print('y', end= ' ')
print('D')
#OR
for d in range(14): #0, 1, ..., 13 (every other even and odd like x0,y1,x2,y3,x4,y5)
    if d % 2 == 0:
        d='x'
    else: 
        d='y'
    print(d, end = ' ')
print('E')
#EXAMPLE 2 (5/14)
guess=int(input('give a positive integer: '))
is_prime= True
for f in range(2,guess):
    if guess % f == 0:
        is_prime= False
        break
if is_prime:
    result= 'number is a prime'
else:
    result='number is not a prime'
print(result)
#EXAMPLE 3 (7/14)
import random
count = 0
p=1000000
for k in range(p):
    u= random.random()
    v= random.random()
    if u**2 + v**2 <1:
        count+=1
print(count)
print(count / p*4) #approximate pi
#EXAMPLE 4 (9/14)
string=input('please give text: ').strip()
for (i, c) in enumerate(string):
    if c == ' ':
        print(string[i - 1], string[i + 1])