# Module: RetailItem.py
# Description: This module creates a Retail Item class and holds data about the
#              items in a retail store and methods that acts on the data.
# Programmer: William Kpabitey Kwabla
# Date: 02.03.17



""" Creating the Retail Item Class with the data attributes and methods
"""
class RetailItem:

    # Defining the __init__ method to initialize the date attributes of the objects
    # created from this class.
    def __init__(self, item_description, units_in_inventory, price):
        self.__item_description = item_description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    """ Creating the accessors to the access the data attributes of the class
"""

    # Defining the get_item_description method to get the item_description
    # for the objects created from this class.
    def get_item_description(self, item_description):
        self.__item_description = item_description

    # Defining the get_units_in_inventory method to get the units_in_inventory
    # for the objects created from this class.
    def get_units(self, units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    # Defining the get_price method to get the items price
    # for the objects created from this class.
    def get_price(self, price):
        self.__price = price

        
