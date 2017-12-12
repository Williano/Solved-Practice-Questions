# Script: ProductionWorker.py
# Description: This program creates an object from the ProductionWorker class in the
#              Employee Class module. It is also a demonstration of python inheritance.
# Programmer: William Kpabitey Kwabla.
# Date: 05.03.17


# Importing the Employee class to allow access to it's data attributes and methods.
import Employee


# Defining the main function to begin the program.
def main():
    # Asking user for his information.
    name = input("Please enter your name: ")

    number = input("Please enter your number: ")

    shift = int(input("Please enter your shift, 1 for day and 2 for night: "))

    pay_rate = int(input("Please enter your hourly pay rate: "))

    # Creating a worker object from the ProductionWorker class in the Employee Module.
    worker = Employee.ProductionWorker(name, number, shift, pay_rate)

    # Displaying Employee details
    print("Employee Details")
    print("----------------")
    print("Your name is: ", worker.get_employee_name())
    print("Your number is: ", worker.get_employee_number())
    print("Your shift number is: ",worker.get_shift_number())
    print("Your pay rate is: ", worker.get_hourly_pay_rate())


# Calling the main function to start execution of the program.
main()
