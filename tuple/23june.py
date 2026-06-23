# tuple  : immutable  sequence  ===> it can not be changed 

"""
t1=(12,34,56,78,90,"ram",90.89,45+8j,True)
print(t1)
print(type(t1))

t2 = 12,34,56,78,90,"ram" 
print(t2)
print(type(t2))
"""

# built  in function  : len min max sorted sum

"""
t1=(1112,34,156,178,900,90.89)
print(len(t1))
print(min(t1))
print(max(t1))
print(sum(t1))
print(sorted(t1))  # asc to desc
print(sorted(t1,reverse=True))  # desc to asc
"""

# slicing  :  same as list  
"""
t1=(1112,34,156,178,900,90.89)

print(t1[0])
print(t1[2:5])
print(t1[ : : -1])
"""

# method  : index , count 

t1=(1112,34,156,178,900,90.89,34)

print(t1.count(34))
print(t1.index(34))
print(t1.index(34,2))   #34 value ===> start 2 

"""
Tuple - Theory Questions

1.What is a tuple in Python?
2.What is the difference between a list and a tuple?
3.How do you create a tuple with a single element?
4.Why are tuples immutable?
Answer:
Tuples are immutable to provide:

    Data security
    Faster execution
    Memory optimization
5.What built-in functions can be used with tuples?

Tuple - Practical Questions

1. Find the length of a tuple
2. Reverse a tuple using slicing
3. Count occurrence of a value
4. Find index of an element
5. Find largest and smallest value

Tuple Interview Questions
1.Is a tuple mutable or immutable?
2.Which methods are available in tuples?
3.Can a tuple contain different data types?
4.Why would you use a tuple instead of a list?
5. Can a tuple contain a list?
6.Can we modify a list inside a tuple?
7.What happens if the value is not found in index()?
8.Write a program to find duplicate values in a tuple.
    t = (10,20,30,10,40,20,50)
    output  :[10, 20]
9.Find second largest number in a tuple 
    t = (12,45,78,23,90,56)
    output  : 78

"""
