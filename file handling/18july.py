# file handling tasks : 
"""
1. ask user to  enter the string  and  seprate the  vowel and  consonant in seprate  txt file .

input : my name is harshita singh. 
output  : vowel.txt : ae i aia i
          consonant.txt : my nm s hrsht sngh.


"""

"""s1=input("enter the string : ")  # my name is harshita singh.

for i in s1 :
    if i in 'aeiouAEIOU' :
        with open("vowel.txt","a") as f :
            f.write(i)
    else : 
        with open("consonant.txt","a") as f :
            f.write(i)

"""

# 2. ask user to enter the string and seprate the vowel and consonant in seprate txt file.and  count the total vowel and  consonant.

"""
3. ask user to enter the  string and count  the total words , number of statements in separate  txt file.

input : my name is harshita singh.
        i love to play football.
        study in college.
        live in ahmedabad.
        
output : total number of  words : 16 
         total number of  statements : 4
"""

s1="my name is harshita singh."

result = s1.split()
print(result)
total_words = len(result)
print(total_words)