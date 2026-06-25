# list  : mutable  sequence  ===> it can be changed
# tuple : immutable  sequence  ===> it can not be changed

# dict : mutable  ===> key value pair 

"""
d1 ={"phy" : 90, "che" :89 }
# phy  key  value :90   che key  value  89 
print(d1)
print(type(d1))

d2 = {80 :78 , "ram" :99}
print(d2)
print(type(d2))   # you can take  any value  of  key  not specify to take string . 

"""

# update : 
"""
d1 ={"phy" : 90, "che" :89 }
d1['che']=99
print(d1)
"""
# add : 
"""
d1['com'] =67 
print(d1)
"""

# built  in function  : len min max sorted sum

"""
d1 ={"phy" : 90, "che" :89 }
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  # asc to desc
print(sorted(d1,reverse=True))  # desc to asc
"""

# you can't access though the  index for dict  and slicing not  possible in dict . 

"""
d1 ={"phy" : 90, "che" :89 }
print(d1[0])
"""

# method : 
d1 ={"phy" : 90, "che" :89 }

# d1.clear()   # clear all the key value pair
# print(d1)

"""d2 =d1.copy()
print(d2)
d2["com"] =90
print("d2 :",d2)
print("d1 :",d1)

d2 =d1 
d2['com'] =90 
print("d2 :",d2)
print("d1 :",d1)
"""

"""print(d1.keys())
print(d1.values())
print(d1.items())

for i ,j  in d1.items(): 
    print(i,j)
"""

# task  : 1  ask user to enter the 3 student name and marks store in to the dict . 
"""
ram  sita  ravan
90    99     78 
output  : {'ram': 90, 'sita': 99, 'ravan': 78}
hint  : to empty dict   add  

"""
d1={}    # d1['name'] = marks 
for i in range(3) :  # name marks 
    name = input("enter the name : ")
    marks = int(input("enter the marks : "))
    d1[name] = marks
print(d1)