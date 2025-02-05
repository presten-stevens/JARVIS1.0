# CLI for Task Master
def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            view_all_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def print_menu():
    print("Hello, welcome to Task Master!")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit")

if __name__ == "__main__":
    main()