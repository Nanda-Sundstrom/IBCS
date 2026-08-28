directions = ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw')
answer=str(input(f'Give me a direction {directions}: '))
if answer in directions:
    print('valid')
else:
    print('invalid')