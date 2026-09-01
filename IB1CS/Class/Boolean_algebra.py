#Ex 2 (ex 1 on paper)
#1
year=int(input('please give year to check: '))

leap=False

if year%4==0: #is multiple of 4
    leap=True

if year%100==0:
    leap=False

if year%400==0:
    leap=True

print(leap)

#2
print(year%400==0 or year%4==0 and year%100!=0) # or using "and not year%100==0"

#Walrus operator (start code imported)
while (response := input('yes or no: ')) != 'yes' and response != 'no':
       pass # do nothing; provides an empty suite

print(response)

#Ex 3
#part1
while not (1<= (day:=int(input('please give day of week (1-7): ')))<=7): #while input is bs
     print('please provide a valid day of week')
#part2
while (vacation:=input('is James on vacation (yes/no): ')) != 'yes' and vacation!='no':
     pass
#output
print(vacation=='yes' or day>5)