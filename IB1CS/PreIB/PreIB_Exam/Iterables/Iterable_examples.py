for a in range(10, 0, -1):
    print(a, end=' ')
print('A')
for b in range(8,1,-1):
    print(b, end=' ')
print('B')
for c in range(8,1,-2):
    print(c, end=' ')
print('C')
for d in range(11):
    print(d, end=' ')
print('D')
for e in range(11):
    if e==7:
        break
    else:
        print(e, end=' ')
print('E')
for f in range(11):
    if f==7:
        continue
    else:
        print(f, end=' ')
print('F')