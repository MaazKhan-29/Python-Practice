""" Dictionary """

dict={1:"One",2:"Two",3:"Three"} #before colon in key and after colony is value 

print(dict)

print(dict[3])
print(dict.get(3))

""" print(dict[8]) Will show error """
print(dict.get(8))

print(dict.keys())
print(dict.values())
print(dict.items())

""" dictionary using Loops """

for i in dict:
    print(i)

for i in dict:
    print(dict[i])

for i in dict.values():
    print(i)
    
for i in dict.keys():
    print(i)

for i in dict.items():
    print(i)
 
for i,j in dict.items():
    print(i,"in English",j)
        
for i in dict:
    print(i,dict[i])
    
""" Mutable """

dict[2]="TWO"
print(dict)
 
""" If there is a duplicate keys then the old one will get removed & the last entered value shown"""

data={1:"One",2:"Two",1:"Three"}
print(data)

""" Dictionary is mutable hence only mutable value are inserted immutable are not allowed"""

numbers={'1':"one", '2':"two", (3.0,4):"three"} # List & set are not allowed 
print(numbers)

""" Membership operator"""

print('2' in numbers)
print(4 in numbers)
print(2 not in data)

""" nested dictionary"""

nest={"Hanif":{"age":45,"id":7},"surya":{"age":20,"id":9}}
print(nest)
print(nest["Hanif"])
print(nest["Hanif"]["id"])

""" insertion of data into dictionary"""

a={}
a["Name"]="joy"
a["age"]=8
print(a)



