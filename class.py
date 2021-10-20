"""

class car():
    def __init__(self,modelname,year,price):
        self.modelname=modelname
        self.year=year
        self.price=price

toyota=car('cryta',2021,10000)
honda=car('city',2020,50000)

toyota.cc=2000
print(honda.__dict__)

"""
"""
def Mindtree():
    def Edge():
        name='python'
        
    def Nonedge():
        Nonedge name
        name ='Spark'
        
    def global():
        global name
        name='aws'
        
    name='it company'
    print(name)
    Edge()
    print(name)
    Nonedge()
    print(name)
    Global()
    print(name)


Mindtree()
print(name)



#class and object 

def mindtree():
    def local_fun():
        name='python'  
    def non_localfun():      
        nonlocal name      
        name='python programming'  
    def gobal_fun():      
        global name      
        name='AWS Cloud'  
    name ='mindtree'  
    print(name)  
    non_localfun()  
    print(name)  
    gobal_fun()  
    print(name)
mindtree()
print(name)

"""

