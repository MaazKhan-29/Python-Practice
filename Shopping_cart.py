""" Shopping Cart """

class Cart:
    
    def __init__(self):
        self.items={}
        
    def add_items(self,item, quantity):
        self.items[item]=quantity
        
    def remove_items(self,item):
        self.items.pop(item)  
        
    def change_quantity(self,item, quantity):
        self.items[item]=self.items[item]+quantity   
        
    def __len__(self):
        return len(self.items) 
        
    def __str__(self):
        str="Cart Contains: "    
        
        for item in self.items:
            str+=f"\n{item} : {self.items[item]}"
        return str   
            
result=Cart()
result.add_items("Aloo",2)
result.add_items("Sabji",3)
print(result)
result.remove_items("Aloo")       
print(result)
result.change_quantity("Sabji",7)
print(result)
result.change_quantity("Sabji",-1)
print(result)
print(result.__len__())
print(len(result))
        
        
                
        
        
        