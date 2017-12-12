# Script: SalesTax.py
# Description: This program ask a user for the amount of a purchase and then compute
#              state and the county sales tax assuming the sales tax is 5 percent and
#              the county sales tax is 2.5 percent. The program then displays amount of
#              the purchase, the state sales tax, the county sales tax, the total sales
#              tax and the total of the sale.
# Programmer: William Kpabitey Kwabla.
# Date: 07.03.17


# Defining the main function of the program.
def main():

    # Asking user for the amount of purchase.
    amount_of_purchase = float(input("Please enter the amount of purchase $: "))

    # Calculating the state sales tax assuming the sales tax is 5 percent.
    state_tax = amount_of_purchase * 0.05

    # Calculating the county sales tax assuming the county sales is 2.5 percent.
    county_tax = amount_of_purchase * 0.25

    # Calculating the total sales tax.
    total_sales_tax = state_tax + county_tax
    
    # Calculating the total of the sale by adding the amount of purchase and the total sales.
    total_sales = total_sales_tax + amount_of_purchase

    # Displaying the amount of purchase, state tax, conunty tax, total sales tax and the total
    # sales.
    print("The amount of purchase is: ", amount_of_purchase)
    print("The state tax is: ", state_tax)
    print("The county tax is: ", county_tax)
    print("The total sales tax is: ",total_sales_tax)
    print("The total of the sale is: ", total_sales)

# Calling the main function to start execution of the program.
main() 
