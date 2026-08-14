students = []


def show_menu():
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. View Students")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Exit")
    print("===============================================")


def view_students(students):
    if len(students) == 0:
        print("No students available.")
        return

    print("\n---------- Students ----------")

    for i in range(len(students)):
        print("----------------------------")
        print(f"Student : {i + 1}")
        print(f"Name    : {students[i]['name']}")
        print(f"Age     : {students[i]['age']}")
        print(f"Course  : {students[i]['course']}")

    print("----------------------------")


def add_student(students):
    name = input("Enter Student Name: ").strip().title()

    if name == "":
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    if age <= 0:
        print("Age must be greater than 0.")
        return

    course = input("Enter Student Course: ").strip().title()

    if course == "":
        print("Course cannot be empty.")
        return

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully.")


def delete_student(students):
    if len(students) == 0:
        print("No students available to delete.")
        return

    try:
        student_number = int(input("Enter Student Number To Delete: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    if student_number >= 1 and student_number <= len(students):
        removed_student = students.pop(student_number - 1)

        print(f"{removed_student['name']} deleted successfully.")
    else:
        print("Invalid Student Number.")


def search_student(students):
    if len(students) == 0:
        print("No students available to search.")
        return

    search_name = input("Enter Student Name: ").strip().lower()

    found = False

    for student in students:
        if student["name"].lower() == search_name:
            print("\n---------- Student Found ----------")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print("-----------------------------------")

            found = True
            break

    if found == False:
        print("Student not found.")


def update_student(students):
    if len(students) == 0:
        print("No students available to update.")
        return

    search_name = input("Enter Student Name: ").strip().lower()

    found = False

    for student in students:
        if student["name"].lower() == search_name:
            print("\n---------- Student Found ----------")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print("-----------------------------------")

            try:
                new_age = int(input("Enter New Age: "))
            except ValueError:
                print("Please enter numbers only.")
                return

            if new_age <= 0:
                print("Age must be greater than 0.")
                return

            new_course = input("Enter New Course: ").strip().title()

            if new_course == "":
                print("Course cannot be empty.")
                return

            student["age"] = new_age
            student["course"] = new_course

            print("Student updated successfully.")

            found = True
            break

    if found == False:
        print("Student not found.")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        delete_student(students)

    elif choice == "4":
        search_student(students)

    elif choice == "5":
        update_student(students)

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Please choose a valid option.")