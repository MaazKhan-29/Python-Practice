""" Bill Generator """

""" WAP to enter number of products then enter product name 
quantity, price and create a list of tuple 
At last display the bill and total bill"""

print("Welcome to code store")

num=int(input("Enter the number of products " ))
list=[]

for i in range(num):
    name=input("Enter the name of products: ")
    quantity=float(input("Enter the quantity: "))
    price=float(input("Enter the price: "))
    list.append((name,quantity,price))

print("\n")
print("Items\tQty\tPrice\tTotal price")

for i in list:
    total=i[1]*i[2] 
    print(f"{i[0][0:5]}\t{i[1]:3.2f}\t{i[2]:3.2f}\t{total:3.2f}") 

print("\n") 
   
print("Final_bill=",total)      