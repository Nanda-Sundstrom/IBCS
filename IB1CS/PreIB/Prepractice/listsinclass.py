lst = ['a', 'short', 'sentence']

for w in lst:
    print(len(w))
print(lst+ ['continued'])
print(lst * 3)
print(sum(list(range(100)))) # 0 + 1 + 2 + ... + 99

#yatzy example
import random
throws= [random.randint(1,6) for i in range(5)]
print(throws)
kept = [t for t in throws if input(f'keep {t} (yes/no) ')] == 'yes'
print(kept)