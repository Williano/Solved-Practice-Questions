# Script: CaloriesBurned.py
# Description: Running on a particular tredmill you burn 4.2 calories per minute.
#              This program uses a loop to display the number of calories
#              burned after 10,15,25, and 30 minutes
# Programmer: William Kpabitey Kwabla
# Date: 16.07.16



# Declaring a constant for calories per minute.
CALORIES_PER_MINUTE = 4.2


# Defining the main fuction.
def main():

    # Looping for the minutes giving.
    for minutes in range(10,35,5):
        calories = minutes * CALORIES_PER_MINUTE

        # Displaying the number of calories for each minute.
        print("The number of calories for", minutes, "is: ", calories)

# Calling the main function to execute the program.
main()

    
