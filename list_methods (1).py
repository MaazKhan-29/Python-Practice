""" List Methods """

num=[6,9,3,8,4]
n=[2,0,1]
str=["Boy","girl","none"]
str1=["cat","dog","horse"]
str2=["goat","donkey","hor"]

print(num)
print(n)

print("\nAppend")
num.append(7)
print(num)

print("\nadding at last")
final=num+n
print(final)

num.extend(n)
print(num)

print("\ninsert between")
num.insert(0,500) #value.insert(index_position,value)
print(num)

print("\nRemove")
num.remove(9)
print(num)

str.remove("girl")
print(str)

str1.pop()
print(str1)
str1.pop(0)
print(str1)

print("\nClear")
str2.clear()
print(str2)

print("\n")

alpha=["b","c","a"]

print("sort")
alpha.sort()
print(alpha)

print("sort in descending order")
alpha.sort(reverse=True)
print(alpha)

""" difference between function and methods 
In function if we modify the list the original one will not change 
but in method original one changes"""

print("\nsort using function")

func=["b","c","a"]
x=sorted(func)
print(x)
print(func)

print("\n")

birds=["sparrow","crow","piegion","owl"]
p=birds
p[0]="Hen"
print(p)
print(birds)

"""Here birds assign one memory location and p also assigned same memory locations 
hence changes in one effect in. the original one"""
""" To solve this copy is used"""

print("\nCopy")

birds=["sparrow","crow","piegion","owl"]
p=birds.copy()
p[0]="Hen"
print(p)
print(birds)

print("\nCount and index")

numbers=[8,6,6,3,2,0]
print(numbers.count(6))
print(numbers.index(2))
print(numbers.index(6))