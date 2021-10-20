
# single level inheritence----
"""
class Animal():
    def speak(self):
        print("Animail is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d=Dog()
d.bark()
d.speak()

"""
# multi level inheritence----
"""
class Animal():
    def speak(self):
        print("Animail is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class puppy(Dog):
    def child(self):
        print("Puppy is child of dog")


p=puppy()
p.bark()
p.speak()
p.child()

"""
# heirarchical inheritence----

class Animal():
    def speak(self):
        print("Animail is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class puppy(Animal):
    def child(self):
        print("Puppy is child of dog")


print("object of child 1")
d=Dog()
d.bark()
d.speak()

print("object of child 2")
p=puppy()
p.speak()
p.child()
