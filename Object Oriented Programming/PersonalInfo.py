# Module: PersonalInfo.py
# Description: This module creates a Personal Information Class with data
#              attributes and methods acting on the data.
# Programmer: William Kpabitey Kwabla.
# Date: 02.03.17



""" Creating the Personal Info class with data attributes and methods.
"""
class PersonalInfo:
    
    # Defining the __init__ method to initializes the data attributes of objects
    # created from this class.
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number


   """ Creating the mutators to access the data attributes of the class and make
        any modifications.
"""

   # Defining the set_name method to set the name attribute of the objects created from this class.
    def set_name(self, name):
        self.__name = name

    # Defining the set_address method to set the address attribute of the objects created from this class.
    def set_age(self, address):
        self.__address = address

    # Defining the set_age method to set the age attribute of the objects created from this class.
    def set_address(self, age):
        self.__age = age

    # Defining the set_phone_number method to set the phone number attribute of the objects created from this class.
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


    """ Creating the accessors to access the data attributes of the class
"""
    # Defining the get_name method to get the name from the name field for the object.
    def get_name(self):
        return self.__name

    # Defining the get_address method to get the address from the address field for the object.
    def get_address(self):
        return self.__address

    # Defining the get_age method to get the age from the age field for the object.
    def get_age(self):
        return self.__age

    # Defining the get_phone_number method to get the phone number from the phone number field for the object.
    def get_phone_number(self):
        return self.__phone_number
    
    
