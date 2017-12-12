# Script: software_sales
# Description: A software company sells a package that retails for $99.
#              This program asks the user to enter the number of packages purchased. The program
#              should then display the amount of the discount (if any) and the total amount of the
#              purchase after the discount.

# Programmer: William Kpabitey Kwabla
# Date: 26.06.16


# Declaring discount percentage as Global constants.
DISCOUNT1 = 50
DISCOUNT2 = 40
DISCOUNT3 = 30
DISCOUNT4 = 20

# Defining the main function.
def main():

    # Displaying what the program does to the user.
    print("A software company sells a package that retails for $99.")
    print("This program asks the user to enter the number of packages purchased. The program")
    print("should then display the amount of the discount (if any) and the total amount of the")
    print("purchase after the discount.")
    print("")

    # Asking user for the number of packages purchased.
    number_of_packages = int(input("Please Enter the number of packages purchased: "))
    print("**************************************************************************")



    # Displaying the discount and the total amount of the purcahse after the discount.
    if number_of_packages >= 100:
        total_amount = (DISCOUNT1/100) * 99
        print("The total amount of discount is",DISCOUNT1,"%.")
        print("The total amount of purchase after discount is $",format(total_amount,".1f"))

    elif number_of_packages >= 50:
        total_amount = (DISCOUNT2/100) * 99
        print("The total amount of discount is",DISCOUNT2,"%.")
        print("The total amount of purchase after discount is $",format(total_amount,".1f"))

    elif number_of_packages >= 20:
        total_amount = (DISCOUNT3/100) * 99
        print("The total amount of discount is",DISCOUNT3,"%.")
        print("The total amount of purchase after discount is $",format(total_amount,".1f"))

    else:
        total_amount = (DISCOUNT4/100) * 99
        print("The total amount of discount is",DISCOUNT4,"%.")
        print("The total amount of purchase after discount is $",format(total_amount,".1f"))
        
        


# Calling the main function to execute program.
main()
