""" User defined Exception handling """

class Ageless(Exception):
    pass
    
class Agemore(Exception):
    
    def __init__(self,age):
        self.age=age
        
    def display(self):
        print("Your age is : ",self.age)   

age=int(input("Enter age: "))   

try:
    if age<3:
        raise Ageless
    elif age>60:
        raise Agemore(age)
         
except Ageless:
    print("Not eligible,age is less")
           
except Agemore as e:
    print("Not eligible,age is more")
    e.display()
               

""" Suppose we have code in one of the file named as calculator.py
i.e
def add(self):
    print("Add")
def substract(self):
    print("subtract")  

add()
substract()
//code end//

if we create another file named as calci and there we import above code file name as calculator 

there automatically Add and subtract gets printed without calling them

if we code print(__name__) in calculator.py file 
output:__main__

and output on calci.py will be output: Calculator 


Since in file of calculator.py automatically Add and subtract gets printed without calling them
to solve this issue 

we write below code:
def add(self):
    print("Add")
def substract(self):
    print("subtract")  

if __name__=='__main__':
    add()
    substract()
//code end//

Now the calci.py have no output!like before """

""" if we write such code in calculator.py

def welcome(self):
    print("Welcome")
    
if __name__=='__calculator__':
    welcome()    

The output for calci.py will be 
output:welcome

"""