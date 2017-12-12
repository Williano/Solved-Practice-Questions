# Script: TipTaxTotal.py
# Description: This program calculates the total number of meals purchased at a
#              restaurant. The program asks for the charge and then calculate
#              the amount of a 18 percent tip and 7 percent sales tax and display
#              these amount and the total.
# Programmer: William Kpabitey Kwabla.
# Date: 08.03.17


# Defining the main function
def main():

    # Declaring and initializing the total_cost to hold the total cost of the food.
    total_cost = 0

    # Asking user for charge of food.
    food_charge = float(input("Please input charge of food: "))

    # Calculating the 18 percent tip.
    tip = food_charge * 0.18

    # Calculating the 7 percent tax.
    tax = food_charge * 0.07

    # Calculating the total for the meal.
    total_cost =  food_charge + tip + tax

    # Displaying the outputs to the user.
    print("The food charge is: ", food_charge)
    print("The tip for the food is: ", tip)
    print("The tax for the food is: ", tax)
    print("The total cost of the food is: ", total_cost)

# Calling the main function to start execution of the program.
main() 
