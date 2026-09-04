lst1=[]
lst2=[]
while (a:=int(input('Please give an integer: ')))!=0:
    if a>0:
        lst1.append(a)
    elif a<0:
        lst2.append(a)

print(lst1)
print(lst2)