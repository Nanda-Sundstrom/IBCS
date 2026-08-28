lst=list(range(10))
print(lst)

lst2=[]
for x in range(10):
    lst2.append(x**2)
print(lst2)

lst3=[f'val {x}' for x in range(10) if x%3==0]
print(lst3)

#Traversing lists
lst4=[y%3 for y in range(10)]
print(lst4)
for y in lst4:
    print(y, end='-')
print()

lst5=[c for c in 'thingamabob']
for i in range(len(lst5)):
    if i%2==0:
        print(lst5[i], end=' ')