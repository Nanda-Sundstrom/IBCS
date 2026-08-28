#Hw1
#1
#Fudamental: Adding & comparing values
#Compound: finding patterns in data & simulating actions
#2

#3


#Hw2
a=int(input('Please give a value: '))
b=int(input('Please give another value: '))
if a==b:
    n=(a+b)*(a+b) #squaring???
else:
    n=a+b
print(n)

#Hw3
#1
s=10
while s<=37:
    print(s, end=' ')
    s+=3
print()
#2 #thisshitiswrongsomehow
x=998
for y in range(50):
    print(x, end=' ')
    x-=2
print()
#3
for j in range(1, 21):
    if j%2==0:
        j=-1
    else:
        j=1
    print(j, end=' ')
print()
    
#4

#Hw4
cards=int(input("what is the value of your cards? "))

action=None #None??

if cards<17:
    action='hit'
elif cards>21:
    action='bust'
else: 
    action='stand'

print(action)

#Hw5
#1
c=int(input('Give an integer: '))
d=int(input('Give another integer: '))

if c>=100 and d<=50:
    output=1
else:
    output=0

print(output)

#2 the same one as #1?

#Hw6
#1
