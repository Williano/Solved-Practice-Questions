# Module: Birthdays.py
# Description: This program uses a dictionary to keep friends'
#              name and birthdays.
# Programmer: William Kpabitey Kwabla.
# Date: 12.02.17


# Defining global constants for menu choices.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Defining the main function
def main():

    # Calling the intro function.
    intro()

    # Creating an empty dictionary.
    birthdays = {}

    # Initializing the variable for the user's choice.
    choice = 0


    # Checking to see if user do want to quit.
    while choice != QUIT:
        # Getting the user's menu choice if choice is not equal to quit.
        choice = get_menu_choice()

        # Processing user's choice.
        if choice == LOOK_UP:
            look_up(birthdays)

        elif choice == ADD:
            add(birthdays)

        elif choice == CHANGE:
            change(birthdays)

        elif choice == DELETE:
            delete(birthdays)



# Defining the intro function to display what the program does.
def intro():
    print("\t\t\t*****************************************************************************")
    print("\t\t\t* This is a menu driven program that uses a dictionary to keep friends      *")
    print("\t\t\t* name and birthdays.It allows user's to LOOK FOR, ADD, CHANGE and DELETE   *")
    print("\t\t\t* names and birthdays from the dictionary.                                  *")
    print("\t\t\t*****************************************************************************")
    print()
    


# Defining the get menu choice function.The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print("\t\t\t\t\t\tFriends and Their Birthdays")
    print("\t\t\t\t\t\t---------------------------")
    print("\t\t\t\t\t\t1. Look up a birthday")
    print("\t\t\t\t\t\t2. Add a new birthday")
    print("\t\t\t\t\t\t3. Change a birthday")
    print("\t\t\t\t\t\t4. Delete a birthday")
    print("\t\t\t\t\t\t5. Quit the program")
    print()

    # Getting the user's choice.
    choice = int(input("\t\t\t\t\t\tEnter your choice: "))

    # Validating the user's choice to make sure he/she doesn't enter
    # a choice outside the range of choices.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("\t\t\t\t\t\tEnter a valid choice: "))

    # Returning the user's choice to the function header.
    return choice



# Defining the look up function. The look_up function looks up a name in the
# birthdays dictionary.
def look_up(birthdays):
    # Getting a name to look for in dictionary.
    name = input("\t\t\t\t\t\tEnter a name: ")

    # Looking it up in the dictionary.
    print("\t\t\t\t\t\t", birthdays.get(name, "NOT FOUND."))




# Defining the add birthday function. The add function adds a new entry into the
# birthdays dictionary.
def add(birthdays):
    # Getting a name and birthday form user.
    name = input("\t\t\t\t\t\tEnter a name: ")
    bday = input("\t\t\t\t\t\tEnter a birthday: ")

    # Checking to see if name does not exist before adding it to the dictionary.
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print("\t\t\t\t\t\tThat entry already exists. ")



# Defining the change birthday function.The change function changes an existing
# entry in the birthdays dictionary.
def change(birthdays):
    # Getting a name to look for in the dictionary.
    name = input("\t\t\t\t\t\tEnter a name: ")

    # Checking to see if name does not exist before updating it in the dictionary
    if name in birthdays:
        # Getting a new birthday from user.
        bday = input("\t\t\t\t\t\tEnter the new birthday: ")

        # Updating the dictionary with user input.
        birthdays[name] = bday
    else:
        print("\t\t\t\t\t\tThat name is not found.")




# Defining the change function.The delete function deletes an entry from the
# birthdays dictionary.
def delete(birthdays):
    # Getting a name to look for in the dictionary.
    name = input("\t\t\t\t\t\tEnter a name: ")

    # Checking to see if name does not exist before deleting it.
    if name in birthdays:
        del birthdays[name]
    else:
        print("\t\t\t\t\t\tThat name is not found. ")



# Calling the main function to start the execution of the program.
main()

    








     
