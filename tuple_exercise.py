"""Fibonacci series"""

a=0
b=1
n=int(input("Enter number:"))
lst=[a]

for i in range(n):
    s=a+b
    a=b
    b=s
    
    lst.append(a)  

print(lst) 

"""Remove empty tuples from list"""

data=[(),(3,7,9),(),(7,5,1),()]
list=[]

for i in data:
    if len(i)!=0:
        list.append(i)
        
print(list)        