from dbconnect import get_database
from main_game import lobby


def make_account(username, password):
    db = get_database()
    accounts = db.accounts

    # Check if the username already exists
    if accounts.find_one({"username": username}):
        print("Username already exists!")
        return
    else:
        accounts.insert_one({"username": username, "password": password})

    print("Account created successfully!")
    print("You can now login with your username and password.")

    main()


def login(username, password):
    db = get_database()
    accounts = db.accounts

    account = accounts.find_one({"username": username, "password": password})

    if account:
        print("Login successful!")
        print("Welcome, " + username + "!")
        main_menu(account)
    else:
        print("Login failed!")
        main()

    return account


def main():
    print("Welcome to the account creation script!")
    print("1. Create an account")
    print("2. Login")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        make_account(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        login(username, password)
    else:
        print("Invalid choice!")
        main()


def main_menu(account):
    print("Welcome to the main menu, " + account["username"] + "!")
    print("1. Play the game")
    print("2. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Starting the game...")
        lobby(account)
    elif choice == "2":
        print("Logging out...")
        main()
    else:
        print("Invalid choice!")
        print("\n" * 100)
        main_menu(account)

    return choice, account


if __name__ == "__main__":
    main()