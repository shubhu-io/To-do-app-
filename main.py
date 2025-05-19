from todo import TodoApp

def print_menu():
    print("\n=== TODO App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("==============")

def main():
    app = TodoApp()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            task = app.add_task(description)
            print(f"Task added with ID: {task['id']}")
            
        elif choice == '2':
            tasks = app.view_tasks()
            if not tasks:
                print("No tasks found!")
            else:
                print("\nYour Tasks:")
                for task in tasks:
                    status = "✓" if task['completed'] else " "
                    print(f"{task['id']}. [{status}] {task['description']} (Created: {task['created_at']})")
                    
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            if app.mark_complete(task_id):
                print("Task marked as complete!")
            else:
                print("Task not found!")
                
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            if app.delete_task(task_id):
                print("Task deleted!")
            else:
                print("Task not found!")
                
        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()