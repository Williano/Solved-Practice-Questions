# Script: BudgetAnalysis.py
# Description: This program asks the user to enter the amount that he or she has budgeted for
#              a month. A loop then prompt the user to enter each of his or her expenses for the
#              month and keep a running total. When the loop finishes, the program display the
#              amount that the user is over or under budget.
# Programmer: William Kpabitey Kwabla.
# Date: 16.07.16


# Defining the main function.
def main():

     # Declaring and intializing a local variable to the keep the running total.
    total_expenses = 0.0


    # Asking user for the month and number of days in the month.
    month = input("What months budgets it's: ")
    print("How many days are in", month , ': ', sep=' ', end='')
    num_of_days = int(input()) 
    

     # Asking user for the amount budgeted for a month.
    month_budget = float(input("Please Enter the amount budgeted for this month $: "))
    print()

    print("Please enter each of your expenses for this month:")


    # Looping through the number of days to get the expenses for each day.
    for days in range(1, num_of_days + 1):
        # Asking user for daily expenses for the month.
        print("Day#", days , ': ', sep='', end='')
        expenses = float(input())

        # Adding the expenses to the running total expenses.
        total_expenses += expenses

    # Displaying the total expenses.
    print("Your total expenses is", format(total_expenses, ",.2f"))
    print()

    # Checking if expenses is under or over budget.
    if month_budget > total_expenses:
        # Displaying if expenses is under budget.
        print("Your expenses is UNDER the monthly budget.")
        print()

    else:
        # Displaying if expenses is over budget.
        print("Your expenses is OVER the monthly budget.")
        print()

            


# Calling the main function to execute the program.
main()

        
        

    

    
