lst=[5, 11, 7]
for x in lst:
    print(x)

print(lst[0], lst[2])
lst[2]*=3
print(lst)
print(lst[-1])
print(len(lst))

#Searching lists
lst2=list(range(10))
print(10 in lst)

lst3=[10-abs(y-3) for y in range(7)]
print(lst3)
val=8
print(lst3.count(val))
print(lst3.index(val))

#Adding elements
lst4=list(range(10))
lst4.insert(0,55)
print(lst4)

#Removing elements
lst5=list(range(10))
print(lst5.pop())
print(lst5)
lst5.pop(5)
print(lst5)

#Reordering
lst6=list(range(10))
print(list(reversed(lst6)))
print(lst6)
lst6.reverse()
print(lst6)

lst7=['cat', 'dog', 'squirrel', 'mouse']
lst7.sort()
print(lst7)
lst7.sort(reverse=True)
print(lst7)

import random
lst8=list(range(10))
print(random.sample(lst8, 3))