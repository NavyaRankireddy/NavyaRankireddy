class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            done_task = self.tasks.pop(task_index)
            print(f"Task '{done_task}' marked as done.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            new_task = input("Enter the task to add: ")
            todo_list.add_task(new_task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            if todo_list.tasks:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                todo_list.mark_task_done(task_index)
            else:
                print("No tasks in the list.")

        elif choice == '4':
            todo_list.clear_tasks()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
