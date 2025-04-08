"""
WHAT IS OS MODULE ??

The os module in Python provides a way of using operating system-dependent functionality which includes files and directory operations, process management, environment variable and more
We can import the os module usin using:  """

import os

""" If we want to print directory path we use this command """
print(os.getcwd())

"""We can. change the current path directory """
os.chdir("/storage/emulated/0/Python/New fol")

""" If we want to create new folder """
os.mkdir("new_folder") #folder name in parenthesis 

"""To remove the path directory """
os.rmdir("storage/emulated/0/Python/New fol")

"""To create 10 folder named 1 to 10"""
for i in range(1,11):
    os.mkdir(str(i))

"""To create a folders named as python script inside that 10 folder"""
for i in range(1,11):
    os.makedirs(str(i)+"/Python scripts")

""" To print the list of folders in this path"""
print(os.listdir(os.getcwd()))

""" To check whether our folder exist or not """
exist=os.path.exists(os.getcwd()+"/5")
print(exist) #It returns true or false

""" Since above we create 10 folder if we want to append new folder continue to it we write this code"""
for i in range(1,21):
    if (os.path.exists(str(i)+"/Python scripts")==False):
        os.makedirs(str(i)+"/Python scripts")
        
"""check whether path is file or not"""
store=os.path.isfile("storage/emulated/0/Python/New fol")      
print(store)    #It returns true or false    
 
"""check whether path is directory or not"""
store1=os.path.isdir("storage/emulated/0/Python/New fol")      
print(store1)    #It returns true or false    
 
"""Rename file or directory """
os.rename("storage/emulated/0/Python/New fol","New_name728") 

"""Remove the file""" 
os.remove("file_name") 
 
""" For more information visit 
https://docs.python.org/3/library/os.html  """




"""
➤ WHAT IS shutil Module ??

The shutil module in Python provides a high-level interface for file and directory operations.
 This module is useful for directories, as copying, moving, and xemoving files and. archiving them. """

import shutil 

shutil.copy("Existing_path","new_path") #this will copy all folders and files from existing to newpath 

"""By copying exist to new we get the real time in order to make same time on both path we use copy2""" #dealing with time are all metadata
shutil.copy2("Existing_path","new_path")

"""Copying whole directory"""
shutil.copytree("Existing_path","new_path")

""" Moving files and directories"""
shutil.move("Existing_path","new_path")

"""Remove a directory"""
shutil.rmtree("path_name")

""" For Archive any folder/file"""
shutil.make_archive("File name","File type ex:zip","file path")

""" To check usage of disk"""
total,used,free=shutil.disk_usage("E:") #result will come in bytes
print(total,used,free)

""" For more information visit 
https://docs.python.org/3/library/shutil.html """