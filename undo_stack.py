stack = []

while True:
    action = input("Enter action (type text / undo / quit): ")

    if action == "quit":
        break
    elif action == "undo":
        if stack:
            undone = stack.pop()
            print(f"Undid: {undone}")
        else:
            print("Nothing to undo.")
    else:
        stack.append(action)
        print(f"Current Stack: {stack}")
