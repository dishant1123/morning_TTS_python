# python  built in module : math ,cmath , random ,datetime ,date ,time,timedelta 

import math as m 

"""print(m.factorial(5))
print(m.sqrt(25))
print(m.pow(5,3))  # base power 
print(m.pi)
print(m.e)
print(m.fsum([12,34,56,78]))
print(m.fsum((12,34,56,78)))
print(m.floor(31.90))  # only  int 
print(m.ceil(31.01))  # given asnwer as round up 
print(m.trunc(31.30))

"""
import random as r
"""
a=r.random()  # 0-1   ===> 1 excluded 
a=r.randrange(1,10,2)  # 1-10  ===> 10  excluded
a=r.randint(1,10)  # 1-10  ===> both  point are included
a=r.choice([1,2,3,4,"manthan","raju",90])
a=r.choices([1,2,3,4,"raju",90],k=3)

print(a)"""

# game  : rock paper scissor
"""
player : user 
player : computer

user_score =0 
computer_score =0
if u==r and c==r or u==p and c==p or u==s and c==s:
    print("tie")

elif u==r and c==p  or u==s  and c==p  or u==r or c==s :
    print("user win")
    user_score+=1

else :
    print("computer win")
    computer_score+=1
"""
"""
def main():
    print("GAME OF ROCK PAPER SCISSOR")
    print("1.ROCK")
    print("2.PAPER")
    print("3.SCISSOR")
    
    choices=['rock','paper','scissor']
    user_score=0
    computer_score=0
    for  i in range(5):
        user_choice=input("ENTER YOUR CHOICE : ")
        computer_choice=r.choice(choices)

        print("COMPUTER CHOICE : ",computer_choice)
        if user_choice==computer_choice:
            print("TIE")
        
        elif user_choice=="rock" and computer_choice=="paper" or user_choice=="scissor" and computer_choice=="paper" or user_choice=="rock" and computer_choice=="scissor":
            print("USER WINS")
            user_score+=1
        else :
            print("COMPUTER WINS")
            computer_score+=1
    
    print("GAME OVER")
    if user_score>computer_score:
        print("USER WINS",user_score)
    else :
        print("COMPUTER WINS",computer_score)

main()
"""
# hw : number  guessing game
"""
1. computer picks a number between 1 to 20  ====> computer guesses 19 
2. user attempts :5 

"""

import datetime as dt

"""today = dt.datetime.today()
print(today)

formated_date = today.strftime("%d-%m-%Y %H:%M:%S")
print(formated_date)

now =dt.datetime.now()
print(now)

custom_date = dt.datetime(2022,7,21,12,30,45)
print(custom_date)
print(custom_date.day)
print(custom_date.month)
print(custom_date.year)
print(custom_date.hour)
print(custom_date.minute)
print(custom_date.second)
"""
# time  : 

import time as t

"""time = t.time() # search EPOCH time  
print(time)

local_time = t.localtime()
print(local_time)

asctime = t.asctime()
print(asctime)
"""

# sleep :

"""for i in range(10):
    t.sleep(0.5)
    print(i)
"""

# timedelta : 
"""from datetime import timedelta

today = dt.datetime.today()
future = today + timedelta(days=90)

print(today)
print(future)
"""

# custom module  : hw  
"""
1. utils.py   ====> function  : 1.calculate_of_percent 2. subjects() 3 .grades()
2.main.py  
"""

# regex : 

import re

"""text = "Contact us at support@example.com or sales@company.org. Phone: 123-456-7890."
phone_pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(phone_pattern, text)
print(match.group())
"""

l1=[1,2,3,4]
l2=["apple","mango","orange","banana"]

# pop method in list 
# can convert tuple in to list 
# enter :s1= my name is  shrutika. ===> reversed string  
#        s1.count("a",4,40)  ===> output ???

# pratical  :
"""
1. ask user to enter the 5 element store in to the  list  and print  reverse order to another  list .

input : l1 =["raju","ram","sita","ravan"]
output : l1 =["ujar","mar","atis","navar"]
"""

# shoheb : 
"""
python is  object oriented programming language ??  -->no
what is  frozenn set ?? -->immutable 
can i store repeated element in set ??-->no  

d1 ={"phy" :90 ,"che" :89}   i want  update phy marks with  99  ?? and i also add the  com  in d1.--->  d1['com']=78 

s1="my name is shoheb."
print(s1.rindex("h"))   ---> output   ?? 
print(s1.index("h"))   ---> output   ?? 

in dict why we use items() method ?? --> key values 

pratical :

1. ask user to enter the 5 element store in to the  list  and print  pelindrome number   to another  list .

input : l1 =[123,456,789,121,131]
output : l1 =[121,131]

#raju : 
t1 =12,2,3,4,5,6,7,8,9,10
print(t1)
print(type(t1))

s1= "my name is shoheb"  ===>print(s1[ : : -1])

l1= [1,2,3,4,5,6]
print(l1[-3])  ===> what remove method in list  ?? pop method l1.pop(2),l1.remove() 

Find second largest number in a tuple 
    t = (12,45,78,23,90,56)
    output  : 78

"""

