""" Enumerate """

index=1
lst=["One","Two","Three","Four"]
for i in lst:
    print(index,i)
    index=index+1

print("\n")    
"""The above code can be done by enumerate """
    
for i in enumerate(lst):
    print(i)  

print("\n") 
for unpack,i in enumerate(lst):
    print(unpack,i)  

print("\n")     
for i in enumerate(lst,100):
    print(i)      
 
print("\n")     
print(list(enumerate(lst)))

print("\n") 


""" Walrus Operator"""

a=5*5
print(a) 

# print(a=6*6)  using assignment operator in print statement is not applicable 
# To solve this issue walrus Operator comes ahead

print(a:=6*6) #Done✅ 
print("\n")

"""Ex2"""

number=input("Enter the number: ")

if (number.isdigit()):
    print("The number is: ", number)
else:
    print("invalid number")

"""Above code can be done as """
print("\n")

if (number:=input("Enter the number: ")).isdigit():
    print("The number is: ", number)
else:
    print("invalid number")

"""Ex3"""

data=["Horse","Cat","lion"]

for i in data:
    if (length:=len(i))>3:
        print(f"{i} has {length} characters")
    


