tasks = []
while True:
    print("========== TO-DO LIST ==========")
    print("1. View Tasks \n2. Add Task \n3. Remove Task \n4. Exit")
    print("===============================")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    print(f"You selected: {choice}")

    if choice == 1:
        if len(tasks) == 0:
            print("No tasks Available.")
        else:
            for i in range(len(tasks)):
                print(f"{i +1}. {tasks[i]}")

    if choice == 2:
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added Successfully")

    if choice == 3:

        if len(tasks) == 0:
            print("No tasks available to remove.")
            continue

        try:
            task_number = int(input("Enter task number to remove: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if task_number >= 1 and task_number <= len(tasks):

            tasks.pop(task_number - 1)
            print("Task Removed Successfully")

        else:
            print("Invalid Task Number!")

    if choice == 4:
        print("Thank you for using To-Do List!")
        break
