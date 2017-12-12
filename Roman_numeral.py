# Script : Roman_numeral.py
# Description : This program ask user to enter a number within the
#               range of 1 through 10 and displays the Roman Numeral
#               version of that number using 1=I, 2=II, 3=III, 4=IV
#               5=V, 6=VI, 7=VII, 8=VIII, 9=IX, 10=X.

# Programmer : William Kpabitey Kwabla
# Date : 07.05.16

# Defining numbers 1 to 10 as constants
NUMBER1 = 1
NUMBER2 = 2
NUMBER3 = 3
NUMBER4 = 4
NUMBER5 = 5
NUMBER6 = 6
NUMBER7 = 7
NUMBER8 = 8
NUMBER9 = 9
NUMBER10 = 10

# Defining the main function
def main():

    print(" This program ask user to enter a number within the")
    print(" range of 1 through 10 and displays the Roman Numeral")
    print(" version of that number using 1=I, 2=II, 3=III, 4=IV")
    print(" 5=V, 6=VI, 7=VII, 8=VIII, 9=IX, 10=X.")
    print("*******************************************************")
    print()

    # Asking user to enter a number within the range of 1 through 10.
    number = int(input(" Please enter a number within the range 1 through 10: "))

    # Checking and displaying Roman Numeral version of user input.
    if number == NUMBER1:
        print("It's Roman Numeral version is I")

    elif number == NUMBER2:
        print("It's Roman Numeral version is II")

    elif number == NUMBER3:
        print("It's Roman Numeral version is III")

    elif number == NUMBER4:
        print("It's Roman Numeral version is IV")

    elif number == NUMBER5:
        print("It's Roman Numeral version is V")

    elif number == NUMBER6:
        print("It's Roman Numeral version is VI")

    elif number == NUMBER7:
        print("It's Roman Numeral version is VII")

    elif number == NUMBER8:
        print("It's Roman Numeral version is VIII")

    elif number == NUMBER9:
        print("It's Roman Numeral version is IX")

    elif number == NUMBER10:
        print("It's Roman Numeral version is X")

    # If user input is outside of range should display out of range.
    else:
        print("The number is outside the range of 1 through 10")
        

# Calling the main function
main()
