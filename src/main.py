# CLI for Task Master
import sys, os

# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_master import TaskMaster

def main():
    master = TaskMaster()
    
    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            master.add_task(name, description)
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to delete: "))
                master.delete_task(task_id)
            except ValueError:
                print("Please enter a valid integer for the task ID.")
        elif choice == '3':
            master.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()