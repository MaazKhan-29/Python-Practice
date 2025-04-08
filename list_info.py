""" List """
""" List are mutable i.e we can change the given list"""

str=["Rahul","Anil","Rohan"]
num=[1,6,4,9,2,1]

print(str)
print(num)

print(type (str))
print(type (num))
print(len(str))

print("\n")

print(str[0])
print(str[2])
print(num[0])
print(num[2])

for i in str:
    print(i,end=' ')
    
print("\n")
    
for i in num:
    print(i,end=' ')   
  
print("\n")
    
print(str[1:3])     
print(str[0:3:2])
print(str[-3:-1]) 
print(str[-1:-3]) 
print(str[-1:-3:-1])    
print(str[-3::2]) 
print(str[::-1])
"""Similarly for integer list""" 
""" print(str[50]) """ """ Out of range error"""
print(str[0:50]) # in Slicing here also out of range but but don't shows error

"""Use of membership operator"""

if "Anil" in str: 
        print("Present")
else:
        print("Not present")    
        
if "Sunil" not in str: 
        print("Present")
else:
        print("Not present")        

print("\n")

""" Characteristics of list 
1) Mutable 
2) duplicate elements can be print()
3) ordered arranged 
4) heterogeneous  """

name=["Vinod","Binod","Conla"]

name[0]="Boland"
print(name)
# list value change hence Mutable 

n=[1,1,1,1,1]
print(n) # duplicate value can printed

print(name[0]) # ordered arranged 
print(name[1])
print(name[2])

a=["Man",2,5,7.44,True] #heterogenous
print(a)

print("\n")

x=[2,7,[6,0,[5,8,3],4,1],9,4,8]
print(x[2][2][1])
