# Script: Pets.py
# Description: This program creates a python instance(object) from
#              the Pet class, and ask user for his/her pets name,age,
#              and animal type and display the information on the screen
#              the user.
# Programmer: William Kpabitey Kwabla
# Date: 28.02.17

# Importing the Pet Class
import PetClass


# Defining the main fucntion.
def main():

    # Asking user for his/her pets detaila.
    name_of_pet = input("Please enter your pet's name: ")

    animal = input("Please Enter the type of animal your + pet is(Dog, Cat or Bird): ")

    age_of_pet = int(input("Please Enter your pet's age: "))
    print()


    # Creting an object from the Pet class and assinging the user input as
    # parameter variables.
    my_pet = PetClass.Pet(name_of_pet,animal,age_of_pet)


    # Displaying the details about the pet to the screen.
    print("The name of your pet is: ", my_pet.get_name())
    print("The type of animal is: ", my_pet.get_animal_type())
    print("The age of your pet is: ", my_pet.get_age())

# Calling the main function to start execution the program.
main() 
    
    
