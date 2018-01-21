# Script: NameAndEmailAddress.py
# Description: This program keeps names and email addresses in a dictionary as key-value pairs.
#              The program display a menu that lets the user look up a person’s email address,
#              add a new name and email address, change an existing email address, and delete an existing
#              name and email address. The program pickles the dictionary and save it to a
#              file when the user exits the program. Each time the program starts, it retrieves the
#              dictionary from the file and unpickle it.
# Programmer: William Kpabitey Kwabla.
# Date: 15.02.17



# Importing pickle to serialize the dictionary.
import pickle

    

    # Defining the intro function to display what the program does.
def intro():
    print("\t\t\t\t*******************************************************************************************")
    print("\t\t\t\t* This program keeps names and email addresses in a dictionary as key-value pairs.        *")
    print("\t\t\t\t* The program display a menu that lets the user look up a person’s email address,         *")
    print("\t\t\t\t* add a new name and email address, change an existing email address, and delete          *")
    print("\t\t\t\t* an existing name and email address. The program pickles the dictionary and save it to a *")
    print("\t\t\t\t* file when the user exits the program. Each time the program starts, it retrieves the    *")
    print("\t\t\t\t* dictionary from the file and unpickle it.                                               *")
    print("\t\t\t\t*******************************************************************************************")

def load_contacts(name_and_emails, file):
    # Open a file for binary reading.
    input_file = open('name_and_emails', 'rb')

    # Unpickle the next object.
    name_and_emails = pickle.load(input_file)

    # Close the file.
    input_file.close()

        
    # Returning the dictionary.
    return name_and_emails
        


# Defining the get menu choice function.The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print("\t\t\t\t\t\tNames and Their Emails")
    print("\t\t\t\t\t\t---------------------------")
    print("\t\t\t\t\t\t1. Look up for an Email address")
    print("\t\t\t\t\t\t2. Add a new Email address")
    print("\t\t\t\t\t\t3. Change an Email address")
    print("\t\t\t\t\t\t4. Delete an Email address")
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
def look_up(name_and_emails):

    # Getting a name to look for in dictionary.
    name = input("\t\t\t\t\t\tEnter a name: ")

    # Looking it up in the dictionary.
    print("\t\t\t\t\t\t", name_and_emails.get(name, "NOT FOUND."))

    

 

# Defining the add name and email function. The add function adds a new entry into the
# name_and_emails dictionary.
def add(name_and_emails):
    # Getting a name and email address form user.
    name = input("\t\t\t\t\t\tEnter a name: ")
    email = input("\t\t\t\t\t\tEnter an email adderss: ")

    # Checking to see if name does not exist before adding it to the dictionary.
    if name not in name_and_emails:
       name_and_emails[name] = email
       print("\t\t\t\t\t\tWriting to dictionary.......")
    else:
        print("\t\t\t\t\t\tThat entry already exists. ")

    

  
# Defining the change name and email function.The change function changes an existing
# entry in the name_and_emails dictionary.
def change(name_and_emails):
    # Getting a name to look for in the dictionary.
    name = input("\t\t\t\t\t\tEnter a name: ")

    # Checking to see if name does not exist before updating it in the dictionary
    if name in name_and_emails:
        # Getting a new email address from user.
        email = input("\t\t\t\t\t\tEnter the new email: ")

        # Updating the dictionary with user input.
        name_and_emails[name] = email
    else:
        print("\t\t\t\t\t\tThat name is not found.")




# Defining the change function.The delete function deletes an entry from the
# name_and_emails dictionary.
def delete(name_and_emails):
    # Getting a name to look for in the dictionary.
    name = input("\t\t\t\t\t\tEnter a name: ")

    # Checking to see if name does not exist before deleting it.
    if name in name_and_emails:
        del name_and_emails[name]
    else:
        print("\t\t\t\t\t\tThat name is not found. ")


# Definig the quiting function to display program quitting.
def quit():
    print("\t\t\t\t\t\tQuiting.........")



def save_contacts(name_and_emails, file):
    # Opening a file to write the dictionary to.
    output_file = open("name_and_emails.dat", "wb")

    pickle.dump(name_and_emails, file)

    output_file.close()


# Defining global constants for menu choices.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# Defining the main function.
def main():

    # Loading the existing contact assign it to my_contacts.
    # Creating a an empty dictionary to store the name and email addresses.
    name_and_emails = {}


    output_file = open("name_and_emails.dat", "wb")

    # Calling the intro function to display what the program does.
    intro()
  
   
    # Initializing the variable for the user's choice.
    choice = 0
    

    # Checking to see if user do want to quit.
    while choice != QUIT:
        
        # Getting the user's menu choice if choice is not equal to quit.
        choice = get_menu_choice()

        # Processing user's choice.
        if choice == LOOK_UP:
            load_contacts(name_and_emails, output_file)
            look_up(name_and_emails)

        elif choice == ADD:
            add(name_and_emails)

        elif choice == CHANGE:
            change(name_and_emails)

        elif choice == DELETE:
            delete(name_and_emails)
            
        elif choice == QUIT:
            save_contacts(name_and_emails, output_file)
            quit()

# Calling the main fucntion to execute the program.
main()





