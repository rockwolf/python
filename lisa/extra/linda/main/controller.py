#!/usr/env/python
"""
   See LICENSE file for copyright and license details.
"""

from os.path import isfile
import shutil
import os, sys
from decimal import getcontext

from database.databaseaccess import DatabaseAccess
from modules.constant import *

class ControllerMain():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, config, limit):
        """ Initialize """
        # initialise vars
        self.config = config
        self.limit = limit

    # Methods
    ## General
    def run(self, manual):
        """ Run the app. """
        # Show records with drawdown
        self.show_records(self.limit)
        # Determine drawdown value to use
        drawdown_id = dba.get_latest_drawdown_id()
        input_drawdown_id = input('Enter drawdown_id [' + str(drawdown_id) + ': ')
        if input_drawdown_id != '':
           drawdown_id = int(input_drawdown_id)
        if manual:
           day = input('Enter day of drawdown: ')
        else:
           day = dba.get_drawdown_value(drawdown_id) 
        print('day =', day)
        # Save new value
        update_drawdown_value(drawdown_id, day)
         
    def show_records(self, limit):
        """
            Shows last <limit> records with drawdown.
        """
        dba = DatabaseAccess(self.config)
        for record in dba.get_last_records(limit):
            print(record)
        dba = None
   
    def update_drawdown_value(drawdown_id, day):
        """
            Write <day> to drawdown_value for record <drawdown_id>.
        """
        dba = DatabaseAccess(self.config)
        dba.update_drawdown_value(drawdown_id, day)
        dba = None
