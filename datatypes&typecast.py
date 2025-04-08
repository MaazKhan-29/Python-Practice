#Data types
#type function is used to check the data type

name="Sam"
print(type(name))

a=50
print(type(a))

b=3.56
print(type(b))

#No size limit for int and float in python 
#int and float can be positive or negative 

comp=5+7j
print(type(comp))

com=complex(3,6)
print(com)
print(type(com))

z=True #or False
print(type(z))
#bool are case sensitive i.e true/false is not allowed 

u=None
print(type(u))

lst=[32,4.5,"don",True,4+7j]
print(lst)
print(type(lst))
#list of different data

tup=(32,4.5,"don",True,4+7j)
print(tup)
print(type(tup))
#same as list only difference is we cannot further change the  data 

set={1,1,2,2,3,3,4,4,}
print(set)
print(type(set))

dic={"name":"Gui","age":42,"marks":34}
print(dic)
print(type(dic))

#python is dynamically typed language 
#we can change the value during runtime
a=30
b=45
a="abc"
print(a)

#Type Casting

k=57
l="7"
print(type(k))
print(type(l))
print(k+int(l))

f=input("Enter first number:")
o=input("Enter second number:")
print(f+o)
#instead of adding it's get concatenate

#type casting....(Explicit typecasting)
f=input("Enter first number:")
o=input("Enter second number:")
print(int(f)+int(o))

naam="gunjan"
nalen=len(naam)
print(type(nalen))
print("The length of the girl name has ",str(nalen),"characters")

#implicit typecasting (computer automatically decides the data types)
#lower to higher data conversion 
i=10#int lower
p=3.5#float higher
sum=(i+p)
print(sum) # output float (higher)


