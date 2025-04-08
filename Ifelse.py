# if else

age = int(input("Enter your age: "))

if age >= 18:
    print("You can apply for a driving license.")
    print("Congratulations")

    a = input("Enter R for renew license and N for new license: ")

    if a == "R":
        print("You selected renew license.")
    elif a == "N":
        print("You selected new license.")
    else:
        print("Invalid selection.")
elif age <= 14:
    print("You are strictly prohibited to drive.")
    print("Keep patience until you turn 18.")
elif 14 < age < 18:
    print("You are eligible for driving an electric vehicle.")
else:
    print("You cannot apply for a driving license.")
    