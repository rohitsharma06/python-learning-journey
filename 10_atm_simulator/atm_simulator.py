balance = 1000.0

current_pin = 1234

def show_menu():
    print("========== ATM SIMULATOR ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
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
            return  True

        attempts -= 1

        if attempts > 0:
            print(f"Incorrect PIN. Attempts Remaining: {attempts}")
        else:
            print("Too many incorrect attempts.")

    return False



if not  verify_pin():
    print("Access Denied")
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
            print("Please enter a valid amount")
            continue

        if amount <= 0:
            print("Amount must be greater than 0")
            continue

        if amount > 50000:
            print("Maximum deposit limit is ₹50000.")
            continue

        balance += amount

        print(f"₹{amount:.2f} added successfully")
        print(f"Current balance is : ₹{balance:.2f}")
    elif choice == 3:
        try:
            amount = int(input("Enter withdrawal amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0")
            continue

        if amount > 10000:
            print("Maximum withdrawal limit is ₹10000.")
            continue

        if amount > balance:
            print("Insufficient balance.")
            continue

        balance -= amount

        print(f"₹{amount:.2f}  withdrawal successfully")
        print(f"Current balance is : ₹{balance:.2f}")

    elif choice == 4:
        print("Thank you For using ATM")
        break
    else:
        print("Please choose Valid option")

