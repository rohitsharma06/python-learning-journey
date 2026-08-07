contacts = []

while True:

    print("========== CONTACT BOOK ==========")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("==================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    if choice < 1 or choice > 5:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 1:

        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for contact in contacts:
                print("----------------------------")
                print(f"Name  : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")
                print("----------------------------")

    elif choice == 2:

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        print("Contact added successfully.")

    elif choice == 3:

        search_name = input("Enter contact name to search: ")
        found = False

        for contact in contacts:

            if contact["name"] == search_name:
                print("\n---------- Contact Found ----------")
                print(f"Name  : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")
                print("-----------------------------------")
                found = True

        if found == False:
            print("Contact not found.")

    elif choice == 4:

        delete_name = input("Enter contact name to delete: ")
        found = False

        for contact in contacts:

            if contact["name"] == delete_name:
                contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break

        if found == False:
            print("Contact not found.")

    elif choice == 5:

        print("Thank you for using Contact Book!")
        break