""" Recursion"""

""" Repeated function by itself """

""" Ex: counting number backward upto 0 """

def count(n):
    if n==0:
        return
    print(n)    
    count(n-1)
    
count(5)

""" Factorial """

def fact(n):
    if n==0:
        return 1
    return (n*fact(n-1)) 
       
print(fact(5))

""" Lamba function """

def normal():
    print("Hello")
    
normal()

a=lambda : print("Hello")
a()

""" Ex 1: """

def store(x):
    return (x**2)
    
a=store
print(a(5))   

"""using lambda function"""
y=lambda z : z**2
print(y(5))

""" Ex 2: """

def add(x,y):
    return x+y
    
def calculate(calc,a,b):
    print(calc(a,b))
    
calculate(add,4,5)       

""" uning lambda function """

def calculate(calc,a,b):
    print(calc(a,b))
    
calculate(lambda x,y : x+y,5,5)

""" Ex 3 """

x=6
x="Even" if x%2==0 else "Odd"
print(x)

""" using lambda"""

x=lambda x : "Even" if x%2==0 else "Odd"
print(x(8))
print(x(11))
