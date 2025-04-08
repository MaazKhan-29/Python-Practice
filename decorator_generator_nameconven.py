"""
➤ WHAT ARE DECORATORS??

Decorators are powerful tools that allow us to modify or extend the behaviour of functions without changing their actual code.
They are the functions that wrap another functions, adding Some kind of functionality  before or after the wrapped function is called

➤ How To USE IT

A decorator is applied to a function using the @decorator-names placed above the function """

def greet(func):
    def wrap():
        print("Welcome")
        func()
        print("Bye")
    return wrap    

@greet
def data():
    print("Hello how are you")        

@greet
def data2():
    print("Nice to meet you")
    
def data3():
    print("This how without decorator work")    
    
data()
data2()
data3=greet(data3)
data3()
print("\n")

""" use of decorator by passing arguments"""

def calculate(fun):
    def wrap(x,y):
        print("Start")
        fun(x,y)
        print("End")
    return wrap    
 
@calculate    
def add(a,b):
    print(a+b)

add(5,5)

"""
►WHAT ARE GENERATORS ??

In Python, a generator is a function that generates a sequence of values on demand, one at a time. Generators are a type of iterable, similar to lists or tuples, but they don't store all values in memory at once. 
How do generators work? 
Generators use the yield statement instead of the return statement.
Generators produce values on the fly as you iterate over them.
Generators pause their state between each yield."""

import sys

lst=[]
def calcu():
    a=list(range(1,50))
    for i in a:
        lst.append(i**2)
    return lst
    
storing=calcu()
print(storing)

for i in storing:
    print(i)

print("\n",sys.getsizeof(storing))

""" With return statement we get size as 520"""

def cal2():
    a=list(range(1,50))
    for i in a:
        yield (i**2)
        
save=cal2()
print("\n",sys.getsizeof(save)) #Due to generator size gets reduced 
print(next(save))  #Output comes step by step as a single value
print(next(save))  
print(next(save))  # The last value gets saved 

print("\n")
for i in save:   #Since last value is 9 now loop starts after 9 this is the main advantage of generators 
    print(i)
    
"""Use of generators as counter"""

def infinite_count():
    count=0
    while True:
        yield count
        count=count+1   
    
count=infinite_count()
print(next(count))
print(next(count))
print(next(count))
    
"""Another example with file"""

""" Consider we have a text "Hello everyone" 10 times in text file named as test.txt 
we can use generator to print them one by one """

def file(file_name):
    with open(file_name,"r") as f:
        for i in f:
            yield i

content=file("test.txt")
print(next(content))


""". Python Naming Conventions

1. Variables & Functions → lowercase_with_underscores (e.g., student_name, calculate_total()).

2. Constants → ALL_CAPS_WITH_UNDERSCORES (e.g., PI = 3.14).

3. Classes → PascalCase (e.g., StudentDetails).

4. Modules & Packages → lowercase_with_underscores (modules) / lowercase (packages).

5. Private Members → _single_leading_underscore (e.g., _hidden_var).

6. Strongly Private → __double_leading_underscore (e.g., __very_private).

7. Special (Dunder) Methods → __double_underscores__ (e.g., __init__()).

8. Booleans → Use is_, has_, or should_ (e.g., is_admin = True).

For more information visit:
pep8 style guide """
    
    
    
    