# Script: MaleFemalePercentage.py
# Description: This program ask the user for the number of males and females
#              registered in a class. The program displays the percentage of
#              males and females in the class.
# Programmer: William Kpabitey Kwabla
# Date: 11.03.17


# Declaring the percentage variable for the percentage of the students.
PERCENTAGE = 100

# Defining the main function
def main():

    # Asking the user for the number of males in the class.
    males = int(input("Please enter the number of males in the class: "))

    # Asking the user for the number of females in the class.
    females = int(input("Please enter the number of females in the class: "))

    # Calculating the total of the number of males and females.
    total_students = males + females

    # Finding the percentage of males.
    percentage_of_males = (males / total_students) * PERCENTAGE

    # Finding the percentage of females.
    percentage_of_females = (females / total_students) * PERCENTAGE

    # Displaying the total percentage to the user.
    print("The percentage of males in the class is: ", format(percentage_of_males, ".0f"))
    print("The percentage of females in the class is: ", format(percentage_of_females, ".0f"))

# Calling the main function to start execution of the program.
main() 
