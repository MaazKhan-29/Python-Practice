""" Exercise of set """

""" Question 1

We have a set containing names starting with P and S. Write a program
 to create two sets, one with names starting with P and other with names from S.

names = {"Parag", "Sundar", "Sandeep", "paras", "svarg"}
"""

names = {"Parag", "Sundar", "Sandeep", "paras", "svarg"}
set1=set()
set2=set()

for i in names:
    if i.upper().startswith("P"):
        set1.add(i)
        
    elif i.upper().startswith("S"):
        set2.add(i)    
        
print(set1)        
print(set2)

""". Question 2

A Poll is conducted in company to name their new car with 1000cc engine
. We got 20 suggestions, write a program to find the unique suggestions.

names = ["150", "XUV1000", "Hinge", "Grand 1000", "myRider", "150"
, "XUV1000", "Hinge", "Grand 1000", "myRider","150", "XUV1000", 
"Hinge", "Grand 1000", "myRider", "150", "XUV1000", "Hinge", "Grand 1000", "myRider"]
"""

names = ["150", "XUV1000", "Hinge", "Grand 1000", "myRider", "150"
, "XUV1000", "Hinge", "Grand 1000", "myRider","150", "XUV1000", 
"Hinge", "Grand 1000", "myRider", "150", "XUV1000", "Hinge", "Grand 1000", "myRider"]

new=set(names)

print(new)

""" Use of superset and subset """

a={2,3}
b={2,3,6,8}

print(a.issubset(b))
print(b.issubset(a))

print(a.issuperset(b))
print(b.issuperset(a))




