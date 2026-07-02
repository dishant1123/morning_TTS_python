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

# task :1 
"""
s1 ="dishant dipakkumar shah"
result = s1[0] +"." + s1[8]+ "." +s1[19: ]
print(result)
"""
# task :2 

# s1=input("enter first string : ")  # manthan
# s2=input("enter second string : ") # patel 

# s1 = s1[0 :3] + s2[3:]   # man 
# s2 = s2[0 :3] + s1[3 :]

# task :3 

"""s1="restart"
s2 =s1[0]  # r 
result = s2 + s1[1:].replace("r","@")
print(result)
"""

# task :4 
"""s1="my name is manthan patel."

result =s1.replace(" ","_",1)
modify_string  = result[ : : -1].replace(" ","_",1)[ : : -1]
print(modify_string)

"""

# task :5 
"""
count  the vowel in string. 

input  : my name is manthan patel.
output : vowel count :7

hint : for   , ===> vowel = "aeiouAEIOU" , if  ,count+ ,print(count)
"""

"""s1 ="my name is manthan patel."  # input("enter string : ")
vowel = "aeiouAEIOU"
count =0 
consonant_count =0 
for i in s1:   #  i
    if i in vowel :  # if i in  
        count +=1   # 1
    else :
        consonant_count +=1  # 2
print("vowel count :",count)
print("consonant count :",consonant_count)
"""

# task :6 print pelindrome string in separate list.
"""
l1 =["maam","php","java","c++","python"]
output  : ["maam","php"]

"""
# l1 =["maam","php","java","c++","python"]

l1=[121,1345,234,678,141]
result=[]

for x in  l1 :   # 121
    if str(x) ==str(x)[::-1]:  # "121" == "121"[::-1]
        result.append(x)
print(result)

# task :7 
"""
input  : l1 =["maam","php","java","c++","python","1221","aba"]
output : l2 = ["maam","php","java","aba",1221]

condition  :1. len more than 3  and  equal to 3  
            2. first letter and last letter same. 
"""





