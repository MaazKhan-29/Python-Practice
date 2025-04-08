menu={
     "Dosa":20,
     "Idli":10,
     "Wada":15,
     "Tea":10,
     "icecream":30
}

print("\tWELCOME TO BTECH RESTAURANT\n")

print("Menu Card\n")

for key in menu:
    print(key.ljust(10),"-",menu[key])
    
bill=0
   
while True:
    
    order=input("\nEnter order item or say Done: ") 
    
    if order=="Done":
        break

    elif order in menu:
        quantity=int(input("Enter the quantity "))
        bill=bill+(menu[order]*quantity)
        
    else:
        print("Enter the item which is in menu")    

print("\n")
print("Bill: ",bill)  
print("Bill with gst: ",bill+(18/100*bill))      
        
    
    
    
    
    

    