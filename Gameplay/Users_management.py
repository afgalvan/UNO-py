import json

global username

def load_json():
    file = open("Gameplay/Users.json", "r")
    users_data = json.load(file)
    return users_data


def show_users():
    users_data = load_json()
    print(users_data["Users"])


def update_users(users_data):
    info = json.dumps(users_data, indent=2)
    
    change_file = open("Gameplay/Users.json", "w")
    change_file.write(info)
    change_file.close()


def create_user():
    users_data = load_json()
    
    invalid_username = True
    while invalid_username:
        username = input("\nEnter new username: ")
        invalid_username = user_validation(username)
        if invalid_username: print("\nUsername already taken.")

    new_data = {"Username": username, "Matches": 0,
                "Wins": 0, "Loses": 0, "Winrate": 0}
    
    users_data["Users"].append(new_data)
    update_users(users_data)
    
    return username

def load_user():
    users_data = load_json()
    
    exists = False
    while not exists:
        username = input("\nEnter your username: ")
        exists = user_validation(username)
        if not exists: print("\nUsername not registered.")
    return username


def user_validation(username):
    users_data = load_json()
        
    for user in users_data["Users"]:
        if user["Username"].lower() == username.lower():
            return True
    return False


def save_stats(username, matches, wins, loses):
    users_data = load_json()
    for user in users_data["Users"]:
        if user["Username"].lower() == username.lower():
            replace = user
            user["Matches"] += matches
            user["Wins"] += wins
            user["Loses"] += loses
            user["Winrate"] = user["Wins"] / user["Matches"] * 100
            break
            # print("Winrate: {0:.0f}%".format(user["Winrate"]))

    i = users_data["Users"].index(replace)
    users_data["Users"][i] = replace

    update_users(users_data)
