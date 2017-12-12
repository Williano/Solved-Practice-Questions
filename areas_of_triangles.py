# Script : areas_of_triangles
# Description : This program asks the user for the length and width
#               of two rectangles and then tell the user which rectangle
#               has the greater area, or if the areas are the same using the formula
#               Area = Length * Breadth

# Programmer : William Kpabitey Kwabla
# Date : 19.05.16


# Defines the main function
def main():
    print("This program asks the user for the length and width")
    print("of two rectangles and then tell the user which rectangle")
    print("has the greater area, or if the areas are the same using the formula")
    print("Area = Length * Breadth")
    print()

    # Asks User for length and width of both rectangles and assign them
    # to length and width variables.
    Length1 = float(input("Please Enter the length for rectangle 1: "))
    Width1  = float(input("Please Enter the  width for rectangle 1: "))
    print()
    Length2 = float(input("Please Enter the length for rectangle2 : "))
    Width2 = float(input("Please Enter the  Width for rectangle 2: "))
    print()

    # Calculates the Area of rectangle 1
    Area1 = Length1 * Width1
    print("The Area of Rectangle 1 is", Area1)
    print()

    # Calculates the Area of rectangle 2
    Area2 = Length2 * Width2
    print("The Area of Rectangle 2 is", Area2)
    print()

    # Loop to determine which rectangle is bigger or if they are the same in this manner.
    if Area1 == Area2:
        print("The Areas are the same")
    elif Area2 > Area1:
        print("Rectangle 2 has the greater Area")
    else:
        print("Rectangle 1 has the greater Area")

# Calls the main function
main()
    
