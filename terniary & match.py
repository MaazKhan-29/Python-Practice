"""Terniary operation """

""" Below code is normal without using terniary"""

salary=25000
rating=int(input("Enter your rating: "))

if rating>8:
    bonus=10000

elif rating>6:
    bonus=5000
    
else:
    bonus=2000
    
salary=salary+bonus
print(salary)    
    
""" implementation of Above code using terniary operation """

new_salary=25000
new_rating=int(input("Enter the rating "))

new_bonus=10000 if new_rating>8 else 5000 if new_rating>6 else 2000
""" or

print(10000) if new_rating>8 else print(5000) if new_rating>6 else print(2000)
"""

new_salary=new_salary+new_bonus
print(new_salary)

"""match case (not available in this version)"""
"""
number=int(input("Enter the operator"))

match number:
     case 1:
     print("One")
     
     case 2:
     print("Two")
     
     case 3:
     print("Three")
     
     case 4|5
     print("Four and Five")
     
     case number if number>9 and number<15
     print("9++")
     
     case _:
     print("Invalid")
"""
