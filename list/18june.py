# list  : mutable  sequence  ===> it can be changed 

"""
l1 =[12,34,56,78,90,"ram",90.89,45+8j,True]
print(l1)
print(type(l1))
"""
# access index :  index start 0 
"""
print(l1[0])
print(l1[7])
print(l1[3])
"""
# update  : 
"""
l1[2]="manthan"
print(l1)
"""

# loop  : 
"""for i in l1:
    print(i,end=" ")
"""

# built  in function  : len min max sorted sum  

"""
l1 =[120,34,56,78,90,90.89]

print(len(l1))
print(min(l1))
print(max(l1))
print(sum(l1))
print(sorted(l1))  # asc to desc 
print(sorted(l1,reverse=True))  # desc to asc
"""

# method : append ,copy , pop ,remove 

l1 =[120,34,56,78,90,90.89]

# l1.append(234)  # last added 
# print(l1)

# l2 = l1.copy()
# print("l2 :",l2)

"""
l1.remove(78)  # element  wise  remove 
print(l1)
"""
# l1.pop()  # if  no arg give in pop then  pop remove the  last element automatically .
l1.pop(3)  # remove  index wise 
print(l1)