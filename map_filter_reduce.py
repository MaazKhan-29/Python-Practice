""" Map / Filter / reduce """

""" if there is a function and Loop we use map  """

""" normal """

numbers =[2,7,6,9,5,1]
number_2=[]

def square(x):
    return x**2

for i in numbers:
    number_2.append(square(i))
    
print(number_2) 

""" above code using map """

# way 1
numbers =[2,7,6,9,5,1]
number_2=[]

def square(x):
    return x**2
    
number_2=map(square,numbers) 
print(list(number_2))  # Note: typecasting 

# way 2
number_2=map(lambda x : x**2,numbers) 
print(list(number_2))  # Note: typecasting 


""" Filter """

new_number=[7,6,9,5,4]

def find(x):
    if x%2==0:
        print("Even")
    else:
        print("odd")  

find(2)
            
""" using filter"""

# way 1
z=[7,6,9,5,4]

def find(x):
    if x%2==0:
        return True
    else:
        return False 
        
a=filter(find,z) 
print(list(a))  # Note: typecasting   

# way 2
a=filter(lambda x : True if x%2==0 else False,z) 
print(list(a))  # Note: typecasting   


""" Reduce() """

from functools import reduce

def add(a,b):
    return a+b
    
red=[6,4,6,9,8,2]    

#way 1
result = reduce(add,red)     
print(result)  # Note : Not typecast

#way 2
result = reduce(lambda a,b : a+b,red)     
print(result)  # Note : Not typecast

        
    