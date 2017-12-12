# Scripts: shipping_charges
# Description: This program that asks the user to enter the weight of a
#              package and then displays the shipping charges.

# Programmer: William Kpabitey Kwabla
# Date: 26.05.16


# Defining the Rate per pound as Global constants.
RATE1 = 3.80
RATE2 = 3.70
RATE3 = 2.20
RATE4 = 1.10


# Defining the main function.
def main():

    # Displaying to the user what the program does.
    print("This program that asks the user to enter the weight of a")
    print("package and then displays the shipping charges.")
    print("****************************************************")

    # Asking user to enter the weight of the package.
    weight_of_package = float(input("Please Enter the weight of package: "))

    # Displaying the shipping charges for the weight of package.
    if weight_of_package >= 10:
        print("The shipping charge for your package is $",RATE1)

    elif weight_of_package >= 6:
        print("The shipping charge for your package is $",RATE2)

    elif weight_of_package >= 2:
        print("The shipping charge for your package is $",RATE3)

    else:
        print("The shipping charge for your package is $",RATE4)


# Calling the main function.
main()
    
