def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def show_menu():
    print("Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")


while True:
    show_menu()

    choice = int(input("Enter your Choice:- "))

    if choice == 5:
        print("Thank You")
        break

    if choice >= 1 and choice <= 4:
        first_number = int(input("Enter your First Number:- "))
        second_number = int(input("Enter your Second Number:- "))

    if choice == 1:
        result = add(first_number, second_number)
        print("Result =", result)

    elif choice == 2:
        result = subtract(first_number,  second_number)
        print("Result =", result)

    elif choice == 3:
        result = multiply(first_number, second_number)
        print("Result =", result)

    elif choice == 4:
        if second_number == 0:
            print("Cannot Divide By Zero")
        else:
            result = divide(first_number, second_number)
            print("Result =", result)

    else:
        print("Invalid Choice!")
