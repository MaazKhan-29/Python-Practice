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
bill_detail={}
   
while True:
    
    order=input("\nEnter order item or say Done: ") 
    
    if order=="Done":
        break

    elif order in menu:
        quantity=int(input("Enter the quantity "))
        bill_detail[order]=quantity 
        
    else:
        print("Enter the item which is in menu")    

for item in bill_detail:
    bill_cost=menu[item]*bill_detail[item]
    bill=bill+bill_cost
    print(f"{item.ljust(10)}\t{bill_detail[item]}\t{bill_cost}")

print("\n")    
print("Your Bill = ", bill)
print("Bill with GST =", bill + ((18/100)*bill))    

    
    
    
    
    

    