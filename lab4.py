list_users = []

is_continued = True
logged_in = False

def create_user():
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    age = input("Enter your age: ")

    while age_is_number(age) is False:
        print("Your age should be an integer number")
        age = input("Please enter your age again: ")

    address = input("Enter your address: ")
    username = input("Enter your username: ")
    
    while check_username_unique(username) is False:
        username = input("Enter your username: ")

    password = input("Enter your password: ")

    while password_is_valid(password) is False:
        print("Your password is too short")
        password = input("Enter a new password longer than 8 characters: ")

    user = {
        "Name": name,
        "Surname": surname,
        "Age" : age,
        "Address": address,
        "Username": username,
        "Password": password,
    }

    list_users.append(user)

    print("A new user has been created")
    print()

def age_is_number(age: str) -> bool:
    if age.isnumeric():
        return True
    else:
        return False

def password_is_valid(password: str) -> bool:
    if len(password) <= 8:
        return False
    else:
        return True

def check_username_unique(username: str) -> bool:
    for user in list_users:
        if user.get("Username") == username:
            print("A user with such username already exists")
            return False
    return True

def username_exists(username: str) -> dict | bool:
    for user in list_users:
        if user.get("Username") == username:
            return user
        
    return False

def login_by_username(username: str) -> bool:

    if username_exists(username) is False:
        print("No such user found")
        return
    else:
        user = username_exists(username)

    password = input("Enter your password: ")

    if user.get("Password") == password:
        print("You have logged in")
        return True
    print("Your password is incorrect")
    return False

def update_user(user: dict):
    print("Which data would you like to update?")
    print("1. Name")
    print("2. Surname")
    print("3. Age")
    print("4. Username")
    print("5. Password")
    print("6. Don't update anything")

    action = input("Choose the data to update: ")

    match action:
        case "1":
            new_name = input("Enter a new name: ")
            user["Name"] = new_name

        case "2":
            new_surname = input("Enter a new surname: ")
            user["Surname"] = new_surname

        case "3":
            new_age = input("Enter new age: ")
            user["Age"] = new_age

        case "4":
            new_username = input("Enter your new username: ")
            user["Username"] = new_username

        case "5":
            new_password = input("Enter your new password: ")
            user["Password"] = new_password

        case "6":
            return
        
        case _:
            print("Unknown command")
            return 
        
    print("Your data has been updated")

def see_list_users():
    for user in list_users:
        for key, value in user.items():
            if key == "Password":
                continue
            print(f'{key}: {value}', end = " ")
        print()

def delete_user_my_username(username):
    if username_exists(username) is False:
        print("No such user found")
    else:
        user = username_exists(username)
        list_users.remove(user)
        print("The user has been deleted")

def print_available_actions(logged_in):
    if logged_in is True:
        print("1. Update user data")
        print("2. Show list of users")
        print("3. Delete user from the list")
        print("4. Log out")
        print("5. Exit")
        print()

    elif logged_in is False:
        print("1. Create a new user")
        print("2. Show list of users")
        print("3. Delete user from the list")
        print("4. Sign in")
        print("5. Exit")
        print()

while is_continued:
    print("Below you can find the available actions")
    print_available_actions(logged_in)
    action = input("Choose what you want to do by entering a number: ")

    match action:
        case "1":
            if logged_in is True:
                user = username_exists(username)
                update_user(user)
            elif logged_in is False:
                create_user()
        
        case "2":
            if len(list_users) == 0:
                print("There are no users")
            else:
                see_list_users()

        case "3":
            if logged_in is True:
                delete_user_my_username(username)
                
            elif logged_in is False:
                print("You need to login first before deleting the user")
                username = input("Enter your username: ")
                login_by_username(username)
                delete_user_my_username(username)
            loggen_in = False

        case "4":
            if logged_in is True:
                print("You have logged out")
                logged_in = False

            elif logged_in is False:
                username = input("Enter your username: ")
                logged_in = login_by_username(username)

        case "5":
            is_continued = False

        case _:
            print("Unknown command, please enter a number from 1 to 5")
            