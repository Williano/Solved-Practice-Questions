# Script : how_much_insurance.py
# Description : This program asks the user to enter
#               the replacement cost of a building and then displays
#               the minimum amount of insurance
#               he or she should buy for the property at 80 percent of the cost.

# Programmer : William Kpabitey Kwabla
# Date : 07/04/16


# Defining the main function and calling the other functions
def main():
    # Calling the intro function
    intro()

    # Asking the User for the replacement cost of the building
    replacement_cost = float(input(" Please Enter Replacement Cost of your Building: $"))
    print()

    # Calling the minimum amount of insurance function
    mini_amnt_of_insurance(replacement_cost)

# Defining the intro function
def intro():
    print(" This program asks the user to enter ")
    print(" the replacement cost of a building and then displays ")
    print(" the minimum amount of insurance ")
    print(" he or she should buy for the property ")
    print(" at 80 percent of the cost. ")
    print()

def mini_amnt_of_insurance(replacement_cost):
    # Calculating the minimum amount of insurance
    insurance = 0.8 * replacement_cost

    # Displaying the insurance
    print(" The minimum amount of insurance you should pay is: $", \
          format(insurance,",.2f"),\
          sep = '')
    print()
    

#Calling the main function
main()
