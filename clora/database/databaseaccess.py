#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
"""

from modules_generic.function import *
from modules_generic.messagehandler import *
from modules.constant import *
from modules.function import *

class DatabaseAccess():
    """
        Connecting to the database.
    """ 

    def __init__(self):
        """
            Initialize object.
        """
        try:
            self.inventory_file = "data/inventory_example.md"
            self.inventory = []
            self.categories = self.get_categories()

            self.read_inventory()
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
   
    def get_categories(self):
        """
            Get the categories with their max value.
        """
        result = []
        try:
            with open(self.inventory_file) as var_file:
                for line in var_file: 
                    line = line.rstrip()
                    if line == '# categories;max':
                        processing_categories = True
                    elif line[0] == '#':
                        processing_categories = False
                        break; #optimization
                    else:
                        if processing_categories:
                            result.append(line.split(';')[0])
        except Exception as ex:
            print(Error.GET_CATEGORIES, ex)
        finally:
            return result

    def get_inventory(self):
        """
            Returns the inventory as a dictionary.
        """
        return self.inventory

    def get_lines(self):
        """
          Returns the lines from a file.
        """
        result = []
        line_number = 0
        with open(self.inventory_file) as var_file:
            for line in var_file: 
                line_number += 1
                result.append(line.rstrip())
        return result

    def read_inventory(self):
        """
          Reads the inventory
          and save it in a global var.
        """
        try:
            line_number = 0
            current_key = None
            with open('data/inventory_example.md') as var_file:
                for line in var_file: 
                    line = line.rstrip()
                    line_number += 1
                    if line == '# categories;max':
                        process_categories = True
                    elif (line[0] == '#') and (line[2:] in self.categories):
                        current_key = line[2:]
                        process_categories = False
                    elif (line[0] == '#') and (line[2:] not in self.categories):
                        #TODO: if verbose:
                        print('::: Warning: category', line[2:], 'not found!')
                    else:
                        if process_categories:
                            cat = line.split(';')
                            self.categories.append((cat[0], cat[1]))
                        else:
                            self.inventory.append({current_key:line.split(';')})
        except Exception as ex:
            print('Error in read_inventory:', ex)
