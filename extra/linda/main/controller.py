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
    
    def __init__(self, config, days):
        """ Initialize """
        # initialise vars
        self.config = config
        self.days = days

    # Methods
    ## General
    def run(self, update):
        """ Run the app. """
        #TODO: show list of drawdown values and trades for <limit> latest records
        #ask for an id
        # when not update: ask for a number of days
        #TODO: open dba session to call for the codes
        drawdown_id = dba.get_latest_drawdown_id()
        input_drawdown_id = input('Enter drawdown_id [' + str(drawdown_id) + ': ')
        if input_drawdown_id != '':
           drawdown_id = int(input_drawdown_id)
        if update:
           day = dba.get_drawdown_value(drawdown_id)
        else:
            day = input('Enter day of drawdown: ')
        print('day =', day)
        update_drawdown_value(drawdown_id, day)
