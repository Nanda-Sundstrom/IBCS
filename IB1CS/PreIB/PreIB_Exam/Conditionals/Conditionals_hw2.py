a=str(input('Do you prefer red, blue or yellow: '))
if a=='red':
    b=str(input('Light or dark?'))
elif a=='blue':
    b=str(input('Like the sky during the night or the day?'))
elif a=='yellow':
    b=str(input('Butter or mustard yellow?'))
else:
    b="That's not what I asked bro"
print(b)
if b=='light':
    print("That's just pink mate")
else:
    if b=='dark':
        print('This is THE correct answer!')
    else:
        if b=='night':
            print("That's fire")
        else:
            if b=='day':
                print('Boooringgg')
            else:
                if b=='butter':
                    print('Ok whatever')
                else:
                    if b=='mustard':
                        print('Ew this is the worst answer!')
                    else:
                        print('Tf did you say??')