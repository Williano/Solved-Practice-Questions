# Module: PetClass.py
# Description: This Module creates a Pet Class with data attributes
#              and methods.
# Programmer: William Kpabitey Kwabla
# Date: 28.02.17


class Pet:
    """ Creating the Pet class
"""
    # Defining the __init__ method initializes the attributes.
    def __init__(self, name, animal_type, age):
        self.__pet_name = name
        self.__animal_type = animal_type
        self.__pet_age = age


    # Defining the set_name method sets the name attribute.
    def set_name(self, name):
        self.__pet_name = name

    # Defining the set_animal_type method sets the animal type attribute.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Defining the set_age method sets the pet's age attribute.
    def set_age(self, age):
        self.__pet_age = age

    # Defining the get_name method returns the name attribute.
    def get_name(self):
        return self.__pet_name

    # Defining the get_animal_type method returns the animal type attribute.
    def get_animal_type(self):
        return self.__animal_type

    # Defining the get_age method returns the age attribute.
    def get_age(self):
        return self.__pet_age
    
