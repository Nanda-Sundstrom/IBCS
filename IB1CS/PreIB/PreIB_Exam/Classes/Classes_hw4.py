import datetime
independence_day=datetime.date(1917, 12, 6)
print(independence_day)
print(independence_day.weekday())

import calendar
print(calendar.day_name[0])
print(calendar.day_name[6])

print(calendar.day_name[independence_day.weekday()])

a=input('Please give name of person: ')
b=int(input('Please give year of birth: '))
c=int(input('Please give month of birth: '))
d=int(input('Please give day of birth: '))

birthday=datetime.date(b, c, d)

print(f'{a} was born on {calendar.day_name[birthday.weekday()]}.')