"""
conversion  : 
"""
"""a=90 
print(a)
print(type(a)) 
print(float(a))
print(str(a))

b= float(a)
print(b)
print(type(b))
"""

# ex :1 
"""
a=int(input("enter the number : "))
b=int(input("enter the number : "))

print(a)
print(b)
print("div of  two number is  :  ",float(a/b))
"""

# loop  : iteration ===> repeation 
"""
1. for  loop  : entry  control  loop 
2. while  loop :  entry  + exit control loop
"""
# syntax : for loop  
"""
for (variable name) in range(start ,end ,step):
    print(variable name)

"""
# ex :1 : 1-100

"""
for i in range(1,101) :
    print(i,end=" ")
"""    
# ex : -10 to 30 
"""
for i in range(-10,30) :
    print(i,end=" ")

"""
# ex :-40 to -10 

"""for x in range(-40,-10) :
    print(x,end=" ")
"""

# 100-1 : 
"""
for i in range(100,1,-1) :
    print(i,end=" ")
"""

"""
for i in range(1,100,3) :
    print(i,end=" ")
"""

# -10 to -40 :
"""
for i in range(-10,-40,-1) :
    print(i,end=" ")
"""

# print  even  number between 30- 100

# break  : break the  loop  

"""
for i in range(10):  # 5
    if i==5:    # 5==5 
        break 
    print(i,end=" ")   # 0 1 2  3  4 
    
"""

# contunie : continue the  loop  and skip the  current iteration
"""
for i in range(10): 
    if i==3:    
        continue 
    print(i,end=" ")    
"""

# pass : 
"""for i in range(10): 
    if i==3:    
        pass
    print(i,end=" ")   
""" 
# ex :4 
"""
start =int(input("enter the start number : "))
end =int(input("enter the end number : "))

for i in range(start,end,2):
    print(i,end=" ")
"""
# ask user to enter the  number and print  n natural number sum. 

n=int(input("enter the number : "))  # 5
sum =0    # sum =0 
for i in range(1,n+1):  # 5 , 6 
    sum =sum +i   # sum =15
    
print("n natural  number sum  is  : ",sum)

# ask user to enter the number  and  print the factorial of that number. 