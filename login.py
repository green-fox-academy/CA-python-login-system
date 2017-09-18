def get_usr_pass():
    username = input("Username: ")
    password = input("Password: ")
    return {"username": username,
            "password": password}


def login():
    crededentials = get_usr_pass()


def registrate():
    crededentials = get_usr_pass()
    user_save(crededentials)


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
