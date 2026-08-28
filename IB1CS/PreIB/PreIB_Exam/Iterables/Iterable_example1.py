#1
for c in range(10):
    print(c, end=' ')
print('D')
#2
for d in range(10, 0, -1):
    print(d, end=' ')
print('E')
#3
for e in range(1, 16, 2):
    print(e**2, end=' ')
print('F')
#4
for f in range(14):
    if f%2==0:
        print('x', end=' ')
    else:
        print('y', end=' ')