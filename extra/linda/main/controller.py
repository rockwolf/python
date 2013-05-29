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
    
    def __init__(self, config):
        """ Initialize """
        # initialise special vars
        self.config = config
        

    # Methods
    ## General
    def run(self):
        """ Run the app. """
        print('Not implemented yet.')
