import json

contacts = []


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


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
    save_contacts()

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
            print("------------------------------")
            found = True

    if not found:
        print("Contact not found.")


def delete_contact():
    if not contacts:
        print("No contacts found.")
        return

    view_contacts()

    try:
        choice = int(input("Enter contact number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(contacts):
        print("Invalid contact number.")
        return

    deleted_contact = contacts.pop(choice - 1)
    save_contacts()

    print(f"Deleted contact: {deleted_contact['name']}")


def update_contact():
    if not contacts:
        print("No contacts found.")
        return

    view_contacts()

    try:
        choice = int(input("Enter contact number to update: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(contacts):
        print("Invalid contact number.")
        return

    contact = contacts[choice - 1]

    print("\nEnter new details:")

    contact["name"] = input("Enter name: ").title()
    contact["phone"] = input("Enter phone number: ")
    contact["email"] = input("Enter email: ")

    save_contacts()

    print("Contact updated successfully.")


def show_menu():
    print("\n========== CONTACT MANAGER ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=====================================")


contacts = load_contacts()


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
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")