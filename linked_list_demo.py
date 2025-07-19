from linked_list import LinkedList

playlist = LinkedList()

while True:
    print("\nOptions: add / show / quit")
    action = input("Choose an action: ").lower()

    if action == "add":
        song = input("Enter song name: ")
        playlist.insert(song)
        print(f"🎵 '{song}' added to playlist!")

    elif action == "show":
        print("\nYour Playlist:")
        playlist.print_list()

    elif action == "quit":
        print("👋 Playlist closed.")
        break

    else:
        print("❌ Invalid choice. Try again.")
