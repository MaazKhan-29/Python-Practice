""" OPPS """

""" There are three types way of programming """
""" 1) Procedural programming 
    2) Functional programming 
    3) OOPS(Object Oriented programming)
    
    PYTHON follows all the way....."""
    
""" Under oops we have 
    1) Class ( Blueprint/Structure )
    2) Object ( A parts of blueprint )
    3) Methods ( i.e Function )
    4) Inheritance 
    5) Polymorphism 
    6) Abstraction
    7) Encapsulation     """
 
 
    
""" Class & Objects"""

""" A class is basically a blueprint or structure 
Ex: If we want to create passport (First name,last name,father name & address) are the 
    basic information which is compulsory hence it is the main blueprint and the different 
    persons that makes a enrollment of passport are the objects """

""" creation of class & Objects

  Syntax: class class_name:
            class body
            
  Syntax: object_name=class_name(parameters)  """
  
class Employee:
    
    print("Here is the company")
    company="Apple"
    
    def Method(self): # This is called Methods & self keyword is used compulsory in order to assign different employees details 
        print("My company name is: ",self.company)
        
    def info(self,name,age):
        self.name=name   #this self.name is called Instance varaible 
        self.age=age
        print("Name of the Employee is: ",self.name)   
        print("Age of the Employee is: ",self.age)
    
    def data(self):
        print("Name of the Employee is: ",self.name)   
        print("Age of the Employee is: ",self.age)
        
Danish07=Employee()  #Danish07 is object of class Employee 
print(Danish07.company) #Accessing company name
Danish07.Method()   
Danish07.info("Danish",20)
print(Danish07.name)
   
Sandeep09=Employee()  #Sandeep09 is also object of class Employee 
print(Sandeep09.company) 
Sandeep09.info("Sandeep",40)
Sandeep09.data()
print(Sandeep09.age)

print("\n")




""" Constructors """

""" A constructor is basically used to construct an object and
 assign a value to the object's members

Two types: 1) Default constructor 
           2) Parameterized constructor """
           
class Employees:
    organization="ONGC"
    
    def member(self):
        print("Hello")
        
    def __init__(self):
        print("Default Constructor is used")   

class Emp2:    
    def __init__(self,name,age):
        self.name=name
        self.age=age   
        

Mohit67=Employees()   #Here u can see without calling a method the sentence gets printed this is default constructor 
Mohit67.member()   

Akram19=Emp2("Akram",34)  #Here it is a Parameterized constructor since we pass our parameters 
print(Akram19.age)

print("\n")




""" Example 2 """

class Animal:
    drink="Water"
    
    def common(self):
        print("The common drink is: ",self.drink)
    
    def __init__(self,name,area,food):
        self.name=name # instance varaibles
        self.area=area
        self.food=food
    
    def display(self):
        print("My name is: ",self.name)
        print("My area is: ",self.area)
        print("My food is: ",self.food)
        print("Common drinking is: ", Animal.drink)
        
dog=Animal("Dog","Street","meat")  
cat=Animal("Cat","Street","fish")  

print("Name:",dog.name,"\t","Area:",dog.area,"\t","Food:",dog.food)      
print("Name:",cat.name,"\t","Area:",cat.area,"\t","Food:",cat.food)              

dog.display()
cat.display()

print(dog.drink)
print(Animal.drink)
cat.common()

print(id(dog.drink)) #it is a global/class variable hence common to all objects hence id will be same
print(id(cat.drink))

print(id(dog.area)) #area is same hence id will be same
print(id(cat.area))

print(id(dog.food))
print(id(cat.food))

""" we can also update later"""
cat.area="Home"
print(cat.area)
cat.display()

""" we can update a class variable with specific object"""
cat.drink="Milk"
print(dog.drink)
print(cat.drink)

""" we can update a class variable using class name"""
Animal.drink="Beer"  
dog.display() 
print(cat.drink)

print("\n")



""" Static and class methods """

"""
We use staticmethod for calculation which is common to all employees or workers etc.
A static method is a method that belongs to a class but doesn't access or modify 
the class or instance state. A class method takes a reference to the class itself (cls) and can modify
"""
class Bank:
    name="Indian Bank"
    count=0
    
    @staticmethod  #decorators , didn't access any class and instance varaibles 
    def interest(p,r,t):   #self is not used
        result=((p*r*t)/100)
        return result 
        
    @classmethod  # Only access the class variable and can modify 
    def bank_name(cls):
        print(cls.name)
        cls.name="BOI"
        print(cls.name)
     
    @classmethod
    def counting(cls):
        cls.count+=1
        
    @classmethod
    def print_count(cls):
        print("Total Employees calculation is: ",cls.count)
          
    def __init__(self,name,address):
        self.name=name
        self.address=address 
        Bank.counting()
        
Pandey23=Bank("Pandey","60 feet road")  
print(Pandey23.name)   

store=Pandey23.interest(1000,10,3)  #here we calculating pandey bank interest 
print(store)

store1=Bank.interest(2000,60,2)  #We can directly calculate by class name
print(store1)

sanchit56=Bank("Sanchit","Panvel")
sanchit56.bank_name()
Bank.bank_name()  #We can access class Method via class name & Now bank name changes to boi hence two times it get printed 

print(Bank.print_count())


