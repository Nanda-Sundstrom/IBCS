a=input('Give a string: ')
b=input('Give another one: ')
count=0
for (c,d) in zip(a,b):
    if c == d:
        count= count+1
print(count)