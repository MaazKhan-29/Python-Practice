""" Function"""

""" Syntax: def function_name (parameter 1, parameter 2,...) """

def simple():
    print("Hello World")
    
simple() 
print(3)  
simple() # we can call multiple times
simple()

def multiply(a,b,c):
    print(a*b*c)

multiply(2,4,6) 
multiply(7,5,9)

def add(a,b,c):
    return(a+b+c)

print("Add =",add(2,4,6))

def sub(x,y):
    print(a-b)
    
a=10
b=5
sub(a,b)    

""" Two types of functions : User defined & built in """
""" user defined is the function that human makes
while built in function are already build ex print(),len() etc"""

def calculate(a,b):
    s=a+b
    p=a-b
    z=a**b
    return s,p,z
    
x,y,v=calculate(5,2)    
print(x,y,v)

k=calculate(5,2)
print(k)

""" Types of Arguments """

"""
positional argument 
keyword argument 
default argument 
arbitrary argument 
"""

""" positional argument """

def pos(x,y,z):
    if x>y and x>z:
        print("x is greater")
        
    elif y>x and y>z:
        print("y is greater")     
   
    else:
        print("z is greater")
   
x=20
y=60
z=7
pos(x,y,z) 
""" here the position is fixed as x=20,y=60...."""
""" if we change the position the result will be wrong"""

pos(x,z,y) # ex: it shows 7 is greater 

"""Keyword argument """

""" here in keyword argument we assign the exact value to argument that pass to function def"""
a=70
b=67
c=10
pos(x=a,y=b,z=c) 
pos(y=b,z=c,x=a) # since we shuffle it the result will be correct 
   
""" default argument """

def default(x,y,z=99):
    if x>y and x>z:
        print(x)
        
    elif y>x and y>z:
        print(y)     
   
    else:
        print(z)

u=10
n=60
m=30  
default(x=u,y=n)  

""" varaible length argument"""

def collect(*args):
    print("ARGS=",args)
    print("ARGS=",*args)
    print(args[1])

a=10
b=79
c=45
collect(a,b,c,77,46,90,34)  

def list(**kwags):
    print("Kwags=",kwags)
    #print("Kwags=",**kwags) (error)
    print(kwags["z"])  

a=10
b=79
c=45
list(x=a,y=b,z=c)  

print("\n") 

""" Global and local variables"""

name="Kaif" # it is global varaible 

def data():
    name="marco" # it is a local variable
    return name

def info():
    print(name)
    
print(data())
print(name)
info()    
  
print("\n")    

name="Firoz"    

def data():
    global name
    name="Sudesh"
    return name

def info():
    print(name)
    
print(data())
print(name)
info()    

    