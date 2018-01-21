# Module: Employee.py
# Description: This module creates an Employee and Worker Classes that keeps
#              data attributes of the Employee and Worker. It demonstrates
#              inheritance of the python language.
# Programmer: William Kpabitey Kwabla.
# Date: 05.03.17


""" Creating the Employee Class to keep the data attributes and methods of the class
"""
class Employee:

    # Defining the __init__ method to initialize data fields of objects created from
    # this class.
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number


    """ Defining the mutators to access the data attributes of the Employee Class
"""
    # Definig the set_employee_name method to initialize the employee_name data attributes of
    # objects created from this class.
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    # Definig the set_employee_number method to initialize the employee_number data attributes of
    # objects created from this class.
    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number


    """ Defining the the accessors to return the data attributes stored in the Employee class
"""
    # Definig the get_employee_number method to return the employee_name to objects created from this class.
    def get_employee_name(self):
        self.__employee_name = employee_name

    # Definig the get_employee_number method to return the employee_number to objects created from this class.
    def get_employee_number(self):
        self.__employee_number = employee_number



""" Creating the ProductionWorker Class to keep the data attributes and methods of the class
    This class inherits the employee data attributes. """
class ProductionWorker(Employee):

    # Defining the __init__ method to initialize data fields of objects created from
    # this class.
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):

        # Inheriting the attributes of the Employee Class by calling the __init_ method of the
        # Employee class
        Employee.__init__(self, employee_name, employee_number)

        # Initializing the shift_number and hourly_pay_rate of the ProductionWorker Class.
        self.__shift_number = shift_number

        self.__hourly_pay_rate = hourly_pay_rate



""" Defining the mutators to access the data attributes of the Employee Class
"""

    # Definig the set_shift_number method to initialize the shift_number data attributes of
    # objects created from this class.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    # Definig the set_hourly_pay_rate method to initialize the hourly_pay_rate data attributes of
    # objects created from this class.
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate



""" Defining the the accessors to return the data attributes stored in the ProductionWorker class
"""

    # Definig the get_shift_number method to return the shift_number data attributes of
    # objects created from this class.
    def get_shift_number(self):
        self.__shift_number = shift_number

    # Definig the get_hourly_pay_rate method to return the hourly_pay_rate data attributes of
    # objects created from this class.
    def get_hourly_pay_rate(self):
        self.__hourly_pay_rate = hourly_pay_rate
        

    
            
        
    
    
    
