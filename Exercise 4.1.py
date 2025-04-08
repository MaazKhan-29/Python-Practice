# Exercise 

# Find the number is odd or even

n=int(input("Enter the number:"))

if n%2==0:
    print("Number is even")
else:
    print("Number is odd")
    
# Enter age of 3 friends and find the youngest among them

person1=int(input("Enter the age of person 1: "))
person2=int(input("Enter the age of person 2: "))
person3=int(input("Enter the age of person 3: "))

if person1<person2 and person1<person3:
    print("person 1 is youngest")

elif person2<person1 and person2<person3:
    print("person 2 is youngest")
 
elif person3<person2 and person3<person1:
    print("person 3 is youngest")
     