"""
factorial with sum  : 
"""

"""
n=int(input("enter the  number  : "))
sum =0 
fact =1 

for i in range(1,n+1):
    fact =fact *i 
    sum =sum +i 
print("sum of n natural  number  : ",sum)
print("factorial is  : ",fact)
"""

# while  : 
"""
syntax : 

i=100 
while (con) :
    print()
    inc/dec   i-=1
"""
# while  : 

"""i=1 
while (i<=100) :  # 3 <=100 
    print(i,end=" ") # 1 2 
    i+=1  # i= i +1   # 3 
"""

# prime   number: 2 factors  ===> 1 , number itself 
"""
7 factors : 1,7  ===> prime  number 
8 factors  : 1,2,4,8 ==> not  prime 
"""

# n=int(input("enter the  number  : "))  #7
# count =0 

"""
for i in range(1, n+1):   # 7,8 
    if n % i==0 :     # 7 % 7  ==0 
        count =count +1   #  2

if count ==2 :   # 2 == 2 
    print("prime  number")
else : 
    print("not")
"""
"""i=1   # 1 
while i<=n :  
    if n % i ==0 :
        count =count +1
    i+=1 
if count ==2 :
    print("prime  number")
else :
    print("not")
"""

# reverse : 
"""
input  : 123 
output : 321
"""
"""
n=int(input("enter the number : "))   # 123   
rev = 0 

while n > 0 :        # 0 > 0 
    r = n %10        # r = 1 % 10 = 1 
    rev = rev *10 +r # rev = 321 
    n = n //10       # n = 1 //10 = 0

print("reverse is  : ",rev)
"""

# pelindrome number : 121 ,141 ,111 ,33

"""n=int(input("enter the number : "))   # 121  
rev = 0 
temp = n  # temp =121 
while n > 0 :        # 0 > 0 
    r = n %10        # r = 1 % 10 = 1 
    rev = rev *10 +r # rev = 121  
    n = n //10       # n = 1 //10 = 0

if temp ==rev :  #  n ==rev 
    print("pelindrome number")
"""

# nested loop  : 

# print  prime  between 1 -500

start =int(input("enter the start number : "))  # 100
end = int(input("enter the end number : "))    # 500

for i in range(start,end +1):  # 101 ,501 
    count =0   # count = 0 
    for  j in range(1, i+1):  #  100, 101
        if i % j==0 :         # 100 % 100 ==0 
            count =count +1   # 6 
    if count ==2 :   # 6==2
        print(i,end=" ") #  
        
# hw : pelindrome between two range  

