import simple_chalk as chalk
import json
import os
import uuid
from cryptography.fernet import Fernet
from decrypt import decryptUUID

dbFile = "db.json"
uuidFile = "uuid.txt"


def generateKey():
    # Génère une clé et la sauvegarde dans un fichier caché
    keyFile = "key.key"
    if not os.path.exists(keyFile):
        key = Fernet.generate_key()
        with open(keyFile, "wb") as f:
            f.write(key)
        print(chalk.green("Encryption key generated!"))
    else:
        print(chalk.blue("Encryption key already exists!"))


def createUUID():
    generateKey()  # Appel de la fonction pour créer la clé
    with open("key.key", "rb") as f:
        key = f.read()
    cipher = Fernet(key)

    # Check if UUID file already exists
    if os.path.exists(uuidFile):
        print(chalk.blue("UUID already exists!"))
    else:
        myuuid = uuid.uuid4()
        encrypted_uuid = cipher.encrypt(str(myuuid).encode())
        with open(uuidFile, "wb") as f:
            f.write(encrypted_uuid)  # Écriture de l'UUID chiffré
        print(chalk.green("Encrypted UUID created successfully!"))
        if os.name == "nt":
            os.system(f"attrib +h {uuidFile}")
        else:
            os.rename(uuidFile, f".{uuidFile}")


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


def register(uuid):
    username = input("Enter username: ")
    password = input("Enter password: ")
    


def login():
    pass


def main():
    while True:
        mainMenu()

        UUID = decryptUUID()
        print(chalk.blue(f"UUID: {UUID}"))

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
    main()
