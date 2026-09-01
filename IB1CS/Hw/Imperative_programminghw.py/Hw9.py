prev = 0
greatest_time = 0
greatest_diff = 0
for t in range(0, 101):
    current = t * (t - 20) * (t - 100)
    diff = prev - current
    if diff > greatest_diff:
        greatest_time = t
        greatest_diff = diff
    
    prev = current

print(greatest_time)