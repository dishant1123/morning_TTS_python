# string  slicing  : 

"""
s1 ="my name is manthan patel."
#    01234 ..........     ===> l to  r 
# neg index :   r to l       -1
print(s1[0])
print(s1[1:4])  # start  index 1  end index 4   y n 
print(s1[ :8])
print(s1[2:])
print(s1[-2])
print(s1[2 :8 :2])# start index 2 end index 8 step 2
print(s1[1 :10 :3])# start index 1 end index 10 step 3
print(s1[ : : 1])
print(s1[ : : -2])
print(s1[ : : -1])
"""
# method : 

s1 ="my name is Manthan Patel."

"""print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.swapcase())
print(s1.capitalize())
"""

# index , rindex ,find, rfind : 

s1 ="my name is Manthan Patel."

"""print(s1.index("i"))
print(s1.index(" "))
print(s1.index(" ",3,10))
print(s1.index("a"))
print(s1.index("a",5,20))
print(s1.index("is"))
print(s1.index("Manthan"))

print(s1.rindex("a"))   # right  to  left 

print(s1.find("i"))
print(s1.find(" "))
print(s1.find(" ",3,10))
print(s1.find("a"))

print(s1.rfind("a"))
"""
# hw :  what is  the  difference  between  find  and  index , rindex and  rfind ??

# replace ,split ,count ,partition : 

s1 ="my name is Manthan Patel."

"""print(s1.replace("Patel","shah"))
print(s1.replace(" ","-",1))
print(s1.replace(" ","-",2))
print(s1.replace(" ","-",4))

print(s1.split())  # give list  
print(s1.split("a"))

print(s1.partition("a"))   # always 3 parts answer give in tuple . 
print(s1.partition("is"))
print(s1.rpartition("a"))

"""

"""
task :1  use slicing . 

input  : "dishant dipakkumar shah"
output : d.d.shah

task :2 ask user to enter the two  string  and  swap the  first three character of  second string with  the first three character of first string .
hint  : slicing  + concat  

input a : color 
input b : full 

output a :fulor 
output b : coll

task :3 replace the  second  "r" with "@". 
hint   : replace method  

input : "restart"
output : "resta@t"

task :4  ask user to enter the string and  replace first  and  last space  with underscore "_".
hint  : replace  +  slicing   ===> reverse logic 

input  : my name is manthan patel.
output : my_name is manthan_patel.

"""
