# Script: magic_dates
# Description: This program ask the user to enter a month (in numeric form), a day,
#              and a two digit year. The program should then determine whether the
#              month times the day equals the year. If so, it should display a message
#              saying the date is magic. Otherwise, it should display
#              a message saying the date is not magic.

# Programmer: William Kpabitey Kwabla
# Date: 24.05.16


# Defining the main function.
def main():

    # Telling the user what the program does.
    print("This program ask the user to enter a month (in numeric form), a day,")
    print("and a two digit year. The program should then determine whether the")
    print("month times the day equals the year. If so, it should display a message")
    print("saying the date is magic. Otherwise, it should display")
    print("a message saying the date is not magic.")
    print()


    # Asking for user to enter a month and assign to month variable.
    month = int(input("Please Enter a month in numeric form: "))

    # Asking for user to enter a day and assign to day variable.
    day = int(input("Please Enter a day: "))

    # Asking for user to enter a two digit year and assign to year variable.
    year = int(input("Please Enter  a two digit year: "))


    # Determining whether month times day equals the year.
    if month * day == year:
        print("The Date is Magic.")

    else:
        print("The Date is not Magic.")

# Calling the main function.
main()
    
    
