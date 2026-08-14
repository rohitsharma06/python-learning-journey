students = []

next_student_id = 1


def show_menu():
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. View Students")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Exit")
    print("===============================================")


def load_students():
    students = []

    try:
        file = open("students.txt", "r")

        for line in file:
            student_id, name, age, course = line.strip().split(",")

            student = {
                "id": int(student_id),
                "name": name,
                "age": int(age),
                "course": course
            }

            students.append(student)

        file.close()

    except FileNotFoundError:
        pass

    return students


def save_students(students):
    file = open("students.txt", "w")

    for student in students:
        file.write(
            f"{student['id']},{student['name']},{student['age']},{student['course']}\n"
        )

    file.close()


def view_students(students):
    if len(students) == 0:
        print("No students available.")
        return

    print("\n---------- Students ----------")

    for student in students:
        print("----------------------------")
        print(f"Student ID : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Course     : {student['course']}")

    print("----------------------------")


def add_student(students):
    global next_student_id

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
        "id": next_student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    save_students(students)

    next_student_id += 1

    print("Student added successfully.")


def delete_student(students):
    if len(students) == 0:
        print("No students available to delete.")
        return

    try:
        student_id = int(input("Enter Student ID To Delete: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print(f"{student['name']} deleted successfully.")
            return

    print("Student ID not found.")


def search_student(students):
    if len(students) == 0:
        print("No students available to search.")
        return

    try:
        student_id = int(input("Enter Student ID To Search: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    for student in students:
        if student["id"] == student_id:
            print("\n---------- Student Found ----------")
            print(f"Student ID : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Course     : {student['course']}")
            print("-----------------------------------")
            return

    print("Student ID not found.")


def update_student(students):
    if len(students) == 0:
        print("No students available to update.")
        return

    try:
        student_id = int(input("Enter Student ID To Update: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    for student in students:
        if student["id"] == student_id:

            print("\n---------- Student Found ----------")
            print(f"Student ID : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Course     : {student['course']}")
            print("-----------------------------------")

            new_name = input("Enter New Name: ").strip().title()

            if new_name == "":
                print("Name cannot be empty.")
                return

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

            student["name"] = new_name
            student["age"] = new_age
            student["course"] = new_course

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student ID not found.")


students = load_students()

if len(students) > 0:
    next_student_id = max(student["id"] for student in students) + 1


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