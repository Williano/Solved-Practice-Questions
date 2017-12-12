# Script: PenniesForPay.py
# Description: This program calculates the amount of money a person
#              would earn over a period of time if his or her salary is one
#              penny the first day, two pennies the second day, and continues
#              to double each day.  The program ask the user for the
#              number of days.  Display a table showing what the salary was
#              for each day, and then show the total pay at the end of the
#              period.  The output should be displayed in a dollar amount,
#              not the number of pennies.
#              The penny is a US coin worth one cent. One hundred pennies make a dollar.
#              One cent can be written 1¢ or $0.01.

# Programmer: William Kpabitey Kwabla
# Date: 19.07.16

def main():
    # Intializing the runnning total for Pay and Days
    total_pay = 0.0
    total_days = 0.0

    # Asking the user for the number of days worked.
    number_of_days = int(input('Enter the number of days worked: '))

    # Starting salary
    pay = 0.01 
    
    # Displaying the heading for Day and Salary
    print("Day\tSalary")
    print("------------------")
    
    # Creating the function to calculate the pay per day.
    for day in range(1, number_of_days + 1):
        # The penny is a US coin worth one cent. One hundred pennies make a dollar. One cent can be written 1¢ or $0.01. 
        pay *= 2

        # Adding to the running total
        total_pay += pay
        total_days += day
        
        print(day,"\t", pay)

    # State the results of the function.
    print("Your total salary for the ",number_of_days, "days is $ " ,format(total_pay,".2f"))

# Call the main function.
main()
