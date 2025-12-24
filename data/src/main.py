import json
import os

# Load users from JSON file
def load_users():
    if not os.path.exists("users.json"):
        return []
    with open("users.json", "r") as file:
        return json.load(file)

# Save users to JSON file
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Show menu
def show_menu():
    print("\nUser Management System")
    print("1. Register user")
    print("2. List users")
    print("3. Search user")
    print("4. Delete user")
    print("5. Exit")

# Register user
def register_user(users):
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")

    user = {
        "name": name,
        "email": email,
        "age": age
    }

    users.append(user)
    save_users(users)
    print("\nUser registered successfully")

def main():
    users = load_users()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            register_user(users)
        elif option == "2":
            print(users)
        elif option == "3":
            print("Search user selected")
        elif option == "4":
            print("Delete user selected")
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
