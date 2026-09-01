a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))
c = int(input("Enter a third integer: "))

res = a
if b > res:
    res = b
if c > res:
    res = c

print(res)

"""
2. The program tries to find the largest number from integers a, b, c.
3. If a < c < b, res becomes a -> b -> b
"""