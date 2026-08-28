a="season's greetings"
print(a.upper())
b='hello'
print(b.isupper())
print(b.count('hello'))
c='my dog and my cat and my hat'
print(c.count('my'))
print(c.endswith('hat'))

import datetime
now = datetime.date.today()
print(now)
print(now.year)

words=('SOME', 'test','Words')
for w in words:
    print(f'{w}: up {w.isupper()}, low {w.islower()}')

print('-'.join('abc'))
print(', like, '.join(('here', 'we', 'are', 'now')))

print(1+2)
print((1).__add__(2))

print('what'+'on'+'earth')
print(5*'WHAT? ')