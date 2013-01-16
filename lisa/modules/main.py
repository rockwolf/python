#!/usr/env/python
"""
Author: Andy Nagels
Date: 2010-08-24
Lisa: Less Interaction Saves Action
A frontend for a database to store financial transactions in a convenient way.

Copyright (C) 2010 Andy Nagels

This file is part of Lisa.

Lisa is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lisa is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Lisa. If not, see <http://www.gnu.org/licenses/>.
					
"""
import sys

from modules.config import ConfigParser
from main.controller import ControllerMain
from modules.fileimport import FileImport
from modules.fileexport import FileExport
from setup.setup import Setup
        
class MainWrapper():
    """ Main logic 
    
    Parsed options get there functionality here,
    it's seperate from the gui part of the app.
    
    """ 
    
    def __init__(self):
        """ Set program params and python path and load the config. """
        self.exitstate = 0   

        # Adjust system path so we can import from our
        # own module directories
        self.adjust_system_path()

        self.msghandler = __import__('messagehandler')

        # config
        self.config = ConfigParser()

    def adjust_system_path(self):
        """
        Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('main')
        sys.path.append('pyqt')
        sys.path.append('pyqt_generic')
        sys.path.append('database')
        sys.path.append('database_generic')
        sys.path.append('modules')
        sys.path.append('modules_generic')
        sys.path.append('setup')
    
    def file_import(self):
        """ import """
        setup = Setup()
        setup.clear_tables()
        setup.drop_constraints()
        imp = FileImport(self.config)
        imp.file_import()
        setup.add_constraints()
        setup = None
        imp = None

    def file_export(self):
        """ export """
        exp = FileExport(self.config)
        exp.file_export()
        exp = None


    def run(self):
        """ This is the main driver for the program. """
        #TODO: put the QTGui crap in the view and call that from the
        #controller. This part of the code should be used to start the
        #controller.
        if self.exitstate == 1:
            sys.exit(0)
        else:
            #run the controller
            ctl = ControllerMain(self.config)
            ctl.run()
            ctl = None
