#1
s=15
n=0
if n:
    output=f'{s/n}'
else:
    output='undefined'
print(output)
#2
user_input='something'
if not user_input:
    out='nope'
else:
    out='yep'
print(out)
#3
a=15
d=0
print(a%d if a and d else -1)
#4
import random
print('heads' if random.randint(0, 1) else 'tails')