# really inefficient, there's probably a better way to do this
for n in range(2, 10001):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    sum = 0
    for factor in factors:
        sum += factor

    if n == sum:
        print(n, end=" ")