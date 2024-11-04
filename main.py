import simple_chalk as chalk
import json
import os
import uuid

dbFile = "db.json"


def createUUID():
    myuuid = uuid.uuid4()  # Generate a random UUID
    uuidFile = "uuid.txt"
    with open(uuidFile, "w") as f:
        f.write(str(myuuid))  # Write the UUID to the file
    print(chalk.green("UUID created successfully!"))
    os.system(f"attrib +h {uuidFile}")  # Hide the file


def mainMenu():
    print(chalk.yellow("Main Menu"))
    print(chalk.green("1. Login"))
    print(chalk.green("2. Register"))
    print(chalk.red("3. Exit"))


def registerMenu():
    print(chalk.yellow("Register Menu"))
    print(chalk.green("1. Register"))
    print(chalk.red("2. Back"))


def loginMenu():
    print(chalk.yellow("Login Menu"))
    print(chalk.green("1. Login"))
    print(chalk.red("2. Back"))


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    data = {"username": username, "password": password}
    with open(dbFile, "w") as f:
        json.dump(data, f)
    print(chalk.green("Registered successfully!"))


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open(dbFile, "r") as f:
        data = json.load(f)
    if data["username"] == username and data["password"] == password:
        print(chalk.green("Logged in successfully!"))
    else:
        print(chalk.red("Invalid credentials!"))


def main():
    while True:
        mainMenu()
        choice = input("Enter your choice: ")
        if choice == "1":
            loginMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                login()
            elif choice == "2":
                continue
            else:
                print(chalk.red("Invalid choice!"))
        elif choice == "2":
            registerMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                register()
            elif choice == "2":
                continue
            else:
                print(chalk.red("Invalid choice!"))
        elif choice == "3":
            break
        else:
            print(chalk.red("Invalid choice!"))


if __name__ == "__main__":
    createUUID()
