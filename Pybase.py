import os
import json
import difflib
import logging
from datetime import datetime

DATABASE_FILE = "database.json"
LOG_FILE = "Pybase_log.txt"

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def log_event(event_message):
    logging.info(event_message)

def load_database():
    try:
        with open(DATABASE_FILE, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []
    return data

def save_database(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file)

def add_user(name, age, email, address, school, other):
    data = load_database()
    user = {
        "Name": name,
        "Age": age,
        "Email": email,
        "Address": address,
        "School": school,
        "Other Info": other,
        "time_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(user)
    save_database(data)
    log_event(f"User added: Name={name}, Age={age}, Email={email}, Address={address}, School={school}, Other Info={other}")

def get_user_by_name(name):
    data = load_database()
    user_names = [user["Name"].lower() for user in data]

    closest_matches = difflib.get_close_matches(name.lower(), user_names)

    matching_users = []
    for match in closest_matches:
        matching_users.extend([user for user in data if user["Name"].lower() == match])

    return matching_users

def display_all_users():
    data = load_database()
    log_event("Displayed all users")
    print("\n-- All Users --")
    for user in data:
        print(f"Name: {user['Name']}")
        print(f"Age: {user['Age']}")
        print(f"Email: {user['Email']}")
        print(f"Address: {user.get('Address', 'N/A')}")
        print(f"School: {user.get('School', 'N/A')}")
        print(f"Other Info: {user.get('Other Info', 'N/A')}")
        print(f"Time Added: {user['time_added']}")
        print("--" + "-" * 50)

def edit_user(user):
    print("\nEditing User:")
    print(f"Name: {user['Name']}")
    print(f"Age: {user['Age']}")
    print(f"Email: {user['Email']}")
    print(f"Address: {user.get('Address', 'N/A')}")
    print(f"School: {user.get('School', 'N/A')}")
    print(f"Other Info: {user.get('Other Info', 'N/A')}")

    fields = ["Name", "Age", "Email", "Address", "School", "Other Info"]
    field_to_edit = input(f"Enter the field to edit ({', '.join(fields)}): ").strip().title()

    if field_to_edit not in fields:
        print("Invalid field.")
        return

    old_value = user[field_to_edit]
    new_value = input(f"Enter the new value for {field_to_edit} (current: {old_value}): ")

    user[field_to_edit] = new_value
    save_database(load_database())
    log_event(f"User edited: Name={user['Name']}, Field={field_to_edit}, Old Value={old_value}, New Value={new_value}")
    print("\nUser updated successfully!")

def pause_terminal():
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    log_event("Program opened")
    while True:
        # Clear the terminal screen before displaying the user interface
        os.system("cls" if os.name == "nt" else "clear")

        print("╔═════════════════════════════════════════╗")
        print("║          User Database Program          ║")
        print("╠═════════════════════════════════════════╣")
        print("║   1. Add User                           ║")
        print("║   2. Get User by Name                   ║")
        print("║   3. Display All Users                  ║")
        print("║   4. Edit User                          ║")
        print("║   5. Exit                               ║")
        print("╚═════════════════════════════════════════╝")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            school = input("Enter the school: ")
            other = input("Enter other information: ")
            add_user(name, age, email, address, school, other)
            pause_terminal()
        elif choice == "2":
            name = input("Enter the name to search: ")
            users = get_user_by_name(name)
            if users:
                log_event(f"User searched by name: {name}")
                print("\nMatching users found:")
                for user in users:
                    print(f"Name: {user['Name']}")
                    print(f"Age: {user['Age']}")
                    print(f"Email: {user['Email']}")
                    print(f"Address: {user.get('Address', 'N/A')}")
                    print(f"School: {user.get('School', 'N/A')}")
                    print(f"Other Info: {user.get('Other Info', 'N/A')}")
                    print(f"Time Added: {user['time_added']}")
                    print("--" + "-" * 50)
            else:
                print("\nNo matching users found.")
                log_event(f"No matching users found for search: {name}")
            pause_terminal()
        elif choice == "3":
            display_all_users()
            pause_terminal()
        elif choice == "4":
            name = input("Enter the name of the user to edit: ")
            users = get_user_by_name(name)
            if users:
                edit_user(users[0])
            else:
                print("\nUser not found.")
            pause_terminal()
        elif choice == "5":
            log_event("Exiting program")
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")
            pause_terminal()

    input("\nPress Enter to exit...")
