#!/usr/env/python
"""
Author: Andy Nagels
Date: 2010-08-24
Lisa: Pyqt gui for clipf, with extra functionality.

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
import getopt
import sys
from guihandler import Lisa
from subprocess import call

class MainWrapper():
    """ Main logic 
    
    Parsed options get there functionality here,
    it's seperate from the gui part of the app.
    
    """ 

    def __init__(self, parent=None):
        """ Construct basic QApplication, add widgets and start exec_loop. """
        # general properties of the app
        self.pprog = 'lisa.py'
        self.pversion = '0.01a'
        self.prelease = 'Wow, the exit button works!'
        self.pdate = '2010-08-28'
        self.exitstate = 0   
        self.msghandler = __import__('messagehandler')
    
    def usage(self):
        """ Print usage info and exit """
        print('''{0} : Less Interaction Saves Arbeit
Options: 
 -h : displays this help message
 --install : creates tables and views needed
 --uninstall : deletes all relevant tables and views in the database, 
            all data will be destroyed...
 --version : displays version
 --python : displays Python version
All arguments are optional.'''.format(self.pprog))

    def run(self):
        """ This is the main driver for the program. """
        if self.exitstate == 1:
            sys.exit(0)
        # run the gui app
        app = QtGui.QApplication(sys.argv)
        myapp = Lisa()
        myapp.show()
        sys.exit(app.exec_())

    def install(self):
        """ install """
        try:
            call(["sh", "install.sh"])
        except:
            print('Error: could not load install.sh script.')

    def uninstall(self):
        """ uninstall """
        try:
            call(["sh", "uninstall.sh"])
        except:
            print('Error: could not load uninstall.sh script.')

def main():
    """ Main driver, startup and cli options parsing. """
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(
            sys.argv[1:], 'h', ['install', 'uninstall', 'version', 'python'])
    except getopt.error as err:
        print('Error: ' + str(err))
        sys.exit(1)
    wrapper = MainWrapper()
    
    for opt in options[:]:
        if opt[0] == '-h':
            wrapper.usage()
            # don't run the program after the optionparsing
            wrapper.exitstate = 1
    for opt in options[:]:
        if opt[0] == '--install':
            wrapper.install()
            wrapper.exitstate = 1
            break
    for opt in options[:]:
        if opt[0] == '--uninstall':
            wrapper.uninstall()
            wrapper.exitstate = 1
            break
    for opt in options[:]:
        if opt[0] == '--version':
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
            break
    for opt in options[:]:
        if opt[0] == '--python':
            print('Python ' + sys.version)
            wrapper.exitstate = 1
            break

    wrapper.run() #run the main method for the program

if __name__ == "__main__":
    main()
