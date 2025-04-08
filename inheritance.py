""" Oops 2nd part """

""" INHERITANCE """

"""
Inheritance is a way to create a new class that inherits the methods and properties of existing class.

Syntax:

class parent:
    pass

class child (parent):
    pass
"""

class Car:
    Brand="Jaguar"
    
    def car_detail(self):
        print("I am the normal car")
    
class electric_car(Car):
    
    def electric_car_detail(self):
        print("The Brand of the car is: ",self.Brand)
 
    def __init__(self,model):
        self.model=model
        print("Model Entered")
 
e_car=electric_car("Model 10\n")
print("The model of car is: ",e_car.model)
 
print(e_car.Brand)
e_car.car_detail()
e_car.electric_car_detail()    

e_car.Brand="BMW"    
print(e_car.Brand)
e_car.car_detail()
e_car.electric_car_detail()        

print("\n")

""" Calling constructor of parent class """

""" Syntax:
           parent_class_name.__init__(self,p parameters) """

class Bike:
    
    def __init__(self,brand):
        self.brand=brand 
    
class electric_bike(Bike):
    
    def __init__(self,brand,model):
        self.model=model   
        Bike.__init__(self,brand)     # Calling 
        
    def display(self):
        print("The Brand of bike is: ",self.brand)   
        print("The model of bike is: ",self.model)
        
e_bike=electric_bike("Yamaha","Model 8")  
e_bike.display()

""" Above all the examples of single inheritance """

"""Types of Inheritance:
   1)Single 
   2)Multi-level 
   3)Mutiple
   4)Hierarchical 
   5)Hybrid.       """
        
""" Multi-level INHERITANCE """

class Cycle:
    
    def __init__(self,brand):
        self.brand=brand 
    
class electric_cycle(Cycle):
    
    def __init__(self,brand,model):
        self.model=model   
        Cycle.__init__(self,brand)     # Calling 
        
class advance_cycle(electric_cycle):
    
    def __init__(self,brand,model,cost):
        self.cost=cost
        electric_cycle.__init__(self,brand,model)  
        
    def displays(self):
        print("\nThe Brand of the cycle is: ",self.brand)   
        print("The Model of the cycle is: ",self.model)
        print("The Cost of the cycle is: ",self.cost)
        
        
e_cycle=advance_cycle("E-Sports","Model 6",6000)
e_cycle.displays() 

e_cycle=advance_cycle("X-Stream","Model 15",9000)
e_cycle.displays()    

""" Multiple INHERITANCE """

class Cycle:
    
    def __init__(self,brand):
        self.brand=brand 
    
class electric_cycle():
    
    def __init__(self,model):
        self.model=model   
        
class advance_cycle(Cycle,electric_cycle):
    
    def __init__(self,brand,model,cost):
        self.cost=cost
        Cycle.__init__(self,brand)
        electric_cycle.__init__(self,model)  
        
    def displays(self):
        print("\nThe Brand of the cycle is: ",self.brand)   
        print("The Model of the cycle is: ",self.model)
        print("The Cost of the cycle is: ",self.cost)
        
        
e_cycle=advance_cycle("Masai","Model 3",1500)
e_cycle.displays() 

e_cycle=advance_cycle("Xpro","Model 12",600)
e_cycle.displays()   

      
""" Hierarchy INHERITANCE """

class Cycle:
    
    def __init__(self,brand):
        self.brand=brand 
    
class electric_cycle(Cycle):
    
    def __init__(self,model,brand):
        self.model=model   
        super().__init__(brand)   
    
    def dis1(self):
        print("\nThe Brand of the cycle is: ",self.brand)   
        print("The Model of the cycle is: ",self.model)    
        
class advance_cycle(Cycle):
    
    def __init__(self,cost,brand):
        self.cost=cost
        super().__init__(brand)  
        
    def dis2(self):
        print("\nThe Brand of the cycle is: ",self.brand)   
        print("The Cost of the cycle is: ",self.cost)    
        
e_cycle=electric_cycle("Model 50","LR")
u_cycle=advance_cycle(8000,"LR")

e_cycle.dis1()
u_cycle.dis2()

print("\n")


""" Hybrid Inheritance """

class Car:
    brand = "Ford"

class Electric_Car(Car):
    def __init__(self, no_of_batteries):
        self.no_of_batteries = no_of_batteries

class Music_System:
    def __init__(self, speakers):  # Fixed '__init__' method
        self.speakers = speakers

class Sports_Car(Electric_Car, Music_System):
    def __init__(self, no_of_batteries, speakers, top_speed):
        Electric_Car.__init__(self, no_of_batteries)  # Corrected method call
        Music_System.__init__(self, speakers)         # Corrected method call
        self.top_speed = top_speed

mustang = Sports_Car(100, 7, 300)  # Fixed variable name

print(mustang.brand)            # Inherited from Car
print(mustang.no_of_batteries)  # From Electric_Car
print(mustang.speakers)         # From Music_System
print(mustang.top_speed)        # From Sports_Car
