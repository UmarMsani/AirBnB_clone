# 0x00. AirBnB clone - The console

# Description
The Airbnb Console is a command-line interface (CLI) for managing data related to accommodations on the Airbnb platform. It allows users to interact with the system through a series of commands, providing functionalities such as creating, displaying, updating, and deleting instances of different types of accommodations.

# Command Interpreter
Starting the Interpreter
To start the Airbnb Console, follow these steps:

Open a terminal window.

Navigate to the directory containing the Airbnb Console script.

Run the script using the command:

./console.py

This will launch the command interpreter and present you with the (hbnb) prompt.

# Using the Interpreter
The command interpreter supports the following commands:

create: Creates a new instance of a given class and saves it to a JSON file.

show: Displays the string representation of an instance based on the class name and id.

destroy: Deletes an instance based on the class name and id.

all: Prints string representations of all instances or those of a specific class.

update: Updates an instance based on the class name and id by adding or updating attributes.

count: Retrieves the number of instances of a class.

quit: Exits the console.

EOF: Exits at End of File (use Ctrl + D on the keyboard).

# Examples
Creating a new User instance:  (hbnb) create User
Showing an instance:   (hbnb) show User (id)
Listing all instances: (hbnb) all
Exiting the console:   (hbnb) quit 
