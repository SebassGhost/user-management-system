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

    # Check for duplicate email
    for user in users:
        if user["email"] == email:
            print("\nEmail already registered.")
            return

    user = {
        "name": name,
        "email": email,
        "age": age
    }

    users.append(user)
    save_users(users)
    print("\nUser registered successfully")

# List users
def list_users(users):
    if not users:
        print("\nNo users registered.")
        return

    print("\nRegistered Users:")
    for i, user in enumerate(users, start=1):
        print(f"{i}. Name: {user['name']} | Email: {user['email']} | Age: {user['age']}")

# Search user by email
def search_user(users):
    email = input("Enter email to search: ")

    for user in users:
        if user["email"] == email:
            print("\nUser found:")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Age: {user['age']}")
            return

    print("\nUser not found.")

# Delete user by email
def delete_user(users):
    email = input("Enter email to delete: ")

    for user in users:
        if user["email"] == email:
            users.remove(user)
            save_users(users)
            print("\nUser deleted successfully.")
            return

    print("\nUser not found.")

# Main function
def main():
    users = load_users()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            register_user(users)
        elif option == "2":
            list_users(users)
        elif option == "3":
            search_user(users)
        elif option == "4":
            delete_user(users)
        elif option == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Try again.")

if __name__ == "__main__":
    main()
