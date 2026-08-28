a=str(input('Give a string: '))
for (b,c) in enumerate(a):
    if b%2==1:
        print(c, end=' ')
