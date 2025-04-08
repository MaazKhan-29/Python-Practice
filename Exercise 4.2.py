# Exercise 4.2

# Q) find the leap year

"""Leap Year conditions:

1. If the year is evenly divisible by 4 - Yes

2. If the year is evenly divisible by 100 - No

3. If the year is evenly divisible by 400 - Yes"""

year=int(input("Enter the year: "))

if (year%4==0 and year%100!=0) or year%400==0:
    print("It is leap year")
    
else:
    print("Not a leap year")    
    
# Q2) Tea bill generator 

choice=input("Enter your choice M for Medium and L for Large: ")  
cups=int(input("Enter the number of cups: "))
ginger=input("Want ginger? Y/N: " )

if choice=='M':
    bill=10

elif choice=='L':
    bill=20

if ginger=="Y":
    bill+=5


print("Your Final bill is: ",cups*bill)
    