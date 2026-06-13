"""
operator  : 
1. airthematic op : + - * / % // 
2. relational op : == != > < >= <=    ===> bool type  ===> true or false
3. logical op : and or 
4. member op : in not in
5. assignment op : = += -= *= /= %= //=
"""

"""a=100
b=90000
print(a/b)  # 3.33333333
print(a//b)  # floor division : 3 
print(a%b)   # modulas :  remainder  3  rule : if you  modulas small number to  big number then always your answer is  small number.
print(a!=b)

print(a>b and a!=b)
print(a>b or a!=b)

l1=[12,34,56]
print(12 in l1)
print(90 not in  l1)

# a=a+b   a=a-b  a = a*b   
a+=b    
print(a)
"""

# conditional statement : if else 

"""
if con : 
    print()
else :
    print()
"""

# ex :1 
"""
age =int(input("enter the age : "))
if age > 18 :
    print("eligible  for vote ")
else :
    print("not eligible  for vote ")
"""    
#  odd even :  

"""
num =int(input("enter the number : "))
if num % 2 ==0 : 
    print("even number")
else :
    print("odd number")
"""    
# ask user to enter the number and check it is divisible by 5 or not.

"""num =int(input("enter the number : "))
if num % 5 ==0 : 
    print("div  by 5")
else :
    print("not")
"""

#nested if : 
"""
if con : 
    print()
elif con :
    print()
else : 
    print()
"""
# ex :3 

"""a=int(input("enter the number a : "))
b=int(input("enter the number b: "))

if a>b :   # a=900  b=900
    print("a is big")

elif b>a:
    print("b is  big")
  
else :
    print("same")
    
"""

# ex :4 ask user to enter the  number and  check it is div by  5 or 11 or  both 
"""num =int(input("enter the number : "))

if num % 5==0 and num % 11==0 :
    print("div by 5 and  11 both")
elif num % 11==0 : 
    print("div only 11")
elif num % 5 ==0 :
    print("div by  only 5 ")
else :
    print("not 5 and 11") 
"""

"""
task  :1 ask user  to enter the sales price  and  cost price  find out  the profit  or  loss. 
profit = sales - cost  
loss = cost - sales

input sales = 100 
input  cost =90      
output  profit 10 rs. 

task :2 ask user  to enter the  3 subjects calculate the  persontage  on basis of  persontage give a grade . 

per = (phy + che +maths)/100     
per =90 

per    grade 
90 +    A+ 
80-90   A 
70-80   B+ 
60-70   B 
50-60   C+ 
40-50   C
below Fail 

hint  : 

if per > 90 : 
    print("A+")
"""