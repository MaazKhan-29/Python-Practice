#  Loops

# For loop
# syntax : for i in variable_name:

print(range(7))

for i in range(5):
    print(i)
    
print("range(starting,ending,steps)")

for i in range(2,8,2):
    print(i)

print("to print string via loops")    

name="Steve" 
a="Jobs"

for i in name:
    print(i)

for i in a:
    print(i)
    print("@")
    print(" ")     

lst=["Rohan","tope","sam"] 

for i in lst:
    print(i)   

num=[8,6,5,0]  

for i in num:
    
    if i==5:
        print("Lucky number")
    else:
        print(i) 
       
print("nested for loops")  

countries=["Indian","American","Canadian"]
animals=["Cow","Goat"]

for i in countries:
    for j in animals:
        print(i,j)
        
print("Multiplication table ")      

for i in range(10):
    print(f"2*{i}={2*i}")  

print("Reverse Multiplication table ")      

for i in range(10,0,-1):
    print(f"2*{i}={2*i}")  
    
# While loop

# It contains three things initialisation condition increment/decrement 

k="While loop"

i=0
while i<len(k):
    print(k[i])
    i+=1 #i=i+1

print(sep=' ')

x=["gin","chin"]

i=0
while i<len(x):
    print(x[i])
    i+=1

print(sep=' ')

i=0
while i<=4:
    print(i)
    i=i+1

i=0
while i<=4:
    print("Hii")
    i=i+1

print(sep=' ')
   
# Nested while

i=0
j=1

while i<=5:
    print("Hello") 
    
    while j<=2:
        print(j)
        j=j+1 
    
    i=i+1  
    
print("Done")         

print(sep=' ')

i=0

while i<=5:
    print("Hello") 
    
    j=1
    while j<=2:
        print(j)
        j=j+1 
    
    i=i+1  
    
print("Done")         