# Operators

print("Arithmetic operators" )

a=8
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #gives floating value
print(a//b) #floor division (gives rounding value) if it is -8 then it result -3 
print(a%b) #gives Remainder 
print(a**b) #Gives power i.e 8 raise to 3

print(sep='\n')

print("Assignment Operator")

x=y=12
print(x)
print(y)
p,q,r=2,4,5
print(p,q,r)

x=x+12 #longhand
print(x)
y+=12 #shorthand
print(y)
#y we get as 24

y-=12
print(y)
#y we get as 12

y*=3
print(y)
#y=36

y/=3
print(y)
#y=12

y//=3
print(y)
#y=4

y**=2
print(y)
#y=16

y%=2
print(y)

#Note x++ like statment is not allowed in python 

print(sep='\n')

print(" Comparison Operator")

# Always results true and false 

s=4
t=6
print(s==t) #Not same hence false
print(s!=t) #Not same hence true
print(s>t)
print(s<t)
print(s>=t)
print(s<=t)

print(sep='\n')

print("Logical Operators")

k=7
l=5
f=9
print(k>l and f>k) #both true makes result true else false
print(l<f or l>k) #one should true to get result true else false
print(not(k>l and f>k)) #negation of result 

print(sep='\n')

print("Identical Operator (is and is not )")

#checks whether two variables occupied the same memory locations 

h=10
j=20
v=10
z=v
print(id(h))
print(id(j))
print(id(v))
print(id(z))
print(h is v)
print(h is not v)

#Range for same I'd (-5 to 256)
# Gives different id in case of list even if the list has same values 

r=-7
i=-9
print(id(r))
print(id(i))

print(sep='\n')

print("Membership Operators")

#return whether true or false

name="Huran"
print("r" in name)

lst=["horse","cat","dog"]
print("cat" in lst)
print("dog" not in lst)

num=1,3,6,8
print(9 in num)

dict={"name":"Ragu""Sam","Company":"infosis"}
print("name" in dict)
print("infosis" in dict)

print(sep='\n')

print("Bitwise operators")

w=4
g=5
print(w & g) # bitwise and 
# how result 4 ? first calculate binary of 4 and 5 and 
# do and operation on bin numbers the result willbe 4

#to find binary numbers 
print(bin(4))
print(bin(5))

print(w | g) # bitwise or
print(w ^ g) # bitwise xor

print(2<<1) #bitwise left shift #010 left shift by one becomes 100 which is 4
print(2>>1) #bitwise right shift 

#bitwise not
print(~3) #shortcut formula ~x=-(x+1) put x=3
print(~10)

# Precedence and Associativity (full explanation in notes)

# parenthesis > exponential > multiply/divide/modulus > Addition and subtraction 
"""https://ibb.co/bFgmk4H"""
"""https://ibb.co/qy108QG"""