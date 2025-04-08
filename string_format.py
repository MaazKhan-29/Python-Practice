# String Formatting

name="Pratap Singh"
age=35
id=12
price=67.98361

print("My name is:",name,"Age is:",age,"and I'd is:",id)

print("My name is:"+name+" "+"Age is:"+str(age)+" "+"and I'd is:"+str(id))

# it looks complex hence string  format is used to simplify 

print(f"My name is:{name} Age is:{age} and I'd is:{id}")

print(f"My name is:{name} Age is:{age} I'd is:{id} &the price is {price}")

print(f"My name is:{name} Age is:{age} I'd is:{id} &the price is {price*2}") # we can do calculation inside

print(f"My name is:{name} Age is:{age} I'd is:{id} &the price is {price:10.3f}") # 10 indictes spaces and 3f is the numbers after point

# Another method for formatting 

print("My name is:{} Age is:{} I'd is:{} &the price is {}".format(name,age,id,price))

print("My name is:{3} Age is:{1} I'd is:{0} &the price is {2}".format(id,age,price,name)) # indexing in format

print("My name is:{n} Age is:{a} I'd is:{i} &the price is {p}".format(n=name,a=age,i=id,p=price))