from playlist import Playlist

# Create a Playlist object
playlist = Playlist()

# Run the program in a loop
while True:
    print("\nOptions: add / show / quit")
    choice = input("What do you want to do? ").lower()

    if choice == "add":
        song = input("Enter song name: ")
        playlist.add_song(song)

    elif choice == "show":
        playlist.show()

    elif choice == "quit":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")
