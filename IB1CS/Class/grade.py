#example 2?
mark=int(input('please give mark: '))
if mark>=90:
    grade=10
elif mark>=70:
    grade=9
else: 
    grade=8

print('grade is', grade)

#example 3
n=int(input('please give a positive integer: '))
if n>0:
    p=1 #product
    k=n
    while k>=1: #or just k>1 idk bro
        p*=k #so p=p*k
        k-=1 #so k=k-1
    print(f'{n}! = {p}')
else:
    print('given integer is not positive')

#example 4 copypasted from ex.3
n=int(input('please give a positive integer: '))
if n>0:
    p=1 #product
    for k in range(2, n+1): #n+1 so that last value is n
        p*=k #so p=p*k
    print(f'{n}! = {p}')
else:
    print('given integer is not positive')

#example 5
v=9 #1
while v<=65: #v=value
    print(v, end=' ')
    v+=4
print()

a=3 #2
for x in range(13): #meaning 13 numbers
    print(a, end=' ')
    a*=2
print()

for y in range(1, 41): #3
    m=y
    if y%4==0: #== doesn't assign a value its just a true/false thing
        m= -1
    print(m, end=' ')
print()

#example 6
smallest=0
largest=0

for b in range(51):
    value=b*(b-30)*(b-50)
    if value<smallest:
        smallest=value
    if value>largest:
        largest=value

print(smallest, largest)