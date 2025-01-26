
tasks = []

def add_task():
    """Add a new task to the list."""
    title = input("Enter Task Title: ").strip()
    if title:
        task = {
            "title": title,
            "status": "New"  # Default status
        }
        tasks.append(task)
        print(f"Task '{title}' added successfully with status 'New'.")
    else:
        print("Task title cannot be empty. Please try again.")

def list_tasks():
    """List all tasks with their status."""
    if not tasks:
        print("No tasks available.")
        return

    print("--- List of Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Title: {task['title']} | Status: {task['status']}")

def edit_task():
    """Edit an existing task's title or status."""
    if not tasks:
        print("No tasks available to edit.")
        return

    list_tasks()
    try:
        task_num = int(input("Enter the task number to edit: ").strip())
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            print(f"Editing Task: {task['title']} (Current Status: {task['status']})")

            new_title = input("Enter new title (leave blank to keep current): ").strip()
            if new_title:
                task['title'] = new_title

            print("Select new status:")
            print("1. New\n2. In Progress\n3. Completed\n4. Cancelled")
            status_choice = input("Enter the number corresponding to the new status: ").strip()
            status_map = {"1": "New", "2": "In Progress", "3": "Completed", "4": "Cancelled"}
            if status_choice in status_map:
                task['status'] = status_map[status_choice]
                print(f"Task updated successfully! New Title: {task['title']}, Status: {task['status']}")
            else:
                print("Invalid status choice. Task status remains unchanged.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def remove_task():
    """Remove a task from the list."""
    if not tasks:
        print("No tasks available to remove.")
        return

    list_tasks()
    try:
        task_num = int(input("Enter the task number to remove: ").strip())
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' removed successfully.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n--- Todo List Application ---")
        print("1. Add New Task")
        print("2. List All Tasks")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Select your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()