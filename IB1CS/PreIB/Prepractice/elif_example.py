a = int(input('please give 1st int: '))
b = int(input('please give 2nd int: '))

if a % b == 0 or b % a == 0:
    reply = 'yes'
else:
    reply = 'no'

print(reply)

#string nested if-else example
str1 = input('please give 1st string: ')
str2 = input('please give 2nd string: ')

if str1 == str2:
    reply = 'the two strings are equal'
else:
    if str1 > str2:
        comp = 'greater'
    else:
        comp = 'smaller'

    reply = f'{str1} is lexicographically {comp} than {str2}'

print(reply)

#Homework 3 example
primes = (2, 3, 5, 7)
print(f'single digit primes are {primes}')
a= 5 in primes
b= 6 not in primes
print(a)
print(b)

#elif example
str3 = input('please input 1st int')
str4 = input('please input 2nd int')
if str3==str4:
    c='great'
elif str3 > str4:
    c=f'{str3} is greater than {str4}'
else:
    c='damn'
print(c)