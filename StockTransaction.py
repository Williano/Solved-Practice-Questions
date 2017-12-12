# Script: StockTransaction.py
# Description: This program display the stock purchased and sold by Joe. This
#              program displays amount of money, commission he paid and got when he
#              bought the stock and sold the stock respectively.
# Programmer: William Kpabitey Kwabla.
# Date: 11.03.17


# Defining the main function.
def main():

    """ Calculating the stock purchased """

    # Calculating the total amount of money paid for the stock purchased.
    total_amount = 2000 * 40.00

    # Calculating the amount of commission joe paid his broker
    # when he bought the stock by using the 3 percent he paid.
    commission = total_amount * 0.03

    # Calculting the total amount left after paying his broker.
    amount_total = total_amount - commission


    """ Calculating the stock sold """

    # Calculating the total amount of money paid for the stock sold.
    total_sold = 2000 * 42.75

    # Calculating the amount of commission Joe paid his broker
    # when he sold the stcok by using the 3 percent he paid.
    commission_sold = total_sold * 0.03

    # Calculting the total amount left after paying his broker.
    amount_total_sold = total_sold - commission_sold
    
    
    
