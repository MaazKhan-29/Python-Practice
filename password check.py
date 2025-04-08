# Password technique 

original_pass="abcd"

for i in range(1,6):
    password=input("Enter password: ")
    if password!=original_pass:
        print("Invalid pass")
        print(5-i,"Attemps left")
    else:
        print("password correct")
        break    
    
    
    
    
    
    