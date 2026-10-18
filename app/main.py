from app.task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n=== SecureTask Manager ===")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Task title: ")
                description = input("Description: ")
                manager.add_task(title, description)
                print("Task added successfully.")

            elif choice == "2":
                tasks = manager.get_tasks()
                if not tasks:
                    print("No tasks available.")
                for index, task in enumerate(tasks):
                    status = "Done" if task.completed else "Pending"
                    print(f"{index}. {task.title} [{status}]")

            elif choice == "3":
                index = int(input("Task index: "))
                manager.complete_task(index)
                print("Task completed.")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

        except (ValueError, TypeError, IndexError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()