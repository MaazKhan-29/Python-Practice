# BMI Calculator (Body Mass Index)

Weight=float(input("Enter your weight in kg: "))
Height=float(input("Enter your height in m: "))

bmi=Weight/(Height**2)

print("BMI:",bmi)

print(sep='\n')

# Tip Calculator 

bill=float(input("Enter the amount of bill: "))
persons=int(input("How many persons are there: "))
tip=float(input("Amount of tip in percent: "))

total_bill=bill+((tip/100)*bill)
amount_per_person=total_bill/persons

print("The total amount of bill will be: ",total_bill)
print("Amount per person: ",amount_per_person)

