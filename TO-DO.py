todo_list = []

def show_menu():
    print("\n========= TO-DO LIST MENU =========")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def show_tasks():
    print("\nYour Tasks:")
    if not todo_list:
        print("  No tasks added yet!")
    else:
        for i, task in enumerate(todo_list, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"  {i}. {task['task']} [{status}]")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def mark_done():
    show_tasks()
    if not todo_list:
        return
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            deleted = todo_list.pop(task_no - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
