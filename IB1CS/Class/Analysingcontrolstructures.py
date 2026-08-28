#Ex1
a=int(input('please give a '))
b=int(input('please give b '))
c=int(input('please give c '))
ab=a - b
ac=a-c
bc=b-c

if ab*bc>0:
    result=b
elif ab*ac<0:
    result=a
else:
    result=c

print(result)

#Ex2
x=int(input('x: '))
y=int(input('y: '))

result=1
while y>0:
    if y%2==0:
        y/=2
        x=x**2
    else:
        y-=1
        result*=x

print(result)