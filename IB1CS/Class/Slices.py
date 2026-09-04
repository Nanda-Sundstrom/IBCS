lst = list(reversed(range(10)))
print(lst)
print(lst[1:2]) #start at index 1 and end before 2
print(lst[:2]) #start at index 0 end before 2

import random
n=12
lst2=random.sample(list(range(n)), n)
print(lst2)
print(lst2[1:]) #start at 1st index end at last
print()

diffs= [b - a for (a, b) in zip(lst2, lst2[1:])]
print(lst2)
print(diffs)