# Script: BugCollector.py
# Descritption: This program ask for the number of bugs collected for each day,keeps running total of the
#               nunber of bugs collected and display the total number of bugs collected.
# Programmer: William Kpabitey Kwabla
# Date: 16.07.16


# Defining the main function
def main():

    # Declaring local variables
    total = 0

    # looping for each of the five days.
    for day in range(1, 6):
        print("Day:", day)

        # Getting number of bugs for each day.
        bugs_collected = eval(input("Please Enter number of bugs for today ? : "))

        # Adding the number of bugs collected to the total bug
        total += bugs_collected

        # Displaying the total number of bugs collected for the five days.
    print("The total number of bugs collected for the five days is: ", total )

# Calling the main function to execute the program.
main()
