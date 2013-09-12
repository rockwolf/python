#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""
import sys

from main.controller import ControllerMain
from setup.setup import *
        
class MainWrapper():
    """
        Set system paths and run the app.
    """
    
    def __init__(self):
        """
            Set program params and python path and load the config.
        """
        self.exitstate = 0

        # Adjust system path so we can import from our
        # own module directories
        self.adjust_system_path()

    def adjust_system_path(self):
        """
            Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('main')
        sys.path.append('database')
        sys.path.append('modules')
        sys.path.append('modules_generic')
        sys.path.append('setup')

    def run(self, add, update_id, delete_id, show_inventory, inventory_file):
        """
            This is the main driver for the program.
        """
        if self.exitstate == 1:
            sys.exit(0)
        else:
            #run the controller
            ctl = ControllerMain()
            ctl.run(add
                    , update_id
                    , delete_id
                    , show_inventory
                    , inventory_file)
            ctl = None
