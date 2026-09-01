while ((a := int(input("Give a positive integer: "))) <= 0):
    print("Give positive integer")

while ((b := int(input("Give another positive integer: "))) <= 0):
    print("Give positive integer")

n = 1
while True:
    if n % a == 0 and n % b == 0:
        break
    n += 1

print(n)