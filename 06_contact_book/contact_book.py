contacts = []

while True:
    print("========== CONTACT BOOK ==========")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("==================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if len(contacts) == 0:
            print("No contacts Available")
        else:
            for contact in contacts:
                print("----------------------------")
                print(f"Name  : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")

    if choice == 2:

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)

        print("Contact added successfully.")

