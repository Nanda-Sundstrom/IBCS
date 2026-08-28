import random
#1
low =1 
high=100
number=random.randint(low, high)
guess= int(input(f'Guess an integer from [{low} to {high}]: '))
if guess == number:
    reply = 'correct'
else:
    reply = f'incorrect, correct was {number}'
print(reply)

#2
a=int(input('Give an integer: '))
b=int(input('Give another integer: '))
if a%b==0:
    print(f'{a} is divisible by {b}!')
elif b%a==0:
    print(f'{b} is divisible by {a}!')
else:
    print('nuh uh')

#3
c=str(input('Give a string: '))
d=str(input('Give another one: '))
if c==d:
    reply=f'{c} and {d} are equal.'
else:
    if c>d:
        reply=f'{c} is lexicographically greater than {d}'
    else:
        reply=f'{d} is lexicographically greater than {c}'
print(reply)