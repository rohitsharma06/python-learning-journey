def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number

        except ValueError:
            print("Invalid Input! Please enter a number.")


def show_menu():
    print("Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

while True:

    show_menu()
    choice = get_number("Enter your Choice:- ")

    if choice == 5:
        print("Thank You")
        break

    if choice >= 1 and choice <= 4:
        first_number = get_number("Enter your First Number:- ")
        second_number = get_number("Enter your Second Number:- ")

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
