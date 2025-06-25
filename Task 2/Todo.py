import os

# Get the directory of the current script (task2 folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.txt")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [task.strip() for task in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("✅ No tasks in your to-do list.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("🔹 Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("🔻 Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 Removed: {removed}\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("👉 Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()