"""
1. no arg  with return  
2. with arg  with return 
"""

# paramter 
# arg  : 

# ex :1 

"""def x():
    a=10 
    b=20
    c=a+b 
    return c 
print(x())
"""
# ex :2 

"""def sum1(a,b) :
    return a+b

print(sum1(12,56))
"""

# local variable : declared inside function not accessible outside function

"""def k():
    x=10 
    print(x)
k()
# print(x)not accessible outside function
"""

# global variable : declared outside function accessible outside function

"""x=90 
def k():
    print(x)
    
k()
print(x)
"""

# modify global variable inside function

"""x=90 
def k():
    global x
    x=100 
    print(x)
k()
print(x)
"""

# task :1 prime  number  

"""
def prime(n):
    count=0
    for i in range(1,n+1):
        if n % i ==0 :
            count +=1
    if count ==2:
        return True
    else:
        return False
print(prime(11))
"""

# *args :  take any number of arguments

"""def sum1 (*args):
    return sum(args)

print(sum1(1,6,34,56,78,90,12.56,78))
"""

# **kwargs :  take any number of keyword arguments

"""
def d1(**kwargs):
    for i ,j in kwargs.items():
        print(i,j)
d1(name="harshita",age=21,gender="female")
"""

# lambda : one liner function  
"""
syntax : 
lambda  arguments :  expression
"""

# ex:1 

"""
result =lambda a,b : a+b
print(result(34,56))
"""

# ex :2 

"""result =lambda x : x**3
print(result(4))
"""

# built-in function : len min max sum sorted 

"""result =lambda x : len(x)
print(result("my name is abbas."))
print(result([1,2,3,4,5,6,7]))

result1 =lambda x : sorted(x)
print(result1((1,34,56,23,-90)))
"""

# if else  using lambda : 

"""age =int(input("enter your age : "))
if age >18 :
    print("you are eligible for voting")
else :
    print("you are not eligible for voting")
    
"""    
re =lambda age :  print("eligible for  vote") if age >18 else print("not eligible for vote")
re(4)
