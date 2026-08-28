import random
count=0
p=1000
for a in range(p):
    b=random.random()
    c=random.random()
    if b**2 + c**2 <1:
        count+=1
print(count)
print(count/p*4)