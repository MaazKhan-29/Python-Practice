""" Dictionary Methods """

""" Add/update method"""

dict={1:"one",2:"two",3:"three"}
dict.update({3:"THREE"})
print(dict)
dict.update({7:"Seven"})
print(dict)

""" delete method"""

data={1:"One",2:"Two",3:"Three"}
res=data.pop(1) # Compulsory input of key
print(res)
res2=data.popitem() # Don't need to input key it always remove the newest data i.e key and value both 
print(res2)

print("\n")

""" copy """

p={"bird":"crow","animal":"lion","fish":"tiuna"}
q=p
p["Dinosaur"]="Rinosaur"
print(p)
print(q)

print("\n")

p={"bird":"crow","animal":"lion","fish":"tiuna"}
q=p.copy()
p["Dinosaur"]="Rinosaur"
print(p)
print(q)

print("\n")

"""clear"""

p.clear()
print(p)

print("\n")

""" formation of dictionary with only keys"""

k=(5,8,9)
result=dict.fromkeys(k,"Number")
print(result)

print("\n")

""" set default"""

sedef={1:"one",2:"two",3:"three"}
get=sedef.setdefault(4,"Four")
print(get)
get=sedef.setdefault(3,"THREE")
print(get)




