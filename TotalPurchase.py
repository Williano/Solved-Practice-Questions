# Script: TotalPurchase.py
# Description: This program ask a user for the price of five items purchased from a store and
#              displays the subtotal of the sale, the amount of sales tax and the total.
#              Assuming the sales tax is 7 percent.
# Programmer: William Kpabitey Kwabla.
# Date: 07.03.17


# Defining the main function
def main():

    # Declaring a total varible and initializing it to zero.
    sub_total = 0

    # Asking user for the number of items bought.
    num_of_items = int(input("Please input the number of items bought: "))


    # Looping through the number of items and asking the user for price for each item.
    for items in range(1, num_of_items + 1):

        # Asking user for price of item.
        print("Please input price for item #",items,": ", end='')
        price = float(input())

        # Adding the price to the total.
        sub_total += price

    # Calculating the amount of sales tax assuming the sales tax is 7 percent.
    # That is 7% = 0.07
    tax = sub_total * 0.07

    # Calculating the total by subtracting the tax from the total.
    total_sales = sub_total + tax

    # Displaying the subtotal, sales tax and total sales to the user.
    print("The subtotal is: ", sub_total)
    print("The sales tax is: ", tax)
    print("The total sales is:", total_sales)

# Calling the main function to start execution of the proram.
main() 

        
