""" Dunder methods """

"""
Dunder (double underscore) methods, also called magic methods, are special methods in Python that start
 and end with double underscores (__). They allow customization of object behavior, such as initialization,
  string representation, and operator overloading."""

"""Example: __init__ and __str__ """

class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def __str__(self):  # String representation
        return f"{self.name} is {self.age} years old."

p = Person("Rohan", 20)
print(p)  # Calls __str__() -> Output: Asif is 20 years old.

"""Example: Operator Overloading (__add__) """

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # Overloads `+` operator
        return Number(self.value + other.value)

num1 = Number(5)
num2 = Number(10)
result = num1 + num2  # Calls __add__()
print(result.value)  # Output: 15

"""The __repr__ method returns a developer-friendly string representation of an object, often used for debugging."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  # Used for debugging
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Aakif", 20)
print(repr(p))  # Output: Person(name='Asif', age=20)


"""The __call__ method allows an instance of a class to be called like a function."""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):  # Allows instance to be used as a function
        return value * self.factor

double = Multiplier(2)
print(double(5))  # Calls __call__(), Output: 10

""" For more information search 
python dunder methods"""

""" Property decorator """

"""The @property decorator in Python is used to define getter methods that allow accessing class attributes like properties without calling them as methods
. It helps implement encapsulation by controlling attribute access.

Example: Using @property"""

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private variable

    @property
    def radius(self):  # Getter method
        return self._radius

    @radius.setter
    def radius(self, value):  # Setter method
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value

    @radius.deleter
    def radius(self):  # Deleter method
        del self._radius

c = Circle(5)
print(c.radius)  # Calls the getter -> Output: 5

c.radius = 10  # Calls the setter
print(c.radius)  # Output: 10

del c.radius  # Calls the deleter

