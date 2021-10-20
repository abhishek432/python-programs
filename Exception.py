#Try block lets you test a block of code for errors
#Except block lets you handle the error
#Finally block lets you execute code regardlesss of the result of try and except block
#Example for "try"

#Eg1--
"""
try:
    print(x)

except:
    print("an exception occured")
"""
#Eg2:---
"""   
try:
    print("Apple")

except:
    print("an exception occured")

""" 
#Eg3:---
"""
try:
    print(q)
except:
    print("Something went wrong")
else:
    print("nothing went wrong")
"""

#Eg4--

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("nothing went wrong")
finally:
    print("The 'try except' is Fisnished")
"""
