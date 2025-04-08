""" File handling Exercise """

""" Question 1
We have a list of students. Write a program to store this list in a file.
Our program should be able to print the nth name from the list where the user enters n.
#students ["Sandeep", "Aman", "Steve", "Bill", "Rahul"]
"""

"""
def detail(students):
    with open(r"new_file.txt","w") as f
    for i in students:
        f.write(i+"\n")

def printing():
    n=int(input("Enter the number to print that name"))
    with open(r"new_file.txt","w") as f
    store=f.readlines()
    print(store(n-1))


students=["Sandeep", "Aman", "Steve", "Bill", "Rahul"]
detail(students)
printing()

"""


""" Question 2
#Write a program to search for the word "Kode" from the file and
print the line numbers containing the word (create text file named as info.txt and enter one Code gurukul and next line Kode gurukul and repeat 1 more time)
"""
"""
def info(str):
    text=" "
    line=1
    
    with open("info.txt","r") as f:
        
        while text:
            text=f.readline()
            if str in text:
                print(line)
            line=line+1
            
                
info(Kode)
"""

""" Question 3
We have the below text in the file, copy this content to a new file replacing the word
"code" with the "Kode".

Code Gurukul
Kode Gurukul
Code Gurukul
Kode Gurukul
"""

"""
def replace():
    with open("info.txt","r") as f:
        store=f.read()
        new_store=replace("Code","Kode")
        with open("new_info.txt","w") as f:
            f.write(new_store)
            
replace()

"""