#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""
import sys

from modules.config import ConfigParser
from controller.controller import ControllerMain
from modules.fileimport import FileImport
from modules.fileexport import FileExport
from setup.setup import Setup
from modules.constant import *
        
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

        # config
        self.config = ConfigParser()

    def adjust_system_path(self):
        """
            Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('controller')
        sys.path.append('view')
        sys.path.append('model')
        sys.path.append('database')
        sys.path.append('modules')
        sys.path.append('generic')
        sys.path.append('generic/modules')
        sys.path.append('generic/view')
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

    def export(self, export_type):
        """
            export
        """
        exp = FileExport(self.config)
        if export_type == Export.LEDGER:
            exp.ledger_export()
        else:
            exp.csv_export()
        exp = None

    def unit_test(self):
        """
            unit testing
        """
        print("Importing TestValues class...")
        from generic.modules.calculator_finance_test import TestValues
        print("Initialize class...")
        unittest.main()
        print("Done.")

    def run(self):
        """
            This is the main driver for the program.
        """
        if self.exitstate == 1:
            sys.exit(0)
        else:
            #run the controller
            ctl = ControllerMain(self.config)
            ctl.run()
            ctl = None
