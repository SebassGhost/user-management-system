def show_menu():
    print("\nUser Management System")
    print("1. Register user")
    print("2. List users")
    print("3. Search user")
    print("4. Delete user")
    print("5. Exit")
def register_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")

    user = {
        "name": name,
        "email": email,
        "age": age
    }

    print("\nUser registered successfully:")
    print(user)


def main():
    while True:
        show_menu()
        option = input("Choose an option: ")

       if option == "1":
            register_user()
        elif option == "2":
            print("List users selected")
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
