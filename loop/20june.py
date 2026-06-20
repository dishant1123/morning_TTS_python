"""
reverse  number  :123   ===>321 
rev =0 
1. r = n % 10   ===> r =1% 10 = 1  
2. rev = rev *10 +r  ===> rev =321 
3. n =n //10   ===> n =1 //10 =0

"""

"""n=int(input("enter the  number  : "))   # 1456
rev =0 

while n>0:  # 145 > 0 
    r= n % 10   # r = 1456 % 10 =6
    rev = rev *10 +r  # rev = 6
    n= n//10    # n = 1456 //10 =145 
    
print("reverse is  : ",rev)  # 6
"""

# twin  number  : 
"""
twin number  : 123 
each digit sum  : 1+2+3 ==>6 
each digit  multiply  : 1*2*3 ==> 6 
sum =0 , mul =1
while n >0 :   
step  : 1  r =  n % 10 ===> 1 %10 =1
step  : 2  sum =sum +r  ===> sum = 6
step  : 3    mul = mul *r   ===> mul = 6 
step  : 4  n = n //10  ===> n = 1 //10 = 0

if sum ==mul : 
    print("twin number")
"""

