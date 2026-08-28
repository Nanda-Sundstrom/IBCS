#1
for a in range(7):
    print(a**3, end=' ')
print('A')
#2
for b in range(37, 6, -2):
    print(b, end=' ')
print('B')
#3
for c in range(21):
    if c%3==0:
        print('a', end=' ')
    elif c%3==1:
        print('b', end=' ')
    else:
        print('c', end=' ')