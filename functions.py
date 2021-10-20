class hello():
  def __init__(self):
    print("hello this is a class")
    
  def func(x,y):
    return x-y
    
hello.func(2,3)

# abs function----
#integer-
a=-20
print(abs(a))
#float-
f=-20.1
print(abs(f))

#All function-----
a=[1,2,8,3,4,5,7]
print(all(a))
# eg: 2
s=[0,False]
print(all(s))
#eg:3
s=[0,1,2,3,4,5]
print(all(s))
#Eg:4
a=[]
print(all(a))
#eg:5
s=[0,False,4]
print(all(s))

#binary number---
n=10
print(bin(n))

#boolean function----
test=True
print(bool(test))
abhi=False
print(bool(abhi))
anji=None
print(bool(anji))

#dict function---
no=dict(x=5,y=2)
print(no)
print(type(no))

#eval function----
x=12
print(eval('x+1'))

#help funtion----
help(print)

#len function---
str="hello i am abhishek"
print("Length of string: ",len(str))

#max function--
a=[1,3,4,6,7,9]
print(max(a))

#min function--
a=[1,3,4,6,7,9]
print(min(a))

#octal function---
a=256
print("octal of: ",oct(a))

#power fuction--
print(pow(-2,5))
print(pow(5,-2))


#reverse function---
str="ABHISHEK"
print(list(reversed(str)))
#eg-2--
se=range(5,9)
print(list(reversed(se)))


#sum function---
number1=[5,4,6,7,1]
numsum=sum(number1)
print(numsum)

#fuctional programing---
#pure function-
def pure(list):
  newlist=[]
  for i in list:
    newlist.append(i**2)
  return newlist

original_list=[1,2,3,4,5]
modified_list=pure(original_list)

print(original_list)
print(modified_list)

#recursion--
def factorial(x):
  if (x==1):
    return 1
  else:
    return (x * factorial(x-1))

n =8
print(factorial(n))   


#map functions--
def addition(n):
  return n+n

numbers=(5,4,3,2,1)
results=map(addition,numbers)  
print(results)
for result in results:
  print(result)


#filter fuction----
def fun(var):
  letters=['a','e','i','o','u']
  if (var in letters):
    return True
  else:
    return False

sequence=['s','e','i','m','j'] 
filtered=filter(fun,sequence)     
print('Filtered letters are :')
for s in filtered:
  print(s)

#lambda function
#syntaxof lambda   lambda argument:expression
x= lambda a:a+10
print(x(5))

x= lambda a:a*10
print(x(10))

x=lambda a,b,c:a+b+c
print(x(5,5,6))

#immutable function--
immutable='mindtree'
# immutable[1]=k   
