# Module : kilo_to_mile_converter
# Description : This program program asks
#               the user to enter a distance in kilometers,
#               and then converts that distance to miles with this formula
#               Miles = Kilometers * 0.6214

# Programmer : William Kpabitey Kwabla
# Date : 05/04/16


# Defining the main function
def main():
    # Calling the intro function
    intro()

    # Asking user for distance in kilometers
    kilometers = float(input("Please Enter Distance in Kilometers: "))
    print()

    # Calling the kilometer to Mile function and assigning user input as argument.
    kilo_to_mile(kilometers)


# Defining th intro function
def intro():
    print("This program program asks")
    print("the user to enter a distance in kilometers,")
    print("and then converts that distance to miles with this formula")
    print("Miles = Kilometers * 0.6214")
    print()
    

# Defining the kilometer to Mile function
def kilo_to_mile(kilo):

    # Converting distance from Kilometers to Miles
    miles = kilo * 0.6214

    # Displaying the distance in miles
    print("The distance is",miles,"miles" )

# Calling the main function
main()
    
