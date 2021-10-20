
#named tuple----
"""
from collections import namedtuple

#eg1--
student=namedtuple('student','fname,lname,age')
s1=student("sachin","tendulkar",'40')
print(s1.fname,s1.age,s1.lname)

#eg2--
x=namedtuple('course','name,tech')

a=x('data science','python')#object 1
a1=x('r prog','java')#object 2

print(a)
print(a1)

"""
# deque---
"""
from collections import deque

#eg1-
x=['p','t','o','y','n']
d=deque(x)
print(d)
d.append('mindtree')
print(d)

#intersection-

list=['a','c','t']
d=deque(list)
print(d)
d.append('z')#adding element
d.appendleft('a')#adding element in left
print(d)
d.pop()#removing element
d.popleft()
print(d)
"""
#chainmap---
"""
from collections import ChainMap
a={1:'r-prog',2:'python'}
b={3:'mi',4:'ai'}
z=ChainMap(a,b)
print(z)

s={9:'criket',8:'hockey',7:'shooting'}
t={10:'football',11:'chess'}
q=ChainMap(s,t)
print(q)
"""
#counter----
"""
from collections import Counter

a=[12,34,5,6,67,89,24,54,12,546,5,67,6,89,6,5,5,5]
b=Counter(a)
print(b)

color=['red','red','red','red','red','red','green','yellow','pink','blue']
print(Counter(color))
"""
# OrderedDict----
"""
from collections import OrderedDict
d=OrderedDict()
d[1]='m'
d[2]='i'
d[3]='n'
d[4]='d'
d[5]='t'
d[6]='r'
d[7]='e'
d[8]='e'
print(d)
"""
#Defaultdict----
"""
from collections import defaultdict
d=defaultdict(int)
d[1]='c'
d[2]='c++'
d[3]='java'
d[4]='python'
print(d)
"""
