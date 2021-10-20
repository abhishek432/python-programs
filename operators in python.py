#operators in python---

#Aritematic operator-
"""
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
      
"""
#comparison operator---
"""
x=2
z=6
if x==z:
    print("x=z")
elif x>z:
    print("x>z")
else:
    print("x<z")
    
"""
      
#logical operator--

             #And operation--
"""
a=False
b=False
print(a and b)

a=True
b=False
print(a and b)

a=True
b=True
print(a and b)
"""
            #or operation-
"""
a=False
b=False
print(a or b)

a=False
b=True
print(a or b)

a=True
b=True
print(a or b)
"""
            # Not operator--
"""
a=True
print(not a)

a=False
print(not a)
"""
#Identity operator---
"""
a=5
s=5
if a is s:
    print('similar')
elif a is not s:
    print('not similar')
    
#eg2:---

a=5
s=4
if a is s:
    print('similar')
elif a is not s:
    print('not similar')
"""
#Membership operator--
"""
a=(2,3,4,5,6,7,78,45,67,77)
if 45 in a:
    print("available")
elif 45 not in a:
    print("Not available")

    
    
a=[2,3,4,5,6,7,78,45,67,77]
if 1 in a:
    print("available")
elif 1 not in a:
    print("Not available")
"""
#Assignment operator---
"""
x=5
x+=3
print(x)

x=10
x-=2
print(x)
    
x=5
x*=3
print(x)

x=125
x/=6
print(x)

x=1212
x%=7
print(x)
"""
#Bitwise operator---

             #bitwise AND operator-
"""
a=0
b=0
print(a & b)

a=1
b=1
print(a & b)
"""

           #bitwise OR opertion-
"""
a=0
b=0
print(a | b)

a=1
b=0
print(a | b)
"""

        #bitwise XOR operation
x=0
y=1
print(x ^ y)
        #bitwise NOT operation

b=0
print(~ b)
