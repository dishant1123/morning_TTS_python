"""
set : mutable , unordered collection of unique elements, no repeation allowed in set. 
"""
"""
s1 ={100,2,3,3,30,4,5,67,89,90,100}   
print(s1)
print(type(s1))
"""
# no index and slicing  in set . 
"""
s1 ={100,2,3,3,30,4,5,67,89,90,100}   

print(s1[0])  # not  possible in set . 
print(s1[2:4])
"""
# built  in function  : len min max sorted sum

"""
s1 ={100,2,3,3,30,4,5,67,89,90,100}   

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to desc
print(sorted(s1,reverse=True))  # desc to asc
"""

# convert dict  to set : 

"""d1={"phy" : 90, "che" :89 }
print(d1)
print("convert dict to set :",set(d1.items()))

l1= [12,34,56,78,12,34,45,34]
print(l1)
print("convert list to set :",set(l1))
"""
# method :

s1 ={100,2,330.90,4,5,67,89,90,100,"hkl",(67,90)} 
print(s1)  
"""
s1.add(234)
print(s1)

s1.clear()
print(s1)  #set() ===> empty set

s2 =s1.copy()
print(s2)
"""
# pop ,remove,discard : 
"""
s1 ={100,20,3,3,30,4,5,67,89,90,100}   

s1.remove(100)# specific element  remove  but not  exist  element then give error.
print(s1)

s1.discard(2000)  # specific element  remove  but not  exist  element then return same set.
print(s1)

s1.pop()
print(s1)  # any element  remove from set
"""

# union , intersection , difference , symmetric_difference  : 
"""
s1={1,2,3,4}
s2={4,3,9}
s3={1,2,3,4,5,6,7,8,9}

print(s1.union(s2))  # print all  element  from  set  1 and  2
print(s1.intersection(s2))  # print  common  element  from  set  1 and  2
print(s1.difference(s2))  # s1-s2  common element remove  and remaining element print from s1
print(s1.symmetric_difference(s2)) # s1-s2 common element remove  and print remaining element  from s1 and s2 
"""
# isdisjoint , issubset , issuperset  :

"""s1={1,2,3,4}
s2={9}
s3={1,2,3,4,5,6,7,8,9}

print(s1.isdisjoint(s2))  # check  if  set  1 and  2  have  no  common  element.
print(s1.issubset(s3))  # check  if  set  1  is  subset  of  set  3   check if all  element  from  set  1  present  in  set  3.

print(s3.issuperset(s1))  # check  if  set  3  is  superset  of  set  1   check if all  element  from  set  3  present  in  set  1.

"""

# frozenset : imuutable , unordered collection of unique elements, no repeation allowed in frozenset.

fz =frozenset({10,2,2,3,3,4,4,5,5,6,7})
print(fz)
print(type(fz))


# frozenset : no index and slicing  in frozenset .