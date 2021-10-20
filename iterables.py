#iterator of tuple---
"""
fruit_tuple=("apple","kivy","banana","mango")
myiter=iter(fruit_tuple)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""
#iterator  for string---
"""
animal="cat"
ab=iter(animal)
print(next(ab))
print(next(ab))
print(next(ab))

"""
#for loop to iterate an iterble--
"""
fruit_tuple=("apple","kivy","banana","mango")
for i  in fruit_tuple:
    print(i)
"""

#for string--
"""
str="hello"
for i in str:
    print(i)
"""

#stop iteration--

"""
#method 1----
class myno():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=50:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=myno()
myiter=iter(myclass)
for x in myiter:
    print(x)
"""

"""
# method 2----
for i in range(1,51,1):
    print(i)
"""
