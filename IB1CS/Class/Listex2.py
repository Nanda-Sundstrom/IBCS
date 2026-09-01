#1
lst=[]

while (v := int(input('please give next int: '))) >=0:
    lst.append(v)

print(lst)

#2
lst2=[]
while (a := int(input('give next integer: ')))>=0:
    i=0 #index into list
    while i < len(lst2) and lst2[i] < a:
        i+=1
    lst2.insert(i,a)

print(lst2)