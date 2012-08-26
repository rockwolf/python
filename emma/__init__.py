#!/usr/env/python
"""
Author: Andy Nagels
Date: 2011-11-12
Emma: Equations for Money Management

Copyright (C) 2010 Andy Nagels

This file is part of Emma.

Emma is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Emma is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Emma. If not, see <http://www.gnu.org/licenses/>.
					
"""
import getopt
import sys
from decimal import Decimal

from main.controller import ControllerMain
from modules.config import ConfigParser
#from modules.mdlprocess import Process
from modules.config import ConfigParser
from setup.setup import Setup
        
class MainWrapper():
    """ Main logic 
    
    Parsed options get there functionality here.
    
    """ 

    def __init__(self, parent=None):
        """ Init. """
        # general properties of the app
        self.pprog = 'Emma'
        self.pversion = '0.02'
        self.prelease = 'I want some mushu!'
        self.pdate = '2012-08-26'
        self.exitstate = 0   

        # Adjust system path so we can import from our
        # own module directories
        self.adjust_syspath()

        self.msghandler = __import__('messagehandler')
        # config
        self.config = ConfigParser()
 
    def adjust_syspath(self):
        """ Adjust the system path, so we can search in custom dirs for modules. """
        sys.path.append('main')
        sys.path.append('pyqt')
        sys.path.append('modules')
        sys.path.append('modules_generic')
        sys.path.append('setup')

   
    def usage(self):
        """ Print usage info and exit """
        print('''{0} : Equations for Money Management Application
Options (general):
------------------
 --verbose, -v : verbose mode
 --help, -h : displays this help message
 --version, -V : displays version
 --python : displays Python version '''.format(self.pprog))

    def run(self):
        """ This is the main driver for the program. """
        if self.exitstate == 1:
            sys.exit(0)
        else:
            #run the controller
            ctl = ControllerMain(self.config)
            ctl.run()
            ctl = None

    def install(self):
        """ install """
        setup = Setup()
        setup.install()
        setup = None

    def uninstall(self):
        """ uninstall """
        setup = Setup()
        setup.uninstall()
        setup = None


def main():
    """ Main driver, startup and cli options parsing. """
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(
                sys.argv[1:], 'hvV', ['version', 'verbose'])
    except getopt.error as err:
        print('Error: ' + str(err))
        sys.exit(1)
    wrapper = MainWrapper()
    wrapper.exitstate = 0

    try:
        for opt, arg in options:
            if opt in ('-h','--help'):
                wrapper.usage()
                # don't run the program after the optionparsing
                wrapper.exitstate = 1
            elif opt in ('-V', '--version'):
                str_list = [
                    wrapper.pprog,
                    ' version ',
                    wrapper.pversion,
                    ' (',
                    wrapper.pdate,
                    '), \'',
                    wrapper.prelease,
                    '\' release.']
                print(''.join(str_list))
                wrapper.exitstate = 1
            elif opt in ('-v', '--verbose'):
                    wrapper.verbose = True
    except Exception as ex:
        print('Error parsing arguments: ', ex)
        exit(1)

    wrapper.run() #run the main method for the program

if __name__ == "__main__":
    main()
