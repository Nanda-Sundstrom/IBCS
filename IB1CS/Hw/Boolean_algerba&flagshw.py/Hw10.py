# 1
import math

r1 = 2 * 2 # square with side length 2
r2 = math.pi * 1 ** 2 # circle with radius 1

ratio = r2 / r1
print(ratio)

# 2
import random

landed_points_count = 0
total_points_count = 10000
for i in range(0, total_points_count):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:
        landed_points_count += 1

ratio = landed_points_count / total_points_count
print(ratio)