# Script: CelsiusToFahrenheitTable
# Description: This program displays a table of the Celsius temperatures 0 through 20 and
#              their Fahrenheit equivalents using the formula
#              F = (9/5)C + 32

# Programmer: William Kpabitey Kwabla
# Date: 18.07.16


# Defining the main function.
def main():

    # Printing the table headings
    print()
    print("Celsius\tFahrenheit")
    print('--------------------')

    # Printing the table of the Celsius temperatures 0 through 20 and
    # their Fahrenheit equivalents
    for celsius in range(21):
        fahrenheit = 9 * celsius/5 + 32
        print(celsius, '\t', fahrenheit)

# Calling main function to execute the program.
main()


    
