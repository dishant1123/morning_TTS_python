"""
employees management system

1. add employee
2. delete employee
3. update employee
4. search employee
5. display employee
"""
"""
d1={}

def emp_add():
    id=int(input("enter employee id : "))
    name=input("enter employee name : ")
    salary=int(input("enter employee salary : "))
    d1[id] =[name,salary]

def emp_update():
    id =int(input("enter employee id you want to update : "))  # 1 
    if id in d1 : 
        new_name=input("enter new name : ")
        new_salary=int(input("enter new salary : "))
        d1[id][0]=new_name
        d1[id][1]=new_salary
    else :
        print("no such employee exist")

def emp_del():
    id =int(input("enter employee id you want to delete : "))  # 1 
    if id in d1 : 
        del d1[id]
    else :
        print("no such employee exist")
        
def emp_search():
    id =int(input("enter employee id you want to delete : "))  # 1 
    if id in d1 : 
        print(d1[id])
        print("name : ",d1[id][0])
        print("salary : ",d1[id][1])
    else :
        print("no such employee exist")
        
def emp_display():
    print("khud  logic lagaoooo.")
    
def main():
    while True:
        print("1.add employee")
        print("2.delete employee")
        print("3.update employee")
        print("4.search employee")
        print("5.display employee")
        print("6.exit")
        choice =int(input("enter your choice : "))
        if choice==1:
            emp_add()
        elif choice==2:
            emp_del()
        elif choice==3:
            emp_update()
        elif choice==4:
            emp_search()
        elif choice==5:
            emp_display()
        elif choice==6:
            break
        else :
            print("enter correct choice")

main()
"""
# bank app : 
"""
1. create  account  : 
    create the  username :- dishant
    create the password :- Dish@1211       (con : 1 upper,1 lower,1number ,1 special )
2. login  account:
    enter the  username  :- dishant
    enter the password :- Dish@1211
    login  success :: ac :25000
    
1. deposit   : 1 ====> 5000 
2. withdraw  : con  : min 10000 stay in your account
3. check balance :
4. exit 
    

"""

# recurive  function  : function  calling  itself

# ex :1   factorial  
"""
5! = 1*2*3*4*5 =120 
6! = 1*2*3*4*5*6 =720

n = n * (n-1)!   = 5 * (4)!
"""
"""def facto(n):
    if n==1 :
        return 1
    else :
        return n * facto(n-1)
num=int(input("enter the number : "))
print(facto(num))
"""
# ex :2 n natural number sum 
"""
def sum1(n):
    sum =0 
    for i in range(1,n+1):
        sum =sum +i 
    return sum 
print(sum1(5))"""

def n_sum(n):  # 4 
    if n==1 :  
        return 1
    else :
        return n + n_sum(n-1)  # 5 + n_sum(4)   4 + n_sum(3)
    
print(n_sum(5))