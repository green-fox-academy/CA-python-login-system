from getpass import getpass
import sys


def get_usr_pass():
    return {"username": input("Username: "),
            "password": getpass("Password: ")}


def login():
    if account_validation(get_usr_pass()):
        print("success")
    else:
        print("bad credentials")

def account_validation(credential):
    if credential["username"] in get_users():
        return True
    else:
        print("registrate first")
        registrate()


def get_users():
    users = []
    for credential in get_credentials():
        users.append(get_username_from_credential(credential))
    return users


def get_credentials():
    try:
        with open("database", "r") as db:
            return db.read().split("\n")
    except FileNotFoundError:
        print("Database not found")
        sys.exit(2)


def get_password(username):
    for credential in get_credentials():
        if username == get_username_from_credential(credential):
            return get_password_from_credential(credential)


def get_password_from_credential(credential):
    return credential.split(":")[1]


def get_username_from_credential(credential):
    return credential.split(":")[0]


def registrate():
    user_save(get_usr_pass())


def user_save(crededentials):
    with open("database", "a") as db:
        db.write(crededentials["username"] + ":" +
                 crededentials["password"] + "\n")


def choice_manager(choice):
    return {
        "0": login,
        "1": registrate
    }[choice]


def login_engine():
    try:
        choice_manager(input("0: login, 1: registrate  "))()
    except KeyError:
        print("bad choice, dumbass")


try:
    login_engine()
except KeyboardInterrupt:
    print("interrupted")
except:
    raise    