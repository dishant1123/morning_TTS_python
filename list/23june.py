# method : 
l1 =[23,56,78,90,234,67,89]

# append : in last  add element 

"""
l1.append("soheb")
print(l1)
"""
# copy : 
"""l2 = l1.copy()
print("l2=",l2)
l2.append("rajusir")
print("updated l2=",l2)  # updated l2 =[23,56,78,90,234,67,89,"rajusir"]
print("l1=",l1)
"""
# use assign operator  : =   ====> view() create  memory  shared  ===> 1 list  change  2nd list automatically  change

"""l2 =l1 
print("l2=",l2)
print("l1 :",l1)
l2.append("rajusir")
print("updated l2=",l2)
print("l1=",l1)
"""

# insert , pop ,remove : 

l1 =[23,56,78,90,234,67,89]
"""l1.insert(2,"harshita")   # 2 arg  ===> index number , element insert  
print(l1)

l1.pop()   # if  not give arg  then  pop remove the last element
print(l1)

l1.pop(3)  # argument  index wise remove 
print(l1)

l1.remove(234)  # specify  element  remove
print(l1)
"""

# index , extend ,clear : 

"""print(l1.index(234))  # return index number

l2=['apple','mango','banana','orange']
l1.extend(l2)
print(l1)

l1.clear()
print(l1)
"""

# sort :
"""l1.sort()
print(l1)
"""
# reverse :
"""
l1.reverse()
print(l1)
"""

# slicing  : 
# pos index : l to r 
# neg index : r to l
"""l1 =[23,56,78,90,234,67,89]

print(l1[3])
print(l1[2:5])  # start index :2  end index :5 
print(l1[2:])
print(l1[ :6])
print(l1[-1])
print(l1[-3 :])
print(l1[-5 : -3])
print(l1[2 :6:2])  # start index :2  end index :6  step :2
print(l1[1 :-1 :3])  # start index :1  end index :-1  step :3
print(l1[-3 : -5 :-1])
print(l1[ : : 2])
print(l1[ : : 1])
print(l1[ : :-2])
print(l1[ : :-1])
"""
# reverse number using slicing  : 
"""
n=int(input("enter the  number  : "))   # 1456 ===> int 
string_to_int = str(n)
print("number convert in to string : ",string_to_int)   # "1456" 
print(string_to_int[::-1])  # "6541"
"""





