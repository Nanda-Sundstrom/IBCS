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