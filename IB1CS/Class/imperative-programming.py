a=15
b=22
print(a,b) 
print(a-b) 
print(f'ratio of a and b is {a/b}') 
print((3*a)%(2*b)) #3a/2b remainder
print(45/44)
print(45%44)
print(a**b) #to the power of 
name="foo"
last="bar"
print(name," ",last)
import math
print(math.pi)

import dis # import module for showing bytecode

# function finding the sum
def fun():
    s = 0
    for i in range(5, 16):
        s += i
    return s

# disassemble the bytecode of the function
dis.dis(fun)
#move 2ndclass & grade files into here(?)