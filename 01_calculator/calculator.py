
while True:
    print("Simple calculator")

    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = int(input("Enter your Choice:- "))
    if choice == 5:
        print("Thank You")
        break

    if choice >= 1 and choice <= 4:
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
        if second_number == 0:
            print("Cannot Divide By zero")
        else:
            result = first_number / second_number
            print("Result =", result)
    else:
        print("Invalid Choice!")