"""
file  mode  :  txt 

1. read mode  : exiting file open  
2. write mode : new  file create  , write  ,  exiting  overwrite 
3. append mode : new file create  , write , exiting  file  last  add 

"""

# ex :1 write mode  
"""
with  open("soheb.txt","w") as f : 
    f.write("my name is soheb.\n")
    f.write("age is 21.\n")
    f.write("live in ahmedabad.\n")
    f.write("dream to meet  virat kohli.\n")
    f.write("love to play cricket.\n")
    f.close()
"""

# read : 

"""with  open("soheb.txt","r") as f :
    # context =f.read()  # all context  print  
    # context =f.readline()  # first  line read
    context =f.readlines()  # all line  read store  list
    
    print(context)
"""

# append : 

"""with  open("soheb.txt","a") as f : 
    f.write("best friend name is  manthan\n")
    f.write("love pizza.\n")
    f.close()
"""

# r+ : read +write both  
# w+ : new  file  + read +write 
# a+ : new file + read +write 


"""with open("soheb.txt","r+") as f :
    f.write("good boy")
    f.seek(0)  # cursor move to start
    context = f.read()
    print(context)
    f.close()
""" 
#good boy is soheb. 16   -- >8 
    
# w + : new file + read +write

"""with  open("jay.txt","w+") as f :
    f.write("my name is jay.\n")
    f.write("age is 21.\n")
    f.write("live in ahmedabad.\n")
    f.seek(0)
    context = f.read()
    print(context)
    f.close()
"""

# a+ : new file + read +write

"""with  open("jay.txt","a+") as f :
    # f.write("dream to meet  virat kohli.\n")
    # f.write("love to play cricket.\n")
    f.seek(0)
    context=f.read()
    print(context)
    f.close()
"""

# Iterators & GeneratorsTopics:iter()next()enumerate()zip()generator functions with yield

# zip() : 

"""
name =['soheb','jay','manthan','raju','harshita','shruti']
age = [21,22,23,30,22,21]
city = ['ahmedabad','chhattisgarh','bihar','punjab','gujarat','rajasthan']

for i,j,k in zip(name,age,city):
    print(f"name : {i} , age : {j} , city : {k}")
    
"""

# iter() : 
name =['soheb','jay','manthan','raju','harshita','shruti']

# without using  iter() :
"""
for i in name:
    print(i)
"""   
# with using  iter() :

"""def names(n):
    return iter(n)        

demo =names(name)
print(next(demo))
print(next(demo))
print(next(demo))
"""

# generator function :

# without using  yield :
"""def y():
    return 10 
    return 20 

print(y())
"""
# with using  yield :

"""def y():
    
    yield 10
    yield 20
    yield 30
    
demo =y()
print(next(demo))
print(next(demo))
print(next(demo))
"""

# ex :2 

"""def bank_trasaction():
    month =['jan','feb','march']
    amount =[1000,2000,3000]
    
    for  i ,j in zip(month,amount):
        yield f"month : {i} , amount : {j}"
        
b=bank_trasaction()
print(next(b))
print(next(b))
print(next(b))
"""

# enumerate() :

name =['soheb','jay','manthan','raju','harshita','shruti']

"""
0            soheb
1            jay
2            manthan
3            raju
4            harshita
5            shruti
""" 
# without using   enumerate() :
"""
index = 0 
for i in name :   # 
    print(f"index : {index} , name : {i}")
    index +=1
"""   
#with using  enumerate() :

"""for  i  in enumerate(name):
    print(i)
"""
for j in enumerate(name,start=101):
    print(j)