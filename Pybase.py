import os
import json
import difflib
import logging
from datetime import datetime

ACTIVE_DATABASE_FILE = "active_database.json"
BACKUP_DATABASE_FILE = "backup_database.json"
LOG_FILE = "user_database_log.txt"

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE)
    ]
)

def log_event(event_message):
    logging.info(event_message)

def load_json(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []
    return data

def export_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)

def import_json(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        log_event(f"Imported data from JSON file: {file_name}")
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        log_event(f"Failed to import data from JSON file: {file_name}")
        return []

def load_active_database():
    try:
        data = load_json(ACTIVE_DATABASE_FILE)
        log_event(f"Loaded active JSON file: {ACTIVE_DATABASE_FILE}")
        return data
    except FileNotFoundError:
        log_event(f"Failed to load active JSON file: {ACTIVE_DATABASE_FILE}")
        return load_backup_database()

def load_backup_database():
    try:
        data = load_json(BACKUP_DATABASE_FILE)
        log_event("Loaded backup JSON file")
        return data
    except FileNotFoundError:
        log_event("Failed to load backup JSON file")
        return []

def save_database(data):
    export_json(ACTIVE_DATABASE_FILE, data)
    export_json(BACKUP_DATABASE_FILE, data)

def add_user(name, age, email, address, school, other):
    data = load_active_database()
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
    data = load_active_database()
    user_names = [user["Name"].lower() for user in data]

    closest_matches = difflib.get_close_matches(name.lower(), user_names)

    matching_users = []
    for match in closest_matches:
        matching_users.extend([user for user in data if user["Name"].lower() == match])

    return matching_users

def display_all_users():
    data = load_active_database()
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
    save_database(load_active_database())
    log_event(f"User edited: Name={user['Name']}, Field={field_to_edit}, Old Value={old_value}, New Value={new_value}")
    print("\nUser updated successfully!")

def create_backup():
    data = load_active_database()
    save_database(data)
    log_event("Backup created")
    print("Backup created successfully.")

def import_data():
    file_name = input("Enter the name of the JSON file to import: ")
    data = import_json(file_name)
    if data:
        save_database(data)
        print("Data imported successfully.")
    else:
        print("Failed to import data.")

def delete_user():
    name = input("Enter the name of the user to delete: ")
    users = get_user_by_name(name)
    if users:
        user_to_delete = users[0]
        data = load_active_database()
        data.remove(user_to_delete)
        save_database(data)
        log_event(f"User deleted: Name={user_to_delete['Name']}")
        print("\nUser deleted successfully!")
    else:
        print("\nUser not found.")

def pause_terminal():
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    log_event("Program opened")
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("╔═════════════════════════════════════════╗")
        print("║          User Database Program          ║")
        print("╠═════════════════════════════════════════╣")
        print("║   1. User Management                    ║")
        print("║   2. JSON Management                    ║")
        print("║   3. Exit                               ║")
        print("╚═════════════════════════════════════════╝")

        choice = input("\nEnter your choice (1/2/3): ")
        log_event(f"Selected option: {choice}")

        if choice == "1":
            while True:
                os.system("cls" if os.name == "nt" else "clear")

                print("╔═════════════════════════════════════════╗")
                print("║          User Management                ║")
                print("╠═════════════════════════════════════════╣")
                print("║   1. Add User                           ║")
                print("║   2. Get User by Name                   ║")
                print("║   3. Display All Users                  ║")
                print("║   4. Edit User                          ║")
                print("║   5. Delete User                        ║")
                print("║   6. Back                               ║")
                print("╚═════════════════════════════════════════╝")

                sub_choice = input("\nEnter your choice (1/2/3/4/5/6): ")
                log_event(f"Selected sub-option: {sub_choice}")

                if sub_choice == "1":
                    name = input("Enter the name: ")
                    age = int(input("Enter the age: "))
                    email = input("Enter the email: ")
                    address = input("Enter the address: ")
                    school = input("Enter the school: ")
                    other = input("Enter other information: ")
                    add_user(name, age, email, address, school, other)
                    pause_terminal()
                elif sub_choice == "2":
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
                elif sub_choice == "3":
                    display_all_users()
                    pause_terminal()
                elif sub_choice == "4":
                    name = input("Enter the name of the user to edit: ")
                    users = get_user_by_name(name)
                    if users:
                        edit_user(users[0])
                    else:
                        print("\nUser not found.")
                    pause_terminal()
                elif sub_choice == "5":
                    delete_user()
                    pause_terminal()
                elif sub_choice == "6":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    pause_terminal()

        elif choice == "2":
            while True:
                os.system("cls" if os.name == "nt" else "clear")

                print("╔═════════════════════════════════════════╗")
                print("║          JSON Management                ║")
                print("╠═════════════════════════════════════════╣")
                print("║   1. Export Data to JSON                ║")
                print("║   2. Import Data from JSON              ║")
                print("║   3. Create Backup                      ║")
                print("║   4. Back                               ║")
                print("╚═════════════════════════════════════════╝")

                sub_choice = input("\nEnter your choice (1/2/3/4): ")
                log_event(f"Selected sub-option: {sub_choice}")

                if sub_choice == "1":
                    data = load_active_database()
                    output_file = input("Enter the name of the output JSON file: ")
                    export_json(output_file, data)
                    log_event(f"Data exported to JSON file: {output_file}")
                    print("Data exported successfully.")
                    pause_terminal()
                elif sub_choice == "2":
                    import_data()
                    pause_terminal()
                elif sub_choice == "3":
                    create_backup()
                    pause_terminal()
                elif sub_choice == "4":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    pause_terminal()

        elif choice == "3":
            log_event("Exiting program")
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")
            pause_terminal()

    input("\nPress Enter to exit...")
