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

        # config
        self.config = ConfigParser()

    def adjust_system_path(self):
        """
           Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('main')
        sys.path.append(os.path.join(os.path.dirname(__file__), "../../lisa/lisa/modules_generic"))  
        sys.path.append('modules')
        sys.path.append(os.path.join(os.path.dirname(__file__), "../../lisa/lisa/database_generic"))  
        sys.path.append('database')
        sys.path.append(os.path.join(os.path.dirname(__file__), "../../lisa/lisa/pyqt_generic"))  
        sys.path.append('pyqt')
        #TODO: how to import meta.py stuff? It links to modules/....
        #Perhaps make dummy files that import from the lisa files?
        #Or maybe move files to a general upper directory?
    
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
