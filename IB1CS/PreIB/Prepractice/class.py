import random
low = 1
hi = 100
number = random.randint(low,hi)
guess = int(input(f'guess an int from [{low}, {hi}]:'))
if guess == number:
    reply = 'correct'
else:
    reply = f'incorrect, correct was {number}'
print(reply)