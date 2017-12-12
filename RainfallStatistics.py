# Module: RainfallStatistics.py
# Description: This program lets the user enter the total rainfall for each of
#              12 months into a list. The program then calculate and display the total
#              rainfall for the year, the average monthly rainfall, and the months
#              with the highest and lowest amounts.
# Programmer: William Kpabitey Kwabla
# Date: 05.02.17


# Declaring number of months as a constant.
NUM_OF_MONTHS = 12

def main():

    # Calling the intro function
    intro()

    # Creating an empty list to store monthly rain from user
    monthly_rain = []
    

    # Asking user for rain for each month.
    print("\tPlease enter the amount of rainfall for each month.")
    
    for months in range(1,NUM_OF_MONTHS + 1):
        print('\tMonth #', months , ': ', sep='', end='')
        rain = float(input())
        # Appending users input to the monthly rain list
        monthly_rain.append(rain)

    # Assigning the total sales,average rain, the month with highest and lowest amount 
    # of rain by calling the get total, get average, get highest and get lowest 
    # function and assigning the monthly rain to the get total, get highest, get lowest
    # fuctions, and assinging the total rainfall varible to the get average variable
    # as argument to them which will return the total amount of rainfall, average rainfall,
    # month with highest and lowest rainfall and store in the total rainfall, average rain,
    # highest rain variables.
    total_rainfall = get_total(monthly_rain)
    average_rain = get_average(total_rainfall)
    highest = get_highest(monthly_rain)
    lowest = get_lowest(monthly_rain)

    # Displaying the total rain, average rain for the year and the months with the
    # highest and lowest rainfall.
    print()
    print("\tThe total rainfall for the year is ", total_rainfall)
    print("\tThe average monthly rainfall for the year is ", average_rain)
    print("\tThe month with the highest amount of ranifall is ", highest)
    print("\tThe month with th lowest amount of rainfall is ", lowest)
    print()
    

# Defining the intro function to tell user what the program does.
def intro():
    print("\t\t********************************************************************************")
    print("\t\t*   This program lets the user enter the total rainfall for each of            *")
    print("\t\t*   12 months into a list. The program then calculate and display the total    *")
    print("\t\t*   rainfall for the year, the average monthly rainfall, and the months        *")
    print("\t\t*   with the highest and lowest amounts.                                       *")
    print("\t\t********************************************************************************")
    print()

# Defining the get total function and assigning the monthly rain list as
# parameter variable and returning the total rainfall to the the part of the
# program that called it.
def get_total(rainfall_list):

    # Initializing the total rain variable.
    total_rain = 0.0

    # Looping through the monthly rain list to calculate the total sales for the week.
    for total in rainfall_list:
        total_rain += total

    # Returning the total rain to get total function.
    return total_rain

def get_average(rain_total):
    # Calculating the average amount of rainfall for the year.
    average = rain_total / NUM_OF_MONTHS

    # Returning the average amount of rainfall to the get average function.
    return average

def get_highest(rainfall_list):
    highest_month = max(rainfall_list)

    # Returning the month with the highest rainfall.
    return highest_month

def get_lowest(rainfall_list):
    lowest_month = min(rainfall_list)

    # Returning the month with the highest rainfall.
    return lowest_month

# Calling the main funcion to start execution of the program.
main()
    
