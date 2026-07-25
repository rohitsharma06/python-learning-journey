print("Simple calculator")

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter your Choice:- "))

first_number = int(input("Enter your First Number:- "))
second_number = int(input("Enter your Second Number:- "))

if choice == 1:
    result = first_number + second_number
    print("Result =", result)
elif choice == 2:
    result = first_number - second_number
    print("Result =", result)
elif choice == 3:
    result = first_number * second_number
    print("Result =", result)
elif choice == 4:
    result = first_number / second_number
    print("Result =", result)
else:
    print("Invalid Choice!")