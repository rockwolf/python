#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

from os.path import isfile
import shutil
import os, sys
from modules.constant import *
from generic.modules.messagehandler import *
from database.databaseaccess import *


class ControllerMain():
    """ Contains the bussiness logic of the application. """

    def __init__(self):
        """ Initialize """
        self.loaded_inventory = []
        self.inventory_file = "data/inventory.md"

    # Methods
    ## General
    def run(self, add, update_id, delete_id, show_inventory, inventory_file):
        """
            Start the app.
        """
        self.inventory_file = inventory_file
        if show_inventory:
            self.loaded_inventory = self.load_inventory()
            self.print_inventory(self.loaded_inventory)
        if add:
            self.add_item()
        if update_id > 0:
            self.update_item(update_id)
        if delete_id > 0:
            self.delete_item

    def load_inventory(self):
        """
            Load current inventory.
        """
        try:
            dba = DatabaseAccess(self.inventory_file)
            result = []
            inventory = dba.get_inventory()
            current_key = ''
            to_replace = 0
            low = 0
            high = 0
            item_number = 0
            warning = Warning.NONE
            categories = dba.get_categories()
            grand_total = 0
            for key in categories:
                item = inventory[key]
                item_total = len(item)
                grand_total += item_total
                max_items_for_category = dba.get_category_max(key)
                warning = self.get_warning_message(
                    item_total, max_items_for_category)
                if key != current_key:
                    result.append(
                        [key, item_total, max_items_for_category, warning])
                    current_key = key
                for value in item:
                    item_number += 1
                    state = int(value[1])
                    if state == 0:
                        to_replace += 1
                        mark = '[!]'
                    else:
                        mark = '[ ]'
                    if state <= 3:
                        low += 1
                    high = 10 - low
                    result.append([
                        ' ' * (4 - len(str(item_number))),
                        item_number,
                        mark,
                        value[0],
                        value[2],
                        int(value[1]) * 10])
            result.append([
                grand_total,
                to_replace,
                low,
                high])
        except Exception as ex:
            print('Error in load_inventory:', ex)
        finally:
            dba = None
            return result

    def get_warning_message(self, item_total, max_items_for_category):
        """
            Returns the warning to display next to the header.
        """
        if item_total == max_items_for_category:
            warning = Warning.FULL
        elif item_total > max_items_for_category:
            warning = Warning.BURDENED
        elif item_total <= (max_items_for_category / 2):
            warning = Warning.HUNGRY
        else:
            warning = Warning.NONE
        return warning

    def print_inventory(self, loaded_inventory):
        """
            Print the inventory.
        """
        print('Inventory')
        print('---------')
        for index in range(0, len(loaded_inventory)):
            if index == len(loaded_inventory) - 1:
                # last line
                print(
                        'Total: {} | Replace: {} | -60%: {} + 60%: {}'.format(
                        loaded_inventory[-1][0],
                        loaded_inventory[-1][1],
                        loaded_inventory[-1][2],
                        loaded_inventory[-1][3]))
            else:
                if len(loaded_inventory[index]) == 4:
                    # category line
                    print('{} [{}/{}] {}'.format(
                                    loaded_inventory[index][0],
                                    loaded_inventory[index][1],
                                    loaded_inventory[index][2],
                                    loaded_inventory[index][3]))
                else:
                    # item line
                    print('  {}{}. {} {} ({}) [{}%]'.format(
                        loaded_inventory[index][0],
                        loaded_inventory[index][1],
                        loaded_inventory[index][2],
                        loaded_inventory[index][3],
                        loaded_inventory[index][4],
                        loaded_inventory[index][5]))

    def add_item(self):
        """
            Add new item to inventory.
        """
        try:
            msg = MessageHandler()
            dba = DatabaseAccess(self.inventory_file)
            if msg.confirmation(
                'Are you sure you want to add a new item to the inventory?'):
                if msg.confirmation('Add a new category?'):
                    # New category
                    print(dba.get_categories())
                    #TODO: input mask for category
                    category = msg.get_input('New category: ')
                    category_max = msg.get_input('Category max items [8]: ')
                else:
                    category = self.lookup_category()
                # New item
                name = msg.get_input('Name: ')
                description = msg.get_input('Description ')
                state = msg.get_input('State (0 - 10) [10]: ')
                comment = msg.get_input('Comment: ')

                if not is_digit(state):
                    state = 10
                else:
                    state = int(state)
                #print('test: cat {} } name {} | description {} | state {} | comment {}'.format(cat, name, description, state, comment))
        except Exception as ex:
            print('Error in add_item:', ex)
        finally:
            msg = None
            dba = None

    def update_item(self):
        """
            Update an item in the inventory.
        """
        try:
            msg = MessageHandler()
            dba = DatabaseAccess(self.inventory_file)
            category = ''
            if msg.confirmation('add a new item to the inventory'):
                category = self.lookup_category()
                name = msg.get_input('Name: ')
                description = msg.get_input('Description: ')
                state = msg.get_input('State (0 - 10) [10]: ')
                comment = msg.get_input('Comment: ')
                if int(state) in range(11):
                    state = int(state)
                else:
                    raise Exception(
                        'Wrong state value, could not convert to int.')
                #input retrieved, now add it to the db
                dba.save_item(name, description, state, comment)
            dba = None
            msg = None
        except Exception as ex:
            print('Error in update_item:', ex)

    def delete_item(self, item_number):
        """
            If item_number exists: delete values.
        """
        try:
            msg = MessageHandler()
            dba = DatabaseAccess(self.inventory_file)
            record_id = msg.get_input('Id: ')
            if int(record_id) in range(11):
                record_id = int(record_id)
            else:
                raise Exception('Wrong state value, could not convert to int.')
                #input retrieved, now add it to the db
                if msg.confirmation('delete this item from the inventory'):
                    dba.delete_item(record_id)
            dba = None
            msg = None
        except Exception as ex:
            print('Error in delete_item:', ex)

    def lookup_category(self):
        """
            Enter category,
            but it has to exist.
        """
        try:
            msg = MessageHandler()
            dba = DatabaseAccess(self.inventory_file)
            result = ''
            categories = dba.get_categories()
            while result not in categories:
                self.print_categories()
                result = msg.get_input('Category: ')
        except Exception as ex:
            print('Error in lookup_category:', ex)
        finally:
            msg = None
            dba = None
            return result

    def print_categories(self):
        """
            Print the available categories.
        """
        # TODO: fancy this up
        dba = DatabaseAccess(self.inventory_file)
        print(dba.get_categories)
        dba = None

    def backup(self):
        """
            Make a backup of the output file.
        """
        # TODO: create export that will print a summary
        # (of e.g. the profile) to txt.
        # remove old backup
        if isfile(self.config.backupfile):
            try:
                os.remove(self.config.backupfile)
                print(self.config.backupfile + ' removed.')
            #except IOError as strerror:
            except Exception as ex:
                print("Error: ", ex)
        # copy current to .bak
        if isfile(self.config.exportfile) and not isfile(self.config.backupfile):
            try:
                shutil.copy(self.config.exportfile, self.config.backupfile)
                print(self.config.backupfile + ' created.')
            except Exception as ex:
                print('Error: application fucked up while creating backup: ', ex)
        else:
            print('Error: backup file already exists.')
