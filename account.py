
database = {}

#Failed attempts
tries = 0


#Sign up
while True:
    signUp = input("Would you like to sign up (Y/n): ").lower()
    if signUp == "n":
        break
    elif signUp == "y":
        while True:
            username = input("Enter username or press 'Q' to exit (must be at least 8 characters): ")
            if username.lower() == 'q':
                break
            if len(username) < 8:
                print("Username must be at least 8 characters long")
                continue
            elif username in database.keys():
                print("Username already exist")
                continue
            else:
                while True:
                    password = input("Enter password or press 'Q' to exit: ")
                    if password.lower() == 'q':
                        break
                    repeat = input("Repeat password: ")
                    if password != repeat:
                        print("Passwords do not match. Try again")
                        continue
                    else:
                        database[username] = None
                        database.update({username: password})
                        print("Welcome")
                        break
                break
        break
    else:
        print("Invalid input")
        continue


#Sign in
while True:
    signIn = input("Would you like to sign in (Y/n): ").lower()
    if signIn == "n":
        break
    elif signIn == "y":
        while True:
            username = input("Enter username: ")
            if username not in database.keys():
                print("Username does not exist")
                continue
            else:
                while True:
                    password = input("Enter password: ")
                    if password != database.get(username):
                        print("Incorrect password")
                        print(f"{3 - tries} tries left")
                        tries += 1
                        if tries == 3:
                            print("3 consecutive incorrect attempts. Exiting program.")
                            exit()
                    else:
                        for username in database.keys():
                            print(f"Welcome '{username}'")
                            break
        break
    else:
        print("Invalid input")
        continue
    
        

