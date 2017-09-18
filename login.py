def login():
	print("login")

def registrate():
	print("registrate")

def login_engine():
	choice = input("0: login, 1: registrate  ")
	return {
		"0": login,
		"1": registrate
	}[choice]
			


login_engine()()	