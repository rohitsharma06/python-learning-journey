def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

symbols = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}

valid_operations = [1, 2, 3, 4]


def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid Input! Please enter a number.")


def get_two_numbers():
    first_number = get_number("Enter your First Number:- ")
    second_number = get_number("Enter your Second Number:- ")
    return first_number, second_number


def show_result(result):
    print("====================")
    print("Result =", result)
    print("====================")


def show_menu():
    print("\n===== Simple Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("6. History")


while True:

    show_menu()
    choice = get_number("Enter your Choice:- ")

    if choice == 5:
        print("Thank You!")
        break

    elif choice in valid_operations:

        first_number, second_number = get_two_numbers()

        if choice == 4 and second_number == 0:
            print("Cannot Divide By Zero")
            continue

        result = operations[choice](first_number, second_number)
        show_result(result)

        file = open("history.txt", "a")
        file.write(f"{first_number} {symbols[choice]} {second_number} = {result}\n")
        file.close()

    elif choice == 6:

        try:
            file = open("history.txt", "r")
            data = file.read()

            if not data:
                print("No History Available")
            else:
                print("------ History ------")
                print(data, end="")
                print("\n---------------------")

            file.close()

        except FileNotFoundError:
            print("No History Available")

    else:
        print("Invalid Choice!")