# Script: MultiplicationTable.py
# Description: This program ask for a number and limit and generates
#              multiplication table for it.

# Programmer: William Kpabitey Kwabla
# Date: 20.07.16


# Defines the main function.
def main():
    # Calls the intro function
    intro()

    # Declares variable for repeating the loop.
    keep_going = 'Y' or 'y'
    
    # Loop for asking user for another input.
    while keep_going == 'Y' or keep_going == 'y':
            print()
        
            # Asks user for the limit
            limit = int(input("\t\t\tPlease Enter the limit you want to display to: "))
        

            # Asks user for the number
            number = int(input("\t\t\tPlease Enter the number you want to display the multiplication table of : "))
            print()

            # Displays the heading.
            print("\t\t\t\t\t\tMultiplication of ", number)
            print("\t\t\t\t\t************************************")

            # Calls the multiplication function.
            multiplication(limit, number)

            # Asks User if he/she wants to check for another number.
            keep_going = input("\t\t\tDo you want to check for another number ? Yes = y or Y   No = N or n: ")
            

# Defines the intro function to display what the program does.
def intro():
    print("\t\t\t*********************************************************")
    print("\t\t\t*\tThis program ask for a number and limit and \t*")
    print("\t\t\t*\tgenerates multiplication table for it.      \t*")
    print("\t\t\t*********************************************************")
    

# Defines the multiplication function and using the num_limit and number_choice as parameter variables.
def multiplication(num_limit, number_choice):
    
    # Loops and displays the multiplication table
    for num in range( num_limit + 1 ):
            ans = num * number_choice
            print('\t\t\t\t\t\t', num, "X", number_choice, "=" ,ans)
            print()

            
    
# Calls the main function.
main()
