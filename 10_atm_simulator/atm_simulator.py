balance = 1000.0

current_pin = 1234

transactions = []


def show_menu():
    print("========== ATM SIMULATOR ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transactions")
    print("5. Exit")
    print("===================================")


def verify_pin():
    attempts = 3

    while attempts > 0:
        try:
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if pin == current_pin:
            print("PIN verified successfully.")
            return True

        attempts -= 1

        if attempts > 0:
            print(f"Incorrect PIN. Attempts Remaining: {attempts}")
        else:
            print("Too many incorrect attempts.")

    return False


def view_transactions():
    if len(transactions) == 0:
        print("No transactions available.")
        return

    print("\n---------- Transaction History ----------")

    for i in range(len(transactions)):
        print(f"{i + 1}. {transactions[i]}")

    print("------------------------------------------")


def save_data():
    file = open("atm_data.txt", "w")

    file.write(f"{balance}\n")

    for transaction in transactions:
        file.write(f"{transaction}\n")

    file.close()


def load_data():
    global balance

    try:
        file = open("atm_data.txt", "r")

        lines = file.readlines()

        if len(lines) > 0:
            balance = float(lines[0].strip())

            for line in lines[1:]:
                transactions.append(line.strip())

        file.close()

    except FileNotFoundError:
        pass


load_data()


if not verify_pin():
    print("Access Denied.")
    exit()


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid option.")
        continue

    if choice == 1:
        print(f"Current Balance = ₹{balance:.2f}")

    elif choice == 2:

        try:
            amount = int(input("Enter Deposit Amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        if amount > 50000:
            print("Maximum deposit limit is ₹50000.")
            continue

        balance += amount

        transactions.append(f"Deposit: ₹{amount:.2f}")

        save_data()

        print(f"₹{amount:.2f} added successfully.")
        print(f"Current balance is: ₹{balance:.2f}")

    elif choice == 3:

        try:
            amount = int(input("Enter withdrawal amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        if amount > 10000:
            print("Maximum withdrawal limit is ₹10000.")
            continue

        if amount > balance:
            print("Insufficient balance.")
            continue

        balance -= amount

        transactions.append(f"Withdrawal: ₹{amount:.2f}")

        save_data()

        print(f"₹{amount:.2f} withdrawal successful.")
        print(f"Current balance is: ₹{balance:.2f}")

    elif choice == 4:
        view_transactions()

    elif choice == 5:
        save_data()
        print("Thank you for using ATM.")
        break

    else:
        print("Please choose a valid option.")