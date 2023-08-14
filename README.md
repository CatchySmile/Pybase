# Pybase
Pybase is a simple command-line application that allows you to manage a database of users. You can add, search, edit, and delete user records, as well as perform data export and import operations.

## Features
- Add users with their name, age, email, address, and other optional information.
- Search for users by their name and get close matches if an exact match is not found.
- Display all users in the database with their details, including the time they were added.
- Edit user information, including their name, age, email, address, school, and other information.
- Delete users from the database.
- Export user data to a JSON file.
- Import user data from a JSON file.
- View a log file that records program activities, including user management, data import/export, and more.

## Requirements & How to Use
- Make sure you have Python 3.6 or later installed on your system.
- Clone this repository or download the `database.py` file to your computer.
- Run the `database.py` script in your terminal or command prompt.

Upon running the script, you will be presented with a user-friendly menu that categorizes different functionalities:

![Pybase Main Menu](https://i.ibb.co/FqDPZJP/Screenshot-2023-08-14-022210.png)

### User Management
- Add a new user: Enter user details, including name, age, email, address, school, and other information.
- Search for users: Find users by name, with close match suggestions available.
- Display all users: View a list of all users stored in the database.
- Edit user information: Modify user details, including name, age, email, address, school, and more.
- Delete a user: Remove a user record from the database.

### JSON Management
- Export data to JSON: Save user data to a JSON file of your choice.
- Import data from JSON: Load user data from a JSON file and update the database.
- Create a backup: Make a backup of the current database.

### Exit
- Terminate the program: Exit the Pybase program.

## Dependencies
This project does not have any external dependencies beyond the Python standard library.

## Logs
The program logs its activities in the `user_database_log.txt` file. The log includes records of user management operations, data import/export, and more. The logging system provides insights into the program's functionality and any potential errors.
