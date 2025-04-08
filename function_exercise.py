""" Function Exercise """

""" Q1) Find factorial """

def factorial(n):
    fact =1
    for i in range(n,0,-1):
        fact=fact*i
    return fact    
        
print(factorial(5))

""" Q2) Fibo """

def Fibo(n):
    if n<=1:
        return (n)
    else:
        return (Fibo(n-1)+Fibo(n-2))   
    
for i in range(10):
    print(Fibo(i),end=" ")

print("\n")

""" Q3 We have two lists:

#id= [1,2,3]
#names ["Rahul", "Sam", "Steve"]
# Write a Program to create a list of tuples so that each tuple contains one
#element from the first list and a second element from the second list.
# You can use Map, Filter, or Reduce. """

name=["Cat","Dog","Horse"]
number=[2,6,4,3]

a=map(lambda x,y : (x,y),name,number)
print(list(a))

""" #Q4 Write a Program to Convert the below list of names to Upper case.
#names = ["Rahul", "Sam", "Steve"]
"""
names = ["Rahul", "Sam", "Steve"]

z=map(lambda x : x.upper(),names)
print(list(z))




