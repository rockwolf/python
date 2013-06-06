#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

from os.path import isfile
import shutil
import os, sys
from modules_generic.messagehandler import *
from database.databaseaccess import *

class ControllerMain():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self):
        """ Initialize """
        self.loaded_inventory = []

    # Methods
    ## General
    def run(self, add, update_id, delete_id, show_inventory):
        """
            Start the app.
        """
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
            dba = DatabaseAccess()
            print('Inventory')
            print('---------')
            result = []
            inventory = dba.get_inventory()
            current_key = ''
            to_replace = 0
            low = 0
            high = 0
            id = 0
            for item in inventory:
                id += 1
                for key, value in item.items():
                    if key != current_key:
                        current_key = key
                        result.append([key, len(value), dba.get_category_max(key)])
                        #print('-'*len(key))
                    state = int(value[1])
                    if state == 0:
                        to_replace += 1
                        mark = '[!]'
                    else:
                        mark = '[ ]'
                    if state <= 3:
                        low +=1
                    high = 10 - low
                    result.append([
                        ' '*(4-len(str(id)))
                        , id
                        , mark
                        , value[0]
                        , value[2]
                        , int(value[1])*10])
            result.append([
                len(inventory)
                , to_replace
                , low
                , high])
        except Exception as ex:
            print('Error in show_inventory:', ex)
        finally:
            dba = None
            return result
            
    def print_inventory(self, loaded_inventory):
        """
            Print the inventory.
        """
        # first line
        print('{} [{}/{}]'.format(
                           loaded_inventory[0][0]
                           , loaded_inventory[0][1]
                           , loaded_inventory[0][2]))
        # sencond line
        print('  {}{}. {} {} ({}) [{}%]'.format(
            loaded_inventory[1][0]
            , loaded_inventory[1][1]
            , loaded_inventory[1][2]
            , loaded_inventory[1][3]
            , loaded_inventory[1][4]
            , loaded_inventory[1][5]))
        # third line
        print(
                'Total: {} | Replace: {} | -60%: {} + 60%: {}'.format(
                loaded_inventory[2][0]
                , loaded_inventory[2][1]
                , loaded_inventory[2][2]
                , loaded_inventory[2][3]))

    def add_item(self):
        """
            Add new item to inventory.
        """
        try:
            msg = MessageHandler()
            dba = DatabaseAccess(None)
            categories = dba.get_categories()
            if msg.confirmation('add a new item to the inventory?'):
                while category not in categories: 
                    self.print_categories()
                    category = get_input('Category: ')
                name = get_input('Name: ')
                description = get_input('Description: ')
                state = get_input('State [0 - 10]: ')
                comment = get_input('Comment: ')
                if int(state) in range(11):
                    state = int(state)
                else:
                    raise Exception('Wrong state value, could not convert to int.')
                #input retrieved, now add it to the db
                dba.save_item(name, description, state, comment)
            dba = None
            msg = None
        except Exception as ex:
            print('Error in add_item:', ex)

    def print_categories(self):
        """
            Print the available categories.
        """
        #TODO: fancy this up
        dba = DatabaseAccess
        print(dba.get_categories)
        dba = None

    def update_item(self, id):
        """
            If id exists: update values.
        """
        print('Not implemented yet.')

    def delete_item(self, id):
        """
            If id exists: update values.
        """
        print('Not implemented yet.')

    def backup(self):
        """
            Make a backup of the output file.
        """
        #TODO: create export that will print a summary (of e.g. the profile) to txt.
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
