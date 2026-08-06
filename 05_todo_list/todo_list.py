tasks = []
while True:
    print("========== TO-DO LIST ==========")
    print("1. View Tasks \n2. Add Task \n3. Remove Task \n4. Exit")
    print("===============================")

    choice = int(input("Enter your choice: "))
    print(f"You selected: {choice}")

    if choice == 1:
        for i in range(len(tasks)):
            print(f"{i +1}. {tasks[i]}")

    if choice == 2:
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added Successfully")

    if choice == 3:
        task_number = input("Enter task number to remove: ")
        tasks.remove(task_number)
        print("Task Removed Successfully")

    if choice == 4:
        print("Thank you for using To-Do List!")
        break
