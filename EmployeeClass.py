# Module: EmployeeClass.py
# Description: This module creates an Employee Class with data attributes
#              and methods acting on the data.
# Programmer: William Kpabitey Kwabla.
# Date: 01.03.17



class Employee:
    """Creating the Employee class with data attributes and methods.
"""

    # Defining the __init__ method initializes the attributes.
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    # Defining the set_name method sets the name attributes.
    def set_name(self, name):
        self.__name = name

    # Defining the set_id_number method sets the id_number attributes.
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Defining the set_department method sets the department attributes.
    def set_department(self, department):
        self.__department = department

    # Defining the set_job_title method sets the job_title attributes.
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # Defining the get_name method returns the name of the employee.
    def get_name(self):
        return self.__name

    # Defining the get_id_number method returns the id_number of the employee.
    def get_id_number(self):
        return self.__id_number

    # Defining the get_department method returns the department of the employee.
    def get_department(self):
        return self.__department

    # Defining the get_job_title method returns the job_title of the employee.
    def get_job_title(self):
        return self.__job_title
    
        

    
