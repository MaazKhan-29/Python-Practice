# String Methods

name="leonardo da vinci"
str="Samsung galaxy \t ultra"
dig="235"
sp=" "

print(name.capitalize()) # Makes first letter capital others small

print(name.center(40,'@')) # 40 is total space

print(name.count('d')) 
print(name.count('da')) 
print(name.count('d',0,7)) # range includes 

print(name.title()) #capitalize first letter of every word

print(str) #normal 4spaces
print(str.expandtabs(32))

print(name.find('vinci'))
print(name.index('vinci')) # same as find

print(name.find('alpha'))
# print(name.index('alpha')) shows error

print(name.lower())
print(name.upper())

space="w      abc xyz       HELLO      v"

print(space.strip()) #removes spaces from both right and left
print(space.lstrip()) #removes left space/shift to left 
print(space.lstrip('w'))
print(space.rstrip()) #removes right spaces/shift to right
print(space.rstrip('v'))

print(name.replace('leonardo','ronaldo'))
print(name.replace('i','w'))

print(name.split())
print(name.split('v'))

print(space.swapcase())

print(name.startswith('l'))
print(name.startswith('m'))
print(name.endswith('i'))
print(name.endswith('o'))

print(name.isdigit())
print(name.isnumeric()) # same as isdigit
print(dig.isdigit())
print(dig.isnumeric())

print(name.isspace())
print(sp.isspace())

# different syntax

a= "HELLO"

print(('w').join(a))



