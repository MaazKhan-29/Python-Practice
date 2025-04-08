""" Super and macro functions """

"""
Super function is Used to call methods from a parent class in inheritance.
It Helps in method overriding and multiple inheritance.
Ensures proper method resolution order (MRO) in Python.

Python does not support macros like C/C++, but we can use lambda functions for similar behavior.

"""

class old_calci:
    
    def area(self):
        print("Calculating Area.......")
        
class calculation(old_calci):
    
    def __init__(self,height,width):
        self.height=height 
        self.width=width 
        
    def area(self):
        print("Calculating new area....")  
        
class rectangle(calculation):
    
    def __init__(self,height,width):
        super().__init__(height,width)
        
    def area_rect(self):
        super().area()
        print("The area of rectangle is: ",self.height*self.width)  
         
class cube(calculation):
    def __init__(self,height,width,length):
        super().__init__(height,width) 
        self.length=length
    
    def area_cube(self):
        super().area()
        print("The area of cube is: ",self.height*self.width*self.length)  
    
res=rectangle(5,6)
res.area_rect()
 
result=cube(5,6,2)
result.area_cube()

print(rectangle.mro())
print(cube.mro())




class old_calci:
    
    def area(self):
        print("Calculating Area.......")
        
class calculation:
    
    def __init__(self,height,width):
        self.height=height 
        self.width=width 
        
    def area(self):
        print("Calculating new area....")  
        
class rectangle(old_calci,calculation):
    
    def __init__(self,height,width):
        super().__init__(height,width)
        
    def area_rect(self):
        super().area()
        print("The area of rectangle is: ",self.height*self.width)  
         
class cube(old_calci,calculation):
    def __init__(self,height,width,length):
        super().__init__(height,width) 
        self.length=length
    
    def area_cube(self):
        super().area()
        print("The area of cube is: ",self.height*self.width*self.length)  
    
res=rectangle(5,6)
res.area_rect()
 
result=cube(5,6,2)
result.area_cube()

print("\n")

""" Encapsulation """

"""
Python Encapsulation is a process of wrapping data and methods in a single unit.
A class itself is an example of encapsulation, as it wraps data members and methods in a single unit 

Python does not have strict access control like other languages (e.g., C++ or Java), but it follows naming conventions to indicate access levels:

Ex: name for public members 
    _name for protected members 
    __name for private members """
 
"""Public"""
class Example: 
    def __init__(self):
        self.public_var = "I am Public" # ✅ Accessible

obj = Example()
print(obj.public_var)   

"""Protected"""
class Example:
    def __init__(self):
        self._protected_var = "I am Protected"  # ✅ Accessible but should be used with caution
        
obj = Example()
print(obj._protected_var)  

"""Private"""
class Example:
    def __init__(self):
        self.__private_var = "I am Private"

obj = Example()
# print(obj.__private_var)  ❌ AttributeError
print(obj._Example__private_var)  # ✅ Accessed using name mangling

print("\n")


"""Public"""
class Employee:
    def __init__(self, name):  
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")

class HR(Employee):
    def hrdetails(self):
        print(f"Name: {self.name}")

rohit10 = HR("Rohit")

rohit10.display_info()
print(rohit10.name)
rohit10.hrdetails()
print("\n")

"""Protected"""
class Employee:
    def __init__(self, name, account_no):  
        self.name = name
        self._account_no=account_no

    def display_info(self):
        print(f"Name: {self.name},Account_no: {self._account_no}")

class HR(Employee):
    def hrdetails(self):
        print(f"Name: {self.name},Account_no: {self._account_no}")

rohit10 = HR("Rohit",67628628)

rohit10.display_info()
print(rohit10.name)
print(rohit10._account_no)
rohit10.hrdetails()
print("\n")

"""Private"""
class Employee:
    def __init__(self, name, account_no, salary):  
        self.name = name
        self._account_no=account_no
        self.__salary=salary

    def display_info(self):
        print(f"Name: {self.name},Account_no: {self._account_no}, Salary:{self._Employee__salary}")

class HR(Employee):
    def hrdetails(self):
        print(f"Name: {self.name},Account_no: {self._account_no}, Salary:{self._Employee__salary}")

rohit10 = HR("Rohit",67628628,5000)

rohit10.display_info()
print(rohit10.name)
print(rohit10._account_no)
print(rohit10._Employee__salary)
rohit10.hrdetails()

print(dir(rohit10))

""" Abstract method """

"""An abstract method in Python is a method that is declared in a base class but does not have an implementation. Instead, subclasses must provide their own implementation.
Abstract methods are defined using the @abstractmethod decorator inside an abstract class, which is a class that inherits from ABC (Abstract Base Class).

Example:                                   """

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

# dog = Animal()  # This will raise an error (can't instantiate an abstract class)
dog = Dog()
print(dog.sound())  # Output: Bark

"""
Key Points:
Abstract methods must be overridden in derived classes.
An abstract class cannot be instantiated directly.
Used to enforce a structure in object-oriented programming (OOP).

Example 2:
"""
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"

# payment = Payment()  # This will raise an error (can't instantiate an abstract class)
credit = CreditCardPayment()
print(credit.process_payment(100))  # Output: Processing credit card payment of 100

"""
Here, Payment is an abstract class that forces all payment methods (CreditCardPayment, PayPalPayment) to implement process_payment(),
ensuring a structured approach to different payment methods.

"""
