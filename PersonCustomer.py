# Module: PersonCustomer.py
# Description: This program creates a Person Class and Customer class which inherits
#              attributes from the Person Class.
# Programmer: William Kpabitey Kwabla.
# Date: 12.03.17



""" Defining the Person Class """
class Person():

    # Defining the __init__ method to initialize the fields of all objects created
    # from this class.
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    """ Defining the accessor methods to access the data stored in the fields of the class """
    # Defining the get_name method to return the data stored in the name field.
    def get_name(self):
        return self.__name

    # Defining the get_address method to return the data stored in the address field.
    def get_address(self):
        return self.__address

    # Defining the get_telephone method to return the data stored in the telephone field.
    def get_telephone(self):
        return self.__telephone

""" Creating the Customer Class which will inherit the attributes of the Person Class """
class Customer(Person):

    # Defining the __init__ method to initialize the fields of all objects created
    # from this class.
    def __init__(self, name, address, telephone, customer_number):

        # Calling the Person Class to initialize the fields of the Customer Class.
        Person.__init__(self, name, address, telephone)

        # Initializing the customer_number attribute.
        self.__customer_number = customer_number

        # Initializing the mailing_list attribute to True.
        self.__mailing_list = True

    """ Defining the accessor methods to access the data stored in the fileds of the class """
    # Defining the get_customer_number to return the data stored in the telephone customer number field.
    def get_customer_number():
        return self.__customer_number

    # Defining the get_mailing_list method to return the data stored in the mailing list field.
    def get_mailing_list():
        return self.__mailing_list 
    
    
