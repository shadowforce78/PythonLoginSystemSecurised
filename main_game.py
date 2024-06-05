from simple_chalk import chalk
import os


def lobby(account):
    username = account["username"]
    os.system("cls" if os.name == "nt" else "clear")
    print(chalk.green.bold.underline("Welcome to the game lobby, " + username + "!"))


lobby({"username": "test"})
