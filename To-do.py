def show_menu():
    print("MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("TASKS")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")


def mark_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        print(f"Marked '{tasks[task_number-1]}' as completed.")
        tasks.pop(task_number-1)
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        print(f"Deleted '{tasks[task_number-1]}' from the list.")
        tasks.pop(task_number-1)
    else:
        print("Invalid task number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
    
