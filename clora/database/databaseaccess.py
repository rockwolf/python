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

    def __init__(self, inventory_file):
        """
            Initialize object.
        """
        try:
            if inventory_file == "":
                self.inventory_file = "data/inventory_example.md"
            else:
                self.inventory_file = inventory_file
            self.inventory = {}
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
            
    def get_category_max(self, category):
        """
            Returns the max value for the given category.
        """
        result = -1
        try:
            for item in self.categories:
                if item[0] == category:
                    result = item[1]
                    break;
        except Exception as ex:
            print('Error in get_category_max:', ex)
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
            current_key = ''
            previous_key = ''
            with open(self.inventory_file) as var_file:
                for line in var_file: 
                    line = line.rstrip()
                    line_number += 1
                    if line == '# categories;max':
                        process_categories = True
                    elif (line[0] == '#') and (line[2:] in self.categories):
                        previous_key = current_key
                        current_key = line[2:]
                        process_categories = False
                    elif (line[0] == '#') and (line[2:] not in self.categories):
                        previous_key = current_key
                        current_key = line[2:]
                        #TODO: if verbose:
                        print('::: Warning: category', line[2:], 'not found!')
                        process_categories = False
                    else:
                        if process_categories:
                            cat = line.split(';')
                            self.categories.append((cat[0], int(cat[1])))
                        else:
                            print('test --> previous {} | current {}'.format(previous_key, current_key))
                            if self.inventory == {} or previous_key != current_key:
                                self.inventory[current_key] = []
                            self.inventory[current_key].append(line.split(';'))
        except Exception as ex:
            print('Error in read_inventory:', ex)
