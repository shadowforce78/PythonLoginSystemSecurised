from dbconnect import get_database
from main_game import lobby
import os
from simple_chalk import chalk


def make_account(username, password):

    db = get_database()
    accounts = db.accounts

    # Check if the username already exists
    if accounts.find_one({"username": username}):
        print(chalk.red("Username already exists!"))
        return
    else:
        accounts.insert_one({"username": username, "password": password})

    print(chalk.green("Account created successfully!"))
    print(chalk.green.underline("You can now login with your username and password."))

    main()


def login(username, password):
    db = get_database()
    accounts = db.accounts

    account = accounts.find_one({"username": username, "password": password})

    if account:
        print("Login successful!")
        print("Welcome, " + username + "!")
        os.system("cls" if os.name == "nt" else "clear")
        main_menu(account)
    else:
        print("Login failed!")
        main()

    return account


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to the account creation script!")
    print(chalk.greenBright("1. Create an account"))
    print(chalk.greenBright("2. Login"))

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("cls" if os.name == "nt" else "clear")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        make_account(username, password)
    elif choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        login(username, password)
    else:
        print(chalk.red("Invalid choice!"))
        os.system("cls" if os.name == "nt" else "clear")
        main()


def main_menu(account):
    print("Welcome to the main menu, " + account["username"] + "!")
    print(chalk.green.underline.bold("1. Play the game"))
    print(chalk.red.underline.bold("2. Logout"))

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Starting the game...")
        os.system("cls" if os.name == "nt" else "clear")
        lobby(account)
    elif choice == "2":
        print("Logging out...")
        os.system("cls" if os.name == "nt" else "clear")
        main()
    else:
        print("Invalid choice!")
        os.system("cls" if os.name == "nt" else "clear")
        main_menu(account)

    return choice, account


if __name__ == "__main__":
    main()
