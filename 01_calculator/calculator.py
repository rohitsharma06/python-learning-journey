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

history = []

def show_menu():
    print("Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("6.History")

while True:

    show_menu()
    choice = get_number("Enter your Choice:- ")

    if choice == 5:
        print("Thank You")
        break

    if choice == 1:
        first_number = get_number("Enter your First Number:- ")
        second_number = get_number("Enter your Second Number:- ")
        result = add(first_number, second_number)
        print("Result =", result)

        history.append(f"{first_number} + {second_number} = {result}")

    elif choice == 2:
        first_number = get_number("Enter your First Number:- ")
        second_number = get_number("Enter your Second Number:- ")
        result = subtract(first_number,  second_number)
        print("Result =", result)

    elif choice == 3:
        first_number = get_number("Enter your First Number:- ")
        second_number = get_number("Enter your Second Number:- ")
        result = multiply(first_number, second_number)
        print("Result =", result)

    elif choice == 4:
        first_number = get_number("Enter your First Number:- ")
        second_number = get_number("Enter your Second Number:- ")
        if second_number == 0:
            print("Cannot Divide By Zero")
        else:
            result = divide(first_number, second_number)
            print("Result =", result)
    elif choice == 6:
        if len(history) == 0:
            print("No History Available")
        else:
            print("------ History ------")
            for item in history:
                print(item)

            print("---------------------")


    else:
        print("Invalid Choice!")
