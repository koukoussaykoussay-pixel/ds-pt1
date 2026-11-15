tasks = []


def add_task():
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append(title)
    print("Task added successfully.")


def display_tasks():
    if not tasks:
        print("There are no tasks yet.")
        return

    for number, title in enumerate(tasks, start=1):
        print(f"{number}. {title}")


def search_tasks():
    keyword = input("Keyword to search for: ").strip()
    if not keyword:
        print("Search keyword cannot be empty.")
        return

    matches = [
        (number, title)
        for number, title in enumerate(tasks, start=1)
        if keyword.casefold() in title.casefold()
    ]

    if not matches:
        print("No matching tasks found.")
        return

    for number, title in matches:
        print(f"{number}. {title}")


def main():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Search for a task")
        print("0. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            search_tasks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Error: please choose 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
