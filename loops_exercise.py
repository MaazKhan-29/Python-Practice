# Exercise 5

"""Print all even number between 1 to 50"""

for i in range(1,51):
    if i%2==0:
        print(i,end=',')

print("\n")

i=1
while i<=50:
    if i%2==0:
        print(i,end=",")
    i=i+1    


print("\n")

""" Sum of all prime numbers between 1 to 50"""

sum=0
for i in range(1,51):
    if i%2==0:
        print(i,end=",")
        sum=sum+i

print("\nSum=",sum)        
        
print("\n") 

i=1
sum=0
while i<=50:
    if i%2==0:
        print(i,end=",")
        sum=sum+i
    i=i+1 

print("\nSum=",sum)        

print("\n") 

"""Search all the number given in list using loops"""

lst=[1,4,8,9,2,6,8]   
key=int(input("enter the number" ))

found=0
for i in range(len(lst)):
    if key==lst[i]:
        print(i+1)
        found=1
        
if found==0:
    print("not found")   
else:
    print("found") 

print("\n")   

lst=[1,4,8,9,2,6,8]   
key=int(input("enter the number" ))

i=0
found=0

while i<len(lst):
    if key==lst[i]:
        print(i+1)
        found=1
    i=i+1    
        
if found==0:
    print("not found")   
else:
    print("found") 

print("\n") 
  
"""Factorial"""

num=int(input("Enter number: ") )

fact=1
for i in range(1,num+1):
    fact=fact*i
       
print("The factorial is: ",fact) 
  
print("\n")  
    
"""Print all prime numbers between 1 to 100"""

i=2
while i<=100:
    j=2
    while j<i:
        if i%j==0:
            break
        j=j+1
    else:
        print(i)  
      
    i=i+1


    