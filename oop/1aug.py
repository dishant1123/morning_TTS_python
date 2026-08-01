# ploymorphism  : 
"""
Definition:  
Polymorphism means “many forms”. In Object-Oriented Programming, it allows the same function or method name to behave differently depending on the object that calls it.

In Python, polymorphism is achieved through method overriding (in inheritance) and method overloading-like behavior (using default arguments or dynamic typing).

1. method overriding
2. method overloading
"""

# ex :1  method overloading 

"""class maths :
    def add(self,a,b,c=90):
        return a+b+c

    def sub(self,a,b=50):
        return a-b 
    
m=maths()
print(m.add(10,20))
print(m.add(10,20,30))

print(m.sub(10))
print(m.sub(10,20))
"""

# ex :2 method overloading

"""class student :
    def __init__(self):
        print("Student class")
        
    def __init__(self):
        print("Student class is  created")
    
    def show(self):
        print("student 1 class create function  name is  show")
        
    def show(self):
        print("student 2 class create function  name is  show")

s=student()
s.show()
"""

# ex :3 method overriding

"""class animal:
    def sound(self):
        print("animal sound")
        
class dog(animal):
    def sound(self):
        print("bhow bhow bhow .......woowwwww")
        
class cat(animal):
    def sound(self):
        print("meow meow meow .......miauu")
        
class bird(animal):
    def sound(self):
        print("chirp chirp chirp .......tweet tweet tweet")

all =[cat(),dog(),bird()]

for i in all:
    i.sound()
"""

# abstraction  :

"""
Definition:  
Abstraction is the process of hiding implementation details and showing only the essential features of an object. It allows you to focus on what an object does rather than how it does it.

In Python, abstraction is often implemented using abstract classes and abstract methods (via the abc module).

Simplifies complex systems by exposing only necessary parts.
Promotes cleaner design and reduces code duplication.
Provides a blueprint for other classes to follow.

ex : car driving  ---> streeling , cluch ,break ,asscelator  ====> how  its work ,which  first start  its hide 

ABC : abstract base class 

====> you can't create object of ABC class
====>@abstractmethod  ===> decorator 

"""
 
from abc import ABC, abstractmethod
"""
class vehicle(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod
    def stop(self):
        pass 

class car(vehicle):
    def __init__(self,name,model):
        vehicle.__init__(self,name)
        self.model =model
    
    def start(self): 
        print("car start")
    
    def stop(self):
        print("car stop")

class motorbike(vehicle):
    def __init__(self,name,model):
        vehicle.__init__(self,name)
        self.model =model
    
    def start(self):
        print("motorbike start")
    
    def stop(self):
        print("motorbike stop")
        
c=car("Honda","civic")
c.start()
c.stop()

m=motorbike("hero-honda","shine")
m.start()
m.stop()

"""

# class method ,static method : 

# ex :1 class method 
"""
1.@classmethod : decorator 
2. first argument of classmethod is cls
3. you can change the name of classmethod
4. directly access the class name
"""
"""
class student :
    
    clg_name ="Lj university"

    @classmethod
    def show(cls,new_name):
        cls.new_name=new_name
        print("clg new name is :",cls.new_name)
        
print(student.clg_name) # access directly for class name 
student.show("INDUS")
"""

# ex :2 static method
"""
1.@staticmethod : decorator
2. its work like  function
3. if you create static  method then  you can't take first argument as self.
4. you can;t change the static method 
"""

"""class maths :
    @staticmethod
    def add(a,b):
        print(a+b)
        
    @staticmethod
    def sub(a,b):
        print(a-b)
        
m=maths()
m.add(10,20)
m.sub(23,12)
"""

# exception handling :
"""
try:
    # Code that may raise an error
except SomeError:
    # Code to handle the error
finally:
    # Code that always runs (cleanup)

"""

#ex :1

"""try :
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print("result :",a/b)
except ZeroDivisionError:
    print("error :can't divide by zero")
    
"""

# ex :2 

"""try :
    l1=[10,20,30,40,50]
    print(l1[2])
    
except IndexError:
    print("error :index out of range")
    
"""

# ex:3 
try:
    f = open("soheb.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Closing file if it was opened")
    try:
        f.close()
    except:
        pass
