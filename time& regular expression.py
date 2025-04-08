""" Time Module """

"""Time related information:
https://docs.python.org/3/library/time.html """

import time 

print(time.ctime()) #Shows current time

print(time.localtime()) #overall current time structure 
print(time.localtime().tm_mon) #find specific part

print(time.time())  #Shows seconds from 1 jan 1970 called as Epoch 

print("Hello")
time.sleep(0) # waits for 5 second 
print("World")

#To calculate the sleep time
t=time.time()
print("Hii")
time.sleep(0) # waits for 5 second 
print("Everyone")
f=time.time()
total=f-t
print(total)

print(time.strftime("%a %A %b %B %Y %H  %H:%M:%S +0000",time.localtime()))

"""
➤ WHAT ARE REGULAR EXPRESSIONS??

Regular Expressions (often abbreviated as regex) are powerful tools for matching patterns in a string.
They allow to search, match, and manipulate strings based on specific patterns. """

import re

""" Matching """

str="123abc"

result=re.match(r'\d',str)  # \d means checking beginning of str as a first letter whether it contains numbers or not 

if result:
    print(result.group())


result=re.match(r'\d+',str)  # \d+ means checking beginning of str whether it contains numbers or not 

if result:
    print(result.group())
    
str2="abc123"

result=re.match(r'\D',str2)  # \d means checking beginning of str as a first letter whether it contains alphabet or not

if result:
    print(result.group())
        
result=re.match(r'\D+',str2)  # \d means checking beginning of str whether it contains alphabet or not

if result:
    print(result.group())    
 
# Similarly W+ is used for $@#& etc....   
    
""" Searching """

str3="abc123"

result=re.search(r'\d+',str3)  # d+ all numbers the line search the number present!

if result:
    print(result.group())   

str4="abc123ghb657"

result=re.search(r'\d+',str4)  # It search first group of number not further 

if result:
    print(result.group())

str7="788-552-947"

result=re.search(r'(\d+)-(\d+)',str7)  

if result:
    print(result.group()) 
    print(result.group(1))
    print(result.group(2))

str9="abc123ghb657"
str8="179bsj678sdf"

result=re.split(r'\d+',str9)  
result2=re.split(r'\d+',str8)  
print(result)
print(result2)

""" Best Example"""

email = "kode@gurukul.com"
pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'

if re.match(pattern, email):
    print("Email is Valid")
else:
    print("Email is not Valid")
    
""" For more information search for 
python regular expression """


""" Furthermore we have virtual environments studies which I skipped """