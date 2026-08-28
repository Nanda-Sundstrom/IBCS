#1
print([x for x in range(143) if x**2%143==126])
#2


lst=list(range(5, 10))
print(lst)
print(lst [2:4])
print(lst[0:3])

lst=list(range(10, 5, -1))
print(lst)
lst.append(100)
print(lst)

lst=list(range(10, 5, -1))
print(lst)
lst.extend(range(3))
print(lst)

lst=list(range(10, 5, -1))
lst=lst+list(range(3))
print(lst)

lst=list(range(10, 5, -1))
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(1))

lst=[2, 5, 7, 5, 11]
lst.remove(5)
print(lst)

lst=list(range(10, 5, -1))
print(lst)
lst.insert(1, 100)
print(lst)

lst=list(range(5, 10))
print(lst)
lst[:3]=[100, -5, 11]
print(lst)
lst[-2:]=[]
print(lst)

sentence='seeing is believeing'
print(sentence.split())
print([len(w) for w in sentence.split()])
print(sorted('howdy'))

#1HW
lst=list(range(4))
lst[0]=20
print(lst)

lst=list('exciting')
print(lst[1], lst[-1])

lst=[]
lst.append('x')
lst.append('a')
lst.insert(1, 'k')
print(lst)

#2
lst=list('qwerty')
for _ in range(3):
    print(lst.pop())
for l in 'abc':
    lst.append(1)