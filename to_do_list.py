print("📝 Welcome to Your To-Do List Manager")

todo_list = []

while True:
    print ("\nChoose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input ("Enter your choice (1-4): ")
     
    if choice == "1":
        task =  input ("Enter a new task: ")
        todo_list.append(task)
        print(f"✅ Task added: {task}")

    elif choice == "2":
        print("\n📋 Your Tasks: ")
        if not todo_list:
            print(" (No tasks yet)")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not todo_list:
            print("❌ Nothing to remove. Your list is empty.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
                index = int (input("Enter the task number to remove: "))
                if 1 <= index <= len(todo_list):
                    removed = todo_list.pop(index - 1)
                    print (f"🗑️ Removed: {removed}")
                else:
                    print ("⚠️ Invalid task number.")
    elif choice == "4":
        print("👋 Existing To-Do List Manager. Stay productive!")
        break

    else:
        print ("⚠️ Invalid option. Choose 1-4.")

