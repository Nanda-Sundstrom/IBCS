#1
a='yes!'
b='indeed!'
print(3*a+3*b)
print(3*(a+b))

#2
c='spam'
for d in range(5):
    print(d*c)

#3
w='spam'
for (i, l) in enumerate(w, start=1):
    print(i*l, end= '')