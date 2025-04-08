"""
########Electricity Bill Generator###########

Give Customer name ,id and units as inputs

First 100 Units : Rs 5/unit
Next 100 Units : Rs 7/unit
Next all : Rs 9/unit.           """

class ElectricityBill:
    
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
        
    def calculate(self):
        bill=0
        
        if self.units>100:
            bill=bill+(5*100) 
        else:
            bill=bill+(self.units*5) 
            
        if self.units>200:
            bill=bill+(7*100)  
        elif self.units<=200 and self.units>=100:
            bill=bill+((self.units-100)*7)
            
        if self.units>200:
            bill=bill+(9*(self.units-200))    
            
    def display(self):
        bill=0
        print("\n***Welcome to Bill Generator***")
        
        if self.units>100:
            bill=bill+(5*100) 
            print("First 100 units bill: ",bill)
        else:
            bill=bill+(self.units*5) 
            print("First 100 units bill: ",bill)
            
        if self.units>200:
            temp=(7*100) 
            bill=bill+temp
            print("Next 100 units bill: ",temp)
        elif self.units<=200 and self.units>100:
            temp=((self.units-100)*7)
            bill=bill+temp
            print("Next 100 units bill: ",temp)
            
        if self.units>200:
            temp=(9*(self.units-200))  
            bill=bill+temp
            print("Next 200+ units bill: ",temp)
 
        print("Final Bill: ",bill)   
                    
result=ElectricityBill(456,"Komal",150)
result.display()

result2=ElectricityBill(780,"Kamal",250)
result2.display()






