for i in range(5):
    print(i)
    if i==3:
        break

print(sep=' ')
    
for i in range(5):
    if i==3:
        break
    print(i)  

print(sep=' ')

for i in range(5):
    print(i)
    if i==3:
        break
    print("Hii")    

print(sep=' ')

for i in range(5):
    if i==3:
        break
    print(i) 
    print("Hii") 

print(sep=' ')
    
for i in range(5):
    print(i)
    if i==3:
        continue

print(sep=' ')
    
for i in range(5):
    if i==3:
        continue
    print(i)  
    
print(sep=' ')

for i in range(5):
    print(i)
    if i==3:
        continue
    print("Hii") 
    
print(sep=' ')

for i in range(5):
    if i==3:
        continue
    print(i) 
    print("Hii") 

print(sep=' ')
    
print("While\n")

i=1
while i<=4:
    print(i)
    i=i+1
    
    if i==3:
        break

print(sep=' ')

i=1
while i<=4:
    print(i)
    i=i+1
    
    if i==3:
        break
    print("Hi")    

print(sep=' ')

i=1
while i<=4:
    print(i)
    
    
    if i==3:
        break
    i=i+1
    
print(sep=' ')

i=1
while i<=4:
    print(i)
    
    if i==3:
        break
    i=i+1
    print("Hi")    

print("\n")

i=1
while i<=4:
    print(i)
    i=i+1
    
    if i==3:
        continue            

print(sep=' ')

i=1
while i<=4:
    print(i)
    i=i+1
    
    if i==3:
        continue
    print("Hi")    

print(sep=' ')

""" i=1    #infinite loop 
while i<=4:
    print(i)
    
    
    if i==3:
        continue
    i=i+1 """
    
print(sep=' ')

""" i=1    # It is also infinite loop
while i<=4:
    print(i)
    
    if i==3:
        continue
    i=i+1
    print("Hi")  """    
    
# Pass statement is used when we not decide what statment we have to put in that....
# pass is used to enter our perfect statment when we remember afterwards 

a=10
b=8

if a>b:
    pass
elif b<a:
    pass
    print("Hello")

z="await"    
for i in z:
    pass
    
# Loop else
# to print the else statement the loop should execute successfully 

character=["superman","Spiderman","batman"]  

for i in character:
    print(i)
else:
    print("Done successfully")

print(sep=' ')

for i in character:
    print(i)
    if i=="Spiderman":
        break 
else:
    print("Done successfully")

print(sep=' ')

i=0
while i<=4:
    print(i)
    i+=1
else:
    print("Done")  

print(sep=' ')

i=0
while i<=4:
    print(i)
    i+=1
    if i==2:
        print("found")
        break
else:
    print("Done") 

print(sep=' ')

h=[]        

for i in h:
    print(i)
else:
    print("Correct")