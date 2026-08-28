import time
a=int(input('Give a number of seconds until lift-off: '))
for t in range(a, 0, -1):
    print(f'{t}...')
    time.sleep(1)
print('lift-off')