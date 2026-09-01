n = int(input("Give an integer: "))
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)