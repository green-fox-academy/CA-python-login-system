from getpass import getpass


def get_usr_pass():
    return {"username": input("Username: "),
            "password": getpass("Password: ")}


def login():
    if account_validation(get_usr_pass()):
        print("success")
    else:
        print("bad credentials")


def account_validation(credential):
    if credential["username"] is in get_users():
        pass
    else:
        print("registrate first")
        # registrate()


def get_users():
    users = []
    for credential in get_credentials():
        users.append(credential["username"])
    return users


def get_credentials():
    with open("database", "r") as db:
        return db.read().split("\n")


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

login_engine()
