a=enumerate('hello')
print(a)

b=str(input('Give a string: '))
for (i,c) in enumerate(b):
    if c==' ':
        print(b[i-1], b[i+1])
