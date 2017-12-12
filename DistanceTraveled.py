# Script: DistanceTraveled.py
# Description: This program asks the user for the speed of a vehicle (in miles per hour)
#              and the number of hours it has traveled. It then use a loop to display the distance
#              the vehicle has traveled for each hour of that time period using the formula:
#              distance = speed * time

# Programmer:  William Kpabitey Kwabla
# Date: 18.07.16


# Defining the main function.
def main():

    # Getting the speed of the vehicle from the user.
    speed = int(input("Please Enter the speed of the vehicle(in miles per hour): "))
    print()
    # Getting the number of hours the vehicle has traveled.
    number_of_hours = int(input("Please Enter the number of hours the vehicle has traveled: "))
    print()

    # Printing the table headings.
    print()
    print("Hour\tDistance Traveled")
    print("------------------------")

    # Printing the distance the vehicle has traveled for each hour of that time period.
    for hour in range(1, number_of_hours + 1):
        distance = speed * hour
        print(hour, '\t',distance)

# Calling the main function to execute the program.
main()

