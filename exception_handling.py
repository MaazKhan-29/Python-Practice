""" Exception handling """

""" if error occurs in try it print except block or 
 if the try block runs without error then else part also get printed 
 then comes finally block which always runs no cares about try and except """
 
"""Normally we use Exception instead of ZeroDivisionError,TypeError in order to answer for all errors """

try:
     num1=int(input("Enter the first number: "))
     num2=int(input("Enter the second number: "))
     divide=num1/num2
     print(divide)
     
except Exception as e: # 
     print("Division operation didn't run successfully due to some reason\n","Error reason: ",e)   
 
except ZeroDivisionError as e: # 
     print("Division operation didn't run successfully\n","Error reason: ",e)    

except TypeError as e: # 
     print("Division operation didn't run successfully\n","Error reason: ",e)   
          
else:
     print("Division operation completed")
      
finally:
     print("Always printed")




try:
     num1=(input("Enter the first number: "))
     num2=int(input("Enter the second number: "))
     divide=num1/num2
     print(divide)
     
except TypeError as e: # 
     print("Division operation didn't run successfully\n","Error reason: ",e)   
     
else:
     print("Division operation completed")
      
finally:
     print("Always printed")       
     

     
     
           