""" Sets Methods"""

num={6,5,9,3,3,8,0,2}
str={"Ball","Apple","Cat"}
print(type (num))
print(num)
print(str)

print("\n")

"""Add"""

num.add(60)
num.add((40,50)) # tuple added into set as it is
print(num)

print("\n")

"""Update"""

n={6,53,0,8,4,5,58}
"""n.update(7)""" # We can't update single element 
n.update((40,50)) # TUPLE update into by opening it's brackets 
print(n)

print("\n")

"""Remove and discard"""

s={8,6,4,7,5,3,9}
print(s)
s.remove(6)
s.discard(9)
""" Both remove and discard work as same but only difference at out of range time """
print(s)

""" s.remove(80) """ # show error 
s.discard(90) # even it is out of range but don't show erroe
print("set printed even discarded 90",s)

print("\n")
"""pop"""

p={7,6,9,5,1}
p.pop()
print(p)
p.pop()
print(p)

print("\n")

set1={2,7,6,8,9,20}
set2={9,6,9,4,8,40}

"Union" #Combine both set

#way1
result=set1|set2
print(result)

#way2
res=set1.union(set2)
print(res)

#way3
set1.update(set2)
print(set1)

set3={2,0,6,8,9,20}
set4={9,6,9,4,8,40}

print("\n")

"""Intersection""" #output of common elements 

#way1
result=set3&set4
print(result)

#way2
res=set3.intersection(set4)
print(res)

#way3
set3.intersection_update(set4)
print(set3)

set5={2,7,6,8,9,20}
set6={9,6,9,4,8,40}

print("\n")

"""Difference""" #set5-set6 print the value other then common one 

#way1
result=set5-set6
print(result)

#way2
res=set5.difference(set6)
print(res)

#way3
set5.difference_update(set6)
print(set5)

set7={2,7,6,8,9,20}
set8={9,6,9,4,8,40}

print("\n")

""" Symmetric Difference""" #set5-set6 print the value other then common one 

#way1
result=set7^set8
print(result)

#way2
res=set7.symmetric_difference(set8)
print(res)

#way3
set7.symmetric_difference_update(set8)
print(set7)

print("\n")

clr={7,48,9,6,7,}
clr.clear()
print(clr)

print("\n")

x={3,8,7,9}
y=x
print(id(x))
print(id(y))

print("\n")

u={3,8,1,9}
v=u.copy()
print(id(u))
print(id(v))

