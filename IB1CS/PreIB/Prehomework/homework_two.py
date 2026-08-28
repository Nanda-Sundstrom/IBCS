#Homework 1
import math
a=f'{math.pi : .6f}'
print(a)
b=f'{2**100:.3g}'
print(b)
#Homework 2
c=input('give first integer')
d=input('give second integer')
e=f'{float(c):.0f}/{float(d):.0f} is (approximately) {float(c)/float(d):.3g}'
print(e)
#Homework 3
s='So it begins.'
f=f'len(s)'
g=f'{len(s)}'
h=f'{s[4]}{s[3]}'
i=s[len(s)//2]
print(s)
print(f)
print(g)
print(h)
print(i)
#Homework 4
j='this'
k='is'
l='great'
(j, k, l)=(l, j, k)
print(j,k,l)
#Homework 5
s='What a lovely day'
m=('z'in s, 'd' in s)
print(m)
k='this is a test'
n=('k' in k)
print(n)
#Homework 6
import math
o=(2**4, math.sqrt(2))
print(o)
import random
p= (random.randint(1, 6), random.randint(1,6))
print(p)