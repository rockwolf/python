#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""
import sys

from modules.config import ConfigParser
from main.controller import ControllerMain
from modules.fileimport import FileImport
from modules.fileexport import FileExport
from setup.setup import Setup
        
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
        """
            import
        """
        setup = Setup()
        setup.clear_tables()
        setup.drop_constraints()
        imp = FileImport(self.config)
        imp.file_import()
        setup.add_constraints()
        setup = None
        imp = None

    def file_export(self):
        """
            export
        """
        exp = FileExport(self.config)
        exp.file_export()
        exp = None

    def run(self):
        """
            This is the main driver for the program.
        """
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
