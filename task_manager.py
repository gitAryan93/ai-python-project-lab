print("📋 Welcome to Task Manager")

tasks = []

while True:
    print("\nChoose an option: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3 Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        task = {"title": title, "completed": False}
        tasks.append(task)
        print(f"✅ Task Added: {title}")

    elif choice == "2":
        if not tasks:
            print("📪 No tasks added yet.")
        else:
            print("\n📃 Your Tasks:")
            for idx, task in enumerate(tasks, start=1):
                status = "✅ Done" if task["completed"] else "❌ Not Done"
                print(f"{idx}. {task['title']} - {status}")

    elif choice == "3":
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print(f"🎯 Task '{tasks[task_num]['title']} marked as completed!")
        else:
            print("⚠️ Invalid task number.")

    elif choice == "4":
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"🗑️ Deleted task: {removed['title']}")
        else:
            print("⚠️ Invalid task number.")

    elif choice == "5":
        print("👋🏻 Exiting Task Manager. Stay productive!")
        break

    else:
        print("⚠️ Invalid choice. Please select from 1 to 5.")
