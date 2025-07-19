from collections import deque

queue = deque()

while True:
    command = input("Enter (add/view/serve/quit): ")

    if command == "add":
        name = input("Enter customer name: ")
        queue.append(name)
        print(f"{name} added to queue.")

    elif command == "view":
        print("Queue:", list(queue))

    elif command == "serve":
        if queue:
            print(f"Serving: {queue.popleft()}")
        else:
            print("Queue is empty.")

    elif command == "quit":
        break
