import random
count=0
p=1000
for a in range(p):
    b=random.randint(1,6)
    if b==6:
        count=count+1
print(count)