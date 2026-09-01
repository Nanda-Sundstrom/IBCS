a=int(input('Give an integer: '))
b=int(input('Give another integer: '))

#1
if a>=100 and b<=50:
    output=1
else:
    output=0

print(output)

# 2
if (a >= 100 and b <= 50) or (a <= 50 and b >= 100):
    output = 1
else:
    output = 0

print(output)