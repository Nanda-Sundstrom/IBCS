while (s := int(input("Give a positive integer: ")) <= 0):
    print("Give a positive integer")

n = 1
while True:
    if n**3 - 10 * n ** 2 > s:
        break
    n += 1

print(n)