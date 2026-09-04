#Enumerate
lst=['what', 'will', 'happen']
for p in enumerate(lst):
    print(p)

#Unpacked ver.
lst2=['what', 'will', 'happen']
for (i, word) in enumerate(lst2):
    print('index:', i, 'word:', word)

t=('first', 'second')
print(t[0])
#Tuple unpacking
(a,b)=t
print(b)

lst3=list('abc')
lst4=list('def')
for x in zip(lst3, lst4): 
    print(x)