# Strings

first_name="Mary"
second_name="Kom"
print(first_name,second_name) #way 1
name=first_name+" "+second_name #way 2
print(name)
id=10
print(first_name,second_name,id) #way 1 for integer with strings
name1=first_name+" "+second_name+" "+str(id) #way 2 for integer with strings
print(name1)

print("Mary Kom "*5)
print("\nMary Kom"*2)

# String Functions 

a="King Kong"
print(len(a))
b=65
print(chr(b))
c="a"
print(ord(c))

# Indexing of strings 

# +ve indexing 

d="Bill gates" # index starts from zero i.e B is at zero

print(d[0])
print(d[4])
print(d[5])

# -ve indexing

print(d[-1]) #starts from -1,-2,-3... from right to left 
print(d[-10])

# Slicing

# syntax: variable_name[starting_point: ending_point: steps]
print("Slicing")

x="Steve jobs"

print(x[::])
print(x[1:7]) # 7 position is o but it print upto j not o
print(x[7:10])
print(x[0:25])
print(x[:90])

print(x[-10:-1]) # -1 is s but it print upto b 
print(x[-4:])

#steps (by default it is 1,normal)

print(x[0:4:2]) # print character escape by 2 
print(x[0:5:2])
print(x[4::3])
print(x[-2:-7:1])
print(x[-2:-7:-1])
print(x[::-1]) #Mostly used


