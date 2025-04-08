"""Sets"""

"""sets are printed in sequence in output"""
num={6,5,9,3,3,8,0,2}
str={"Ball","Apple","Cat"}
print(type (num))
print(num)
print(str)

print("\n")

"""To define a Empty set"""
typ={}
print(type(typ))
a=set()
print(type(a))

print("\n")

"""Characteristics of sets
1) Unchangeable 
2) No duplicate 
3) heterogeneous 
4) Not maintain order """

""" We can't change the set 
n={7,5,8,4,9}
n[0]=1
print(n)
"""
n={7,7,7,1,4,4,9} # No duplicate printed
print(n)

hetero={3,6.8,"Apps",True,(2,6)} # we can't print lists becuz it is mutable 
print(hetero)

""" We can't print index becuz order is not maintained 
order={6,4,3,8,8,9,2}
print(order[0])
"""
print("\n")

order={6,4,3,8,8,9,2}
for i in order:
    print(i,end=' ')
    
print("\n")
print(len(order))    

print("\n")

print(8 in order)
print(80 in order)
print(9 not in order)

