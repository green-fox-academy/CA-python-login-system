def get_usr_pass():
    username = input("Username: ")
    password = input("Password: ")
    return {"username": username,
            "password": password}


def login():
    crededentials = get_usr_pass()
    if crededentials["password"] == get_password(crededentials["username"]):
        print("success")
    else:
        print("bad credentials")


def get_password(username):
    with open("database", "r") as db:
        crededentials = db.read().split("\n")
    for credential in crededentials:
        if username == credential.split(":")[0]:
            return credential.split(":")[1]

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
