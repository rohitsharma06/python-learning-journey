tasks = []

def show_menu():
    print("========== TO-DO LIST ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("===============================")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks Available.")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task Added Successfully")

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
        tasks.pop(task_number - 1)
        print("Task Removed Successfully")
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
        print("Thank you for using To-Do List!")
        break
