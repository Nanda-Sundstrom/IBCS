lst=[4,11,-5,2.6,'foo']
print(lst[0])
lst[0]=333
print(lst)
lst.append((6,1))
print(lst)

words=['some', 'words', 'here']
print(words)
lst=[]
print(lst)

a=list(range(5))
b=list('a string is also an iterable')
w='whatever'
c=list(zip (w, w.upper()))
d=list((12, 1.1**2, 'y', 'x'))
lst=['a', 'short', 'sentence']
print(lst[0])
print(len(lst))
for w in lst:
    print(len(w))
print(lst+['continued'])
print(lst *3)
print(sum([-2, 8, -60, 50]))

print([x**2 for x in range(10) if x%2!=0])