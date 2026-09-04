#Ex2
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

#Ex3
lst3=['what', 'a', 'wonderful' 'morning']
new_lst=[]
for word in lst3:
    if len(word) <= 4:
       new_lst.append(word) 

lst3=new_lst
print(lst3)

lst4=['what', 'a', 'wonderful' 'morning']
lst4=[word for word in lst4 if len(word) > 4]
print(lst4)