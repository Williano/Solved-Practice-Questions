# Module: TotalSales.py
# Description: This program asks the user to enter a store’s sales
#              for each day of the week. The amounts is 
#              stored in a list.Using a loop to calculate the total
#              sales for the week and display the result.
# Programmer: William Kpabitey Kwabla
# Date: 05.02.17


# Declaring number of days as a constant.
NUM_OF_DAYS = 7

def main():

    # Calling the intro function
    intro()

    # Creating an empty list to store daily sales from user
    daily_sales = []
    

    # Asking user for sales for each day
    print("Please enter the sales for each Day.")
    
    for days in range(1,NUM_OF_DAYS + 1):
        print('Day #', days , ': ', sep='', end='')
        sales = float(input("$ "))
        # Appending users input to the daily sales list
        daily_sales.append(sales)

    # Assigning the total sales for the week by calling the get total
    # function and assigning the daily list as argument to it which
    # will return the total weekly sales and store in the sales total.
    sales_total = get_total(daily_sales)

    # Displaying the to total sales for the week.
    print()
    print("The total sales for the week is $ ", sales_total )
    

# Defining the intro function to tell user what the program does.
def intro():
    print("\t\t*********************************************************")
    print("\t\t*  This program asks the user to enter a store’s sales  *")
    print("\t\t*  for each day of the week. The amounts is             *")
    print("\t\t*  stored in a list.Using a loop to calculate the total *")
    print("\t\t*  sales for the week and display the result.           *")
    print("\t\t*********************************************************")
    print()

# Defining the get total function and assigning the daily_sales list as
# parameter variable and returning the total sales to the the part of the
# program that called it.
def get_total(sales_list):

    # Initializing the total sales variable
    total_sales = 0.0

    # Looping through the daily sales list to calculate the total sales for the week.
    for total in sales_list:
        total_sales += total

    # Returning the total sales to get total function.
    return total_sales
    

# Calling the main funcion to start execution of the program.
main()
    
