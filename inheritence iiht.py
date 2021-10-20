"""
# single inheritence-----
class employee1():
  def __init__(self,name,age,bloodgroup):
    self.name=name
    self.age=age
    self.bloodgroup=bloodgroup

obj=employee1("abhi","17","A+")    
obj2=employee1("sachin","16","B+")

class child(employee1):
  print(obj.age,obj.name,obj.bloodgroup)
  print(obj2.age,obj2.name,obj2.bloodgroup)

"""
#multilevel inheritence----
class employee1():
  def __init__(self,name,age,bloodgroup):
    self.name=name
    self.age=age
    self.bloodgroup=bloodgroup

obj=employee1("abhi","17","A+")    
obj2=employee1("sachin","16","B+")

class child(employee1):
  def __init__(self,name,age,bloodgroup):
    self.name=name
    self.age=age
    self.bloodgroup=bloodgroup
  print(obj.age,obj.name,obj.bloodgroup)
  print(obj2.age,obj2.name,obj2.bloodgroup)
obj3=employee1("chitix","12","C+")  
 

class child2(child):

 print(obj3.age,obj3.name,obj3.bloodgroup)
