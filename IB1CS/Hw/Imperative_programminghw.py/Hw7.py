n = 1
while True:
    if (n ** 3 - 16) % 47 == 0:
        print(n)
        break
    n += 1

# using boolean flag
found = False
n = 1
while not found:
    if (n ** 3 - 16) % 47 == 0:
        print(n)
        found = True
    n += 1