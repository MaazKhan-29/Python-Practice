"""Tuples Operations and Methods"""

""" We can type cast a tuple to list to perform operation"""
num=(6,9,4,7,9,1)
print(type(num))
n=list(num)
print(type(n))

print("\n")

""" To add new data in tuple"""
numbers=(6,9,4,7,9,1)
print(numbers)
print(id(numbers))
numb=list(numbers)

numb.append(0)

numbers=tuple(numb) # here the numbers variable assign different memory' location
print(numbers)    #This is not the numbers variable as above 
print(id(numbers))

print("\n")

"""To modify the data of tuple"""
x=(8,9,1,5)
print(x)
print(id(x))
y=list(x)

y[0]=50

x=tuple(y) # here the numbers variable assign different memory' location
print(x)    #This is not the numbers variable as above 
print(id(x))

print("\n")

"""Adding two tuple"""

add=num+x
print(add)

print("\n")

"""Deletion of tuple """

g=(2,8,6,9)
del g
# print(g) we can't print() bcuz it gets deleted 
""" All above tuple contains numbers if it contains string then also process will be same"""

print("\n")

"""Count method"""

Naam=("PHONE ","HAI","NHI","HAI","UTT","HAI")
print(Naam.count("HAI"))

"""Index """

Naam=("PHONE ","HAI","NHI","HAI","UTT","HAI")
print(Naam.index("UTT"))
print(Naam.index("HAI"))
print(Naam.index("HAI",3,6))

"""length"""
print(len(Naam)) 

print("\n")

"""list is nested inside tuple hence we can modify data """
nested=(7,2,6,[8,7,0],9,1)
nested[3][1]=45
print(nested)

"""if tuple is nested inside tuple then we can't modify data it shows error"""
"""
nested=(7,2,6,(8,7,0),9,1)
nested[3][1]=45
print(nested)
"""

print("\n")

"""Tuple Unpacking"""

data=(8,7,5)
p,q,r=data
print(p,q,r)

"""If value becomes 4 them we can't assign properly shows error

 data=(8,7,5,9)
p,q,r=data
print(p,q,r)

To solve this we use asterisk to make a list"""

new_data=(3,9,7,0,6)
v,*w,z=new_data
print(v,w,z)

k=(6,9,5,1)
*t,f=k
print(t,f)

print("\n")

"""Packing tuple"""

s=(6,9,4,8,0,1)
print(s)








