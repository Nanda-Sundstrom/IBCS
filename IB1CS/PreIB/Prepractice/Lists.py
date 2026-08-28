lst=list(range(5,10))
print(lst)
print(lst[2:4])
print(lst[2:])
print(lst[:4])
print(lst[-2:])

lsi=list(range(10, 5, -1))
print(lsi)
lsi.append(102)
print(lsi)
lsi.extend(range(3))
print(lsi)
lsi.extend('abc')
print(lsi)

lso=list(range(10, 5, -1))
lso= lso + list(range(3))
print(lso)

lsy=list(range(10, 5, -1))
print(lsy.pop())
print(lsy)

lsp=list(range(10, 5, -1))
print(lsp.pop(1))
print(lsp)

lsk=[2, 5, 7, 5, 11]
lsk.remove(5)
print(lsk)

lsd=list(range(10, 5, -1))
print(lsd)
lsd.insert(1, 100)
print(lsd)

lsg=list(range(5, 10))
print(lsg)
lsg[:3] = [100, -5, 11]
print(lsg)
lsg[-2:] = []
print(lsg)

whatever = 'seeing is believing'
print(whatever)
sentence = 'seeing is believing'
print(sentence.split())
long_words = [w for w in sentence.split() if len(w) > 4]
print(long_words)

print(sorted('howdy'))

x = list(range(4))
print(x)
y=x #bind y to the same object as x
print(id(x), id(y))
x.append(100)
print(y)