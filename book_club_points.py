# Script: book_club_points
# Description: Serendipity Booksellers has a book club that awards points to its customers based on the
#              number of books purchased each month.
#              This program asks the user to enter the number of books that he or she has purchased
#              this month and displays the number of points awarded.

# Programmer: William Kpabitey Kwabla
# Date: 26.05.16


# Declaring points to earn as Global constants.
POINT1 = 60
POINT2 = 30
POINT3 = 15
POINT4 = 5
POINT5 = 0

# Defining the main functon.
def main():

    # Displaying to user what the program does.
    print("Serendipity Booksellers has a book club that awards points to its customers based on the")
    print("number of books purchased each month.")
    print("This program asks the user to enter the number of books that he or she has purchased")
    print("this month and displays the number of points awarded.")
    print()

    # Asking user to enter number of books purchased this month.
    number_of_books = int(input("Please Enter the number of books purchased this month: "))

    # Displaying the number of points earned for books purchased this month.
    if number_of_books >= 4:
        print("You have earned",POINT1,"points this month.")
    elif number_of_books == 3:
        print("You have earned",POINT2,"points this month.")
    elif number_of_books == 2:
        print("You have earned",POINT3,"points this month.")
    elif number_of_books == 1:
        print("You have earned",POINT4,"points this month.")
    else:
        print("You have earned",POINT5,"points this month.")


# Calling the main function to execute program.
main()
