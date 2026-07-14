# lambda , map , filter :

# ex :1 filter 
l1= [1,2,3,4,5,6,7,8,9]
"""odd=[] 
even=[] 

for i in l1 :
    if i %2==0 :
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)
"""
"""l1= [1,2,3,4,5,6,7,8,9]
r =list(filter(lambda x :x % 2==0,l1)) 
r1 =tuple(filter(lambda x :x % 2==1,l1)) 

print(r)
print(r1)

"""

# ex :2  div  by  5 or 11 

"""l1=[1,2,33,45,55,70,90]
r2 = tuple(filter(lambda x :x % 5==0 and x % 11==0,l1))
print(r2)
"""

# ex :3 pelindrome string  seperate  

"""l1=["maam","php",'java','.dot','1221','aba']

# hint : [: : -1]
r=list(filter(lambda x : x == x[ : : -1] ,l1))
print(r)

l2=[]
for  i in l1: 
    if i == i[ : : -1]:
        l2.append(i)
print(l2)
"""

# ex :4 map :give a  new list  . 

l1=[3,5,6,9,10]

r=list(map(lambda x : x *5 ,l1))
print(r)

"""
for i in  l1 :   
    print(i *5)
"""

# ex  :5 take a list  and each element  power of  2  