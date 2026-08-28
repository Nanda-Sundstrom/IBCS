a=int(input('Give an integer: '))
prime=True
for b in range(2, a):
    if a%b==0:
        prime=False
        break
if prime:
    print(f'{a} is a prime number!')
else:
    print(f'{a} is not a prime number!')