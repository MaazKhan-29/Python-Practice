""" Exercise of dictionary"""


"""
Question 1

Below we have marks of 3 student. Write a program to remove students 
from last to first and print them side by side.

marks = {"Rohit": 80, "Rahul": 85, "Steve": 70}
"""


marks = {"Rohit": 80, "Rahul": 85, "Steve": 70}

while marks!={}:
    res=marks.popitem()
    print(res)

print(marks)    

print("\n")

"""
Question 2

Below we have dictinary of student with marks in 3 Subjects.
 Find out the average marks and total marks and add them for
  each student and find the topper of the class.

students = { "Rohit": {"English": 70, "Maths": 85, "Science": 85),
 "Rahul": {"English": 60, "Maths": 80, "Science": 70),
  "Steve": {"English": 90, "Maths": 85, "Science" : 80}}
  
 """   
  
students = { "Rohit": {"English": 70, "Maths": 85, "Science": 85},
 "Rahul": {"English": 60, "Maths": 80, "Science": 70},
  "Steve": {"English": 90, "Maths": 85, "Science" : 80}}

topper=""
topper_marks=0
  
for i,j in students.items():  # i=name ,j=subjects, k=marks
    print(i,j)
    
    total=0
    average=0
    for k in j.values():
        print(k)
        
        total=total+k
        average=total/3
    print("Total:",total,"\n","Average:",average)
    
    students[i]["TOTAL"]=total
    students[i]["AVERAGE"]=average 
    
    if total>topper_marks:
        topper_marks=total
        topper=i
    
print(students)  
print(topper_marks)
print(topper)
        
        
  
        