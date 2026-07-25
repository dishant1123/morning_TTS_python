"""
oop : object  oriented programming

ex : software   ===> onine purchase 
       step :1 laptop  ===> website ===> HTML/CSS  ===>js  ===>SQL 
                       ==>testing ===>bug fixing  ===>deployment
                       
class  : blueprint of  objects 
object : instance  of  class

fruits :  <=== class 
    apple ,chiku , mango , orange   <==== object 

"""

# ex :1 

"""class demo:  # class   demo   ===> class name 
    print("demo class is  created")
    print("there is  very high chances for raining today.")

d=demo()   # d ====> object 
"""    

# ex :2 

"""class student :
    name ="manthan"   # name  ,age 
    age =21 
    print("student class is  created")

s=student()
print("name is  :",s.name)
print("age is  :",s.age)
"""

# ex :3 
"""
class employess:
    name ="manthan"   # name  ,age
    salary =90000 
    
    def show(self):  # self ---> keyword  ,access ,arg first 
        # self.name="raju"
        # self.salary=89000
        print("name is :",self.name)
        print("salary is :",self.salary)
        
e=employess()
e.name="raju"
e.salary=89000
e.show()
"""

# ex :4 
"""
1. public : can access from anywhere.
2. private : can access from inside the class.
3. protected :can access from inside the class and from subclass. (inheritance)
"""

# ex :5 public : default 

"""class student :
    name ="manthan"   # name  ,age
    age =21    # name ,age  ====> public 
    
    def show(self):
        print("name is and age is :",self.name,self.age)
    
s=student()
s.show()
print("name is  :",s.name)
print("age is  :",s.age)
s.name="raju"
s.age=22
print("name is  :",s.name)
print("age is  :",s.age)
"""

# ex :6  private  : __ (underscore)

"""class employess:
    name ="manthan"   # name  ,age  ====> public
    age =22
    __salary =90000    # private 
    
    def display(self):
        print("salary is :",self.__salary)
    
e=employess()
print("name is :",e.name)
print("age is :",e.age)
# print("__salary is :",e.__salary)  # not  possible outside the  class bcz of private 
# e.__salary =70000  # you can't change the value of private variable
e.display()
"""

# ex :7  protected  : _ (underscore)

class employees :
    name ="manthan"  # name  age  ====> public 
    age =22
    __salary =90000  # salary  ===> private 
    _bonus =1000     # bonus  ===> protected
    
    def salary_show(self):
        print("salary is :",self.__salary)
        
class company(employees):
    
    def information(self):
        print("name is :",self.name)
        print("age is :",self.age)
        self.salary_show()
        print("bonus is :",self._bonus)  # protected 

c=company()
c.information()