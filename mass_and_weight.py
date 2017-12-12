# Scripts : mass_and_weight
# Description : This program asks the user to enter an object’s mass,
#               and then calculates its weight using
#               weight = mass * acceleration due to gravity.
#               If the object weighs more than 1,000 newtons,
#               it displays a message indicating that it is too heavy.
#               If the object weighs less than 10 newtons,
#               it display a message indicating that it is too light.

# Programmer : William Kpabitey Kwabla
# Date : 19.05.16


# Declaring gravity,maximum and minimum weight as Constants and assigning values to them.
ACCELERATION_DUE_TO_GRAVITY = 9.8
MAXIMUM_WEIGHT = 1000
MINIMUM_WEIGHT = 10


# Defining the main function
def main():

    print("This program asks the user to enter an object’s mass,")
    print("and then calculates its weight using")
    print("weight = mass * acceleration due to gravity.")
    print("If the object weighs more than 1,000 newtons,")
    print("it displays a message indicating that it is too heavy.")
    print("If the object weighs less than 10 newtons,")
    print("it display a message indicating that it is too light.")
    print()

    # Asking User to enter object's mass and assigning to the Mass variable.
    mass = float(input("Please Enter the Mass of the Object: "))
    print()

    # Calculating Objects weights using weight = mass * acceleration due to gravity.
    weight = mass * ACCELERATION_DUE_TO_GRAVITY
    print("The weight of the object is", weight,"Newton")
    print()


    # Determining whether the object is heavier or light in this manner.
    if weight > MAXIMUM_WEIGHT or weight < MINIMUM_WEIGHT:
        print("Object is too heavy ")

    else:
        print("Object is too light ")

# Calling the main function.
main()

    
