"""
4 pillar of oops : 

1. inheritance 
2. encapsulation  
3. abstraction  
4. polymorphism 
"""

# inheritance : 
"""
Inheritance is a way to create a new class by deriving it from an existing class, so the new class automatically has:

The attributes (variables) of the parent class.
The methods (functions) of the parent class.
The ability to override or extend those methods

type : 
1. single level inheritance 
2. multi level inheritance 
3. multiple inheritance
4. hybrid inheritance
5. hierarchical inheritance

"""
# destructor : automatically called when an object is destroyed.

# constructor  : automatically called when an object is created. 
"""
type  of constructors :
1. default constructor
2. parameterized constructor
3. non-parameterized constructor
4. constructor overloading

"""

#ex :1 default constructor

"""class student :  # classs name  student 
    def __init__(self):    # def  function  __init__ ====> constructor / special method
        print("default constructor")

s=student()  # s object of class student 

"""

# ex :2 non-parameterized constructor

"""class student :
    def __init__(self):
        self.__name ="manthan"  # name  : private 
        self.age=22   # age  : public
        print("non-parameterized constructor")
        
    def name_print(self):
        return self.__name

s=student()
print("age is : ",s.age)
print(s.name_print())
"""

# ex :3 parameterized constructor

"""class student :
    def __init__(self,name,age):
        self.name =name 
        self.age=age
    
    def display(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
        
s=student("manthan",23)
s.display()
"""

# ex :1 single level inheritance

"""
class a    ====> class a is base class 
class b(a) ====> class b is derived class from class a

"""

"""class student :
    def __init__(self):
        self.name="manthan"
        self.age=22

class clg(student):
    def __init__(self):
        student.__init__(self)  # base class constructor called 
        self.clg_name = "indus"
        
    def display(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
        print("clg name is : ",self.clg_name)
        
c=clg()
c.display()
"""

# ex :2 with out using constructor

"""class student :
    name="manthan"
    age=22

class clg(student):
    clg_name = "indus"
        
    def display(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
        print("clg name is : ",self.clg_name)
        
c=clg()
c.display()
"""

# ex :3 multi level inheritance

"""
class a 

class b(a) ===> b ===>a 

class c(b) ===> c ===>  a,b 

"""

"""class grandparent:
    def __init__(self,name):
        self.name =name 
        
class parent(grandparent):
    def __init__(self,p_name,name):
        grandparent.__init__(self,name)
        self.p_name=p_name

    def display(self):
        print("grandparent name is : ",self.name)
        print("parent name is : ",self.p_name)
        
class child(parent):
    def __init__(self,c_name,name,p_name):
        parent.__init__(self,p_name,name)
        self.c_name=c_name
        
    def display(self):
        print("grandparent name is : ",self.name)
        print("parent name is : ",self.p_name)
        print("child name is : ",self.c_name)
        
p =parent("amit","suresh")
p.display()

c=child("meet","katilal","dipak")
c.display()
"""

# ex : without using constructor

"""class dada :
    name ="suresh"
    
class bappa(dada) :
    b_name = "amit" 
    def display(self):
        print("dada name is : ",self.name)
        print("bappa name is : ",self.b_name)
        
class chokro(bappa):
    c_name = "manthan"
    
    def display(self):
        print("dada name is : ",self.name)
        print("bappa name is : ",self.b_name)
        print("chokro name is : ",self.c_name)
        
# b=bappa()
# b.display()

c=chokro()
c.display()
"""

# ex : multiple inheritance
"""
class a : 
class b : 
class c (a,b) :
"""

"""class student :
    name= "raju" 
    
class teacher :
    t_name ="varsha"
    
class clg(student,teacher):
    clg_name = "indus"
    
    def show(self):
        print("name is : ",self.name)
        print("t_name is : ",self.t_name)
        print("clg_name is : ",self.clg_name)
    
c=clg()
c.show()"""

#hirechierarchy inheritance : 

"""
class a :
class b(a): 
class c(a) 
class d(b,c):

"""

# hybrid inheritance :  it is  combination  more than one inheritance. 

"""
class a :
class b(a):
class c(b):
class d(b,c):

"""

# encapsulation :
"""
Encapsulation is one of the core principles of Object-Oriented Programming. It means bundling data (attributes) and methods (functions) that operate on that data into a single unit (class), while also restricting direct access to some of the object's components.

In simpler terms:

It hides the internal details of how a class works.
It exposes only what is necessary through public methods.
It protects the data from unintended interference or misuse.

2 methods : 

1. get _method : to get the value of the attribute
2. set _method : to set the value of the attribute
"""

# ex :1 

class employees : 
    
    name ="manthan"  # name  age  ====> public
    age =23 
    __salary =90000 
    __password = 9898 
    
    def get_salary(self):
        return self.__salary

    def get_password(self):
        return self.__password
    
    def set_password(self,new_password):
        self.__password=new_password
    
    def show(self):
        print("name is :",self.name)
        print("age is :",self.age)
e=employees()
print("before using  set method employees information  is : \n")
e.show()
print("salary is :",e.get_salary())
print("password is :",e.get_password()) 

print("after using  set method employees information  is : \n")
e.show()
e.set_password(1211)
print("password is :",e.get_password())
print("salary is :",e.get_salary())