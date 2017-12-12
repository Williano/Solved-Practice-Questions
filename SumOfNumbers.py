# Script: SumOfNumbers.py
# Description: This program uses a loop that asks the user to enter a series of positive numbers.
#              The user would enter a negative number to signal the end of the series.
#              After all the positive numbers have been entered, the program would display their sum.
# Programmer: William Kpabitey Kwabla
# Date: 13.06.17



def main():

    # Initialize for the while loop.
    number = 1.0

    # A variable to accumulate the total of the numbers.
    total = 0.0

    # A loop to continue adding numbers while they are positive.
    while number > 0:
        print("Enter a positive number (negative number to quit): ", end = '')
        number = eval(input())

        # Checking that number is postive so as not to change value of the total.
        if number > 0:
            total += number

    # Displaying the total of the numbers.
    print("The total of the numbers is ", format(total, ".2f")) 
    

    
main()

