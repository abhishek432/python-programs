import os
os.chdir(r"C:\Users\M1073167\Desktop")

#reading of file--
"""
#file = open('test123.txt', 'r')
#print(file.read())
#for x in file:
#    print(x)
"""

#append of flie---
"""
file=open("test123.txt",'a')
file.write("hello this is new line")
file.close()
file = open('test123.txt', 'r')
print(file.read())
"""
#deletion of text file
            #eg-1---
"""
os.remove('')
"""
            #eg-2----
"""
if os.path.exists(''):
    os.remove('')
else:
    print("path is unavailable")
"""
#File handling program-
#python program to read a file word by word---

"""
f=open("test123.txt","r")
for line in f:
    for word in line.split():
        print(word)
"""


#python program to read file by character by character-
"""
f=open("test123.txt","r")
for line in f:
    for word in line:
        for character in word.split():
            print(character)

"""
#python code to count no lines in txt file
"""by method 1"""
"""
f=open("test123.txt","r")
count=0
con=f.read()
colist=con.split("\n")
for i in colist:
    if i:
        count+=1
print("No of liness in file: ",count)        
"""

"""by method 2 """

"""
f=open("test123.txt","r")
count=0
for i in f:
    count+=1
print("No of liness in file: ",count)

"""








