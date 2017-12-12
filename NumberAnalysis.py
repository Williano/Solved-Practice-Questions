# Script: NumberAnalysis.py
# Description: This program a user for 20 series of numbers and store the numbers in
#              a list and then display the lowest,highest,total and average of the list.
# Programmer: William Kpabitey Kwabla.
# Date: 14.03.17


# Defining the minimum function to find the lowest number in the list by passing the
# numbers_list as an argument to it.
def minimum(numbers_list):
    lowest = min(numbers_list)
    return lowest

# Defining the maximum function to find the highest number in the list by passing the
# numbers_list as an argument to it.
def maximum(numbers_list):
    highest = max(numbers_list)
    return highest

# Defining the total function to find the total of the numbers in the list by passing the
# numbers_list as an argument to it.
def total(numbers_list):
    total = 0
    for num in numbers_list:
        total += num

    return total

# Defining the average function to find the average of the numbers in the list by passing the
# numbers_list as an argument to it.
def average(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    average = total / len(numbers_list)

    return average


def main():

    # Declaring a variable for the 20 numbers and initializing it with 20.
    series_of_numbers = 20

    # Creating an empty list to the store numbers from the user.
    numbers_list = []

    # Looping to accept the 20 numbers from the user.
    print("Please enter 20 series of numbers")
    for num in range(1, series_of_numbers + 1):
        # Asking the user for the number.
        print("Please enter #", num, ":", end="")
        numbers = int(input())
        numbers_list.append(numbers)
        
    # Creating a variable to the store the highest, lowest, total and average
    # of the numbers by calling the highest,lowest,total and average functions.
    lowest = minimum(numbers_list)

    highest = maximum(numbers_list)

    total_of_numbers = total(numbers_list)

    average_of_numbers = average(numbers_list)

    print()

    # Displaying the output to the user.
    print("The lowest of the numbers is ", lowest)
    print("The highest of the numbers is ", highest)
    print("The total of the numbers is", total_of_numbers)
    print("The average of the numbers is ", average_of_numbers)

# Calling the main function to start execution of the program.
main() 
