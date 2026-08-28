#Homework 1
import random
guess=int(input('give an integer'))
answer= random.randint(1, 100)
if guess<answer:
    reply = f'{guess} is smaller than {answer}'
else:
    if guess == answer:
        reply = f'{guess} is equal to {answer}'
    else:
        reply = f'{guess} is larger than {answer}'

print(reply)

#Homework 2
preference = str(input('tea or coffee?'))
if preference == 'tea':
    b = str(input('green or rooibos?'))
    if b == 'green':
        say = 'nerd'
    else:
        say = 'wtf'
else:
    a = str(input('cappuccino or espresso?'))
    if a == 'cappuccino':
        say = 'loser'
    else:
        say = 'alpha'
print(say)

#Homework 3
direction = ('n','ne','e','se','s','sw','w','nw')
c = str(input('pick a direction [n, ne, e, se, s, sw, w or nw]:'))
if c in direction:
    go='valid'
else:
    go='invalid'
print(go)

#Homework 4
e=str(input('state a word or sentence:'))
f=str(input('state a second word or sentence:'))
g=str(input('state a third word or sentence:'))
print(f'"{max(e,f,g)}" is lexicographically the largest.')

#Homework 5
s=int(input('give systolic blood pressure:'))
d=int(input('give diastolic blood pressure:'))
print(f'this blood pressure is {'normal' if s<120 and d<80 else 'not normal'}')

#Homework 6
#1
o=15
n=0
if n:
    output=f'{o/n}'
else:
    output='undefined'
print(output)
#2
user_input='something'
if not user_input:
    output='nope'
else:
    output='yep'
print(output)
#3
p=15
q=0
print(p%q if p and q else -1)
#4
import random
print('heads' if random.randint(0, 1) else 'tails')