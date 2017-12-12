# Script: color_mixer
# Description: This program that prompts the user to enter the names of two primary colors to mix.
#              If the user enters anything other than “red,” “blue,” or “yellow,” the program should display
#              an error message. Otherwise, the program should display the name of the secondary
#              color that results.

# Programmer: William Kpabitey Kwabla
# Date: 25.05.16

# Declaring primary colors as constants.
COLOR1 = "red"
COLOR2 = "yellow"
COLOR3 = "blue"


# Defining the main function.
def main():

    # Displaying to the user what the program does.
    print("This program that prompts the user to enter the names of two primary colors to mix.")
    print("If the user enters anything other than “red,” “blue,” or “yellow,” the program should display")
    print("an error message. Otherwise, the program should display the name of the secondary")
    print("color that results.")
    print()

    # Asking user to enter first primaray color to mix and assigning to the variable primary color1.
    primary_color1 = input("Please Enter first primary color to mix: ")


    # Asking user to enter second primaray color to mix and assigning to the variable primary color2.
    primary_color2 = input("Please Enter second primary color to mix: ")

    # Determining whether user entered right primary color and Displaying secondary color if so.
    if primary_color1 == COLOR1 and primary_color2 == COLOR3:
        print("The secondary color is:","PURPLE")

    elif primary_color1 == COLOR1 and primary_color2 == COLOR2:
        print("The secondary color is:","ORANGE")

    elif primary_color1 == COLOR3 and primary_color2 == COLOR2:
        print("The secondary color is:","GREEN")

    else:
        print("Color out of range.Please enter right primary colors.")


# Calling the main function.
main()
    
    
