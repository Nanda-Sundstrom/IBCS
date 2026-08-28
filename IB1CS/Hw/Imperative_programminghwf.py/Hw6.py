#1
#p(4) = 3e + 2e * 2 = 7e
#p(w) = 3e + 2e * (w-2)

#2
#p(11) = 9e + 3e * 6 = 27e
#p(w) = 9e + 3e * (w-5)

#3
w=int(input('Please give weight: '))

if w<=2:
    p=3
elif 2<w<=5:
    p=2*(w-2)+3
else:
    p=3*(w-5)+9

print(f'price is {p} euros!')