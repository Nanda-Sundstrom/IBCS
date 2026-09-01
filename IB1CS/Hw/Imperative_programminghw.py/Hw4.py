cards=int(input("what is the value of your cards? "))

if cards<17:
    action='hit'
elif cards>21:
    action='bust'
else: 
    action='stand'

print(action)