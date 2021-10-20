#write a program that will return true if the two integer values are equal or their sum or diffrence is 5
"""
def func(a,b):
    sum=a+b
    diff=a-b
    if (a==b or sum==5 or abs(diff)==5):
        return True
    else:
        return False

print(func(5,10))
"""
#python code to get os name, platefor
"""
import os
import platform
import struct
print(os.name)
print(platform.system())
print(platform.release())
print(struct.calcsize("P") * 8)
"""
#Math Function---
import math

s=min(23,34,67,88,87,101,35,13)
print(s)

s=max(23,34,67,88,87,101,35,13)
print(s)

s=(-12.7)
print(abs(s))

s=pow(78548,2)
print(s)

x=math.sqrt(2025)
print(x)

print(math.pi)



