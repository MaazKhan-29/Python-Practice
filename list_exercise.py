""" Exercise of list"""

"""Enter 3 names and put in list"""

lst=[]
for i in range(1,4):
    name=input(f"Enter the name{i}:")
    lst.append(name)

print(lst)    

print("\n")

""" program to remove duplicate from list and sort in accending"""

num=[2,7,5,0,6,5,0,2,2,5]
newlst=[]

for i in num:
    if i not in newlst:
        newlst.append(i)

print(newlst)  
newlst.sort()
print(newlst)    

print("\n")

""" Fetch the first character from list and make new list"""

list=["Mango","Apple","chiku","guava"]
nawalst=[]

for i in list:
    nawalst.append(i[0])

print(nawalst)

print("\n")

""" Enter 3 names using one input seperated by space and add them to list"""

a=input("Enter the names: ")

new=a.split(" ")
print(new)

