print("📞 Welcome to Your Contact Book")

contacts = {}

while True:
    print("\nChoose an optoin:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print(f"✅ Contact Added: {name} → {number}")

    elif choice == "2":
        print("\n 📇 All contacts:")
        if not contacts:
            print(" (No contacts yet)")
        else:
            for name, number in contacts.items():
                print(f"{name}: {number}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"🔍 Found: {name} → {contacts[name]}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            new_number = input("Enter new phone number: ")
            contacts[name] = new_number
            print(f"🔂  Updated: {name} → {new_number}")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ")
        print("👋 Exiting Contact Book. Stay connected!")
        break

    else:
        print("⚠️ Invalid option. Choose 1-6.")
