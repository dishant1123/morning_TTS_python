"""
file handling  : txt

1. read mode   : read only , no new file created , only open exiting file 
2. write mode  : new file created , write , if exiting  file  open in write then its overwrite.
3. append mode : new file created , write , if exiting  file  open in write then its add in the end.

function  : 
1. fopen / with open () : file open  
2. fclose : file close 
3. f.read() : read file  all context 
4. f.readline() : read file  one line
5. f.readlines() : read file  all lines ===> store in list 
6. f.write() : write file
7. f.writelines() : write file  all lines
8. f.seek() : move file pointer
"""
# ex :1 write  mode 

"""
with open("manthan.txt",'w') as f : 
    f.write("my name is manthan.\n")
    f.write("age is 22.\n")
    f.write("live in ahmedabad.\n")
    f.write("dream to meet  virat kohli.\n")
    f.write("love to play cricket.\n")
    f.close()
    
"""

# ex :2 write mode : 

"""file =open("harshita.txt",'w')
file.write("my name is harshita.\n")
file.write("age is 21.\n")
file.write("live in ahmedabad.\n")
file.write("dream to meet  messi.\n")
file.write("love to play football.\n")
file.close()
"""

# ex :3 write  mode  : exiting file open 

"""with open("manthan.txt",'w') as f : 
    f.write("best  friend name is alia.\n")
    f.write("love pizza.\n")
    f.write("hobby is  travelling.\n")
    f.close()
"""

# ex :4 read mode

"""
with open("raju.txt",'r') as f :
    context =f.read()
    print(context)
# note : no  new file created  in read mode only open exiting file for reading.
"""    

# ex :5 read mode  exiting file :

"""
with open("harshita.txt",'r') as f :
    context =f.read()  # read all context 
    context =f.readline()  # read only first line .
    context =f.readlines()  # read all context store in to list  
    print(context)

"""

# ex :6 append mode
"""with  open("manthan.txt",'a') as f :
    f.write("love to play cricket.\n")
    f.write("also watch F1-races.\n")
    
    f.close()
"""

# try except 
"""
try :
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a/b)
except ZeroDivisionError:
    print("you can't divide by zero") 
    """