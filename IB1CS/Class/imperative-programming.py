a=15
b=22
print(a,b) 
print(a-b) 
print(f'ratio of a and b is {a/b}') 
print((3*a)%(2*b)) #3a/2b remainder
print(45/44)
print(45%44)
print(a**b) #to the power of 
name="foo"
last="bar"
print(name," ",last)
import math
print(math.pi)

import dis # import module for showing bytecode

# function finding the sum
def fun():
    s = 0
    for i in range(5, 16):
        s += i
    return s

# disassemble the bytecode of the function
dis.dis(fun)

s= int(input('please give the value of S: ')) #Whathefuckisthis example 7

n=1
found=False

while found==False:
    if n*(n+1)/2>s:
        found= True
    else:
        n+=1

print(n)

#example 2
mark=int(input('please give mark: '))
if mark>=90:
    grade=10
elif mark>=70:
    grade=9
else: 
    grade=8

print('grade is', grade)

#example 3
x=int(input('please give a positive integer: '))
if x>0:
    p=1 #product
    k=x
    while k>=1: #or just k>1 idk bro
        p*=k #so p=p*k
        k-=1 #so k=k-1
    print(f'{x}! = {p}')
else:
    print('given integer is not positive')

#example 4 copypasted from ex.3
y=int(input('please give a positive integer: '))
if y>0:
    p=1 #product
    for k in range(2, y+1): #n+1 so that last value is n
        p*=k #so p=p*k
    print(f'{y}! = {p}')
else:
    print('given integer is not positive')

#example 5
v=9 #1
while v<=65: #v=value
    print(v, end=' ')
    v+=4
print()

c=3 #2
for x in range(13): #meaning 13 numbers
    print(c, end=' ')
    c*=2
print()

for d in range(1, 41): #3
    m=d
    if d%4==0: #== doesn't assign a value its just a true/false thing
        m= -1
    print(m, end=' ')
print()

#example 6
smallest=0
largest=0

for e in range(51):
    value=e*(e-30)*(e-50)
    if value<smallest:
        smallest=value
    if value>largest:
        largest=value

print(smallest, largest)