"""
FILE HANDLING

In Python, we can perform operations on external files like. text files, audio/video files and images. 
In general, we have two types of file Categories

(1) Text: txt, Programs, word documents etc
(2) Binary: Images, Music, Videns etc.

Common Operations are performed on these files like: Open/Create, Read, Write, Delete. """




"""
Open file syntax:
file=open("Path name : Absolute or relative","mode")
absolute:link of that text file.
relative:name of the file
mode='r':read,'w': write,'a':append etc

"""



"""
Method to read the file content : read(), readline(), readlines()
read(): reads all the line as it is
readline(): read the line one by one 
readlines(): reads all the line but outputs in form of list

we can use for loop to remove the list
Ex: file name:aiktc\t.txt
file = open(r"aiktc.txt",'r')
data=file.readlines()

for i in data:
    print(i)
file.close()
    
"""



"""
Method to write in the file content : write(), writelines()
write(): write the content 
writelines(): when input content is in form of list we use this 

mode='w'

"""



"""
try:
    file name:aiktc\t.txt
    file = open(r"aiktc.txt",'r')
    data=file.readlines()

    for i in data:
    print(i)
    print(6/0)
except:
    file.close()

Here 6/0 line makes error and due to this the file will not be close
hence we use file exception method to overcome this 

"""


"""
We have to write close statment again and again 
instead writing again we use with open syntax 

Ex: with open("file name","mode") as f:
    f.read()

"""

"""
Use of tell() and seek() 

tell()=says the index number of cursor 
seek()=we can move cursor according to our convenience like to make cursor to move it's 
      initial point we use. seek(0) & it also return its own value 
      
Suppose a text file is created named readme.txt inside we written Super on first line and hero on second line 
Making another file as file_handling.py where we supposed to write code

with open(r"file_handling.py") as f:
    print(f.tell())  // Output:0
    print(f.read())  // Output:Super \n hero
    print(f.tell())  // Output:11(super=5,hero=4, initial and end=2)
    print(f.seek(6)) // Output:Super(only super)
    print(f.tell())  // Output:8
    print(f.read()). // Output:Super Super hero
"""

"""
Deletion of file

import os
os.remove(r"readme.txt")

Another way!

if os.path.isfile("readme.txt"):   // File checking existing or not
    os.remove("readme.txt")
else:
    print("File not exist")    
"""    