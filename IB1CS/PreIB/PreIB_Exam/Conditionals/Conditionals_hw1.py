a=int(input('Guess an integer between 1 and 100: '))
import random
b=random.randint(1, 100)
if a==b:
    print(f"Your guess '{a}' is correct! The answer is '{b}'")
elif a>b:
    print(f"'{a}' is larger than '{b}'!")
else:
    print(f"'{a}' is smaller than '{b}'!")