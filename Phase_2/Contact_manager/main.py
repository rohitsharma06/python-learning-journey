contacts = []


def add_contact():
    name = input("Enter name: ").title()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n========== CONTACTS ==========")

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("------------------------------")


def search_contact():
    name = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("Contact not found.")


def show_menu():
    print("\n========== CONTACT MANAGER ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    print("=====================================")


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        add_contact()

    elif choice == 2:
        view_contacts()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")