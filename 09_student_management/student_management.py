students = []

def show_menu():
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. View Students")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Exit")
    print("===============================================")

def view_students(students):
    if len(students) == 0:
        print("No student Available")
        return

    print("\n---------- Students ----------")

    for i in range(len(students)):
        print("----------------------------")
        print(f"Student : {i + 1}")
        print(f"Name    : {students[i]['name']}")
        print(f"Age     : {students[i]['age']}")
        print(f"Course  : {students[i]['course']}")

def add_student(students):
    name = input("Enter Student Name:")
    age = int(input("Enter Student Age:"))
    course = input("Enter Student Course:")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully.")

def delete_student(students):
    if len(students) == 0:
        print("No student Available to delete.")
        return

    student_number = int(input("Enter Student Number To delete:"))

    if student_number >= 1 and student_number <= len(students):
        removed_student = students.pop(student_number - 1)

        print(f"{removed_student['name']} deleted successfully.")

    else:
        print("Invalid Student Number.")

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
        print("Thank you for using Student Management System.")
        break

    else:
        print("Please choose a valid option.")

