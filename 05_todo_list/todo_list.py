tasks = []

def show_menu():
    print("\n================================")
    print("         TO-DO LIST")
    print("================================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("================================")

def view_tasks(tasks):
    print("\n---------- Your Tasks ----------")

    if len(tasks) == 0:
        print("No tasks available.")

    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

    print("-------------------------------")

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print(f'"{task}" added successfully.')

def remove_task(tasks):

    if len(tasks) == 0:
        print("No tasks available to remove.")
        return

    try:
        task_number = int(input("Enter task number to remove: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    if task_number >= 1 and task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'"{removed_task}" removed successfully.')
    else:
        print("Invalid Task Number!")

while True:

    show_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    print(f"You selected: {choice}")

    if choice == 1:
        view_tasks(tasks)

    if choice == 2:
        add_task(tasks)

    if choice == 3:
        remove_task(tasks)

    if choice == 4:
        print("\n================================")
        print("Thank you for using To-Do List!")
        print("Have a great day! 😊")
        print("================================")
        break
