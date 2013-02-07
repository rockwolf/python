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
import getopt

from setup.setup import Setup

# general properties of the app
pprog = 'lisa.py'
pversion = '01.00'
prelease = 'Mass Convenience'
pdate = '2012-04-10'

def main(option):
    """ Main driver. """
    ### Run the application ###
    #NOTE: the import statement loads the views and tables,
    #but when doing an install, they are not created yet.
    #So we skip loading this until we are sure we can start.
    from main.main import MainWrapper
    wrapper = MainWrapper()
    if (option == 'import'):
        wrapper.file_import()
        wrapper.exitstate = 1
    if (option == 'export'):
        wrapper.file_export()
        wrapper.exitstate = 1
    wrapper.run() #run the main method for the program

def install():
    """ install """
    setup = Setup()
    setup.install()
    setup = None

def uninstall():
    """ uninstall """
    setup = Setup()
    setup.uninstall()
    setup = None

def usage():
        """ Print usage info and exit """
        print('''{0} : Less Interaction Saves Action
Options: 
 -h : displays this help message
 --install : creates tables and views needed
 --uninstall : deletes all relevant tables and views in the database, 
            all data will be destroyed...
 --version : displays version
 --python : displays Python version
All arguments are optional.'''.format(self.pprog))

if __name__ == "__main__":
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(
            sys.argv[1:], 'h', ['import', 'export', 'install', 'uninstall', 'version', 'python'])
    except getopt.error as err:
        print('Error: ' + str(err))
        sys.exit(1)
    
    option = ''
    for opt in options[:]:
        if opt[0] == '-h':
            usage()
            sys.exit(0)
            break
    for opt in options[:]:
        if opt[0] == '--import':
            option = 'import'
            sys.exit(0)
            break
    for opt in options[:]:
        if opt[0] == '--export':
            option = 'export'
            sys.exit(0)
            break
    for opt in options[:]:
        if opt[0] == '--install':
            install()
            sys.exit(0)
            break
    for opt in options[:]:
        if opt[0] == '--uninstall':
            uninstall()
            sys.exit(0)
            break
    for opt in options[:]:
        if opt[0] == '--version':
            str_list = [
                pprog,
                ' version ',
                pversion,
                ' (',
                pdate,
                '), \'',
                prelease,
                '\' release.']
            print(''.join(str_list))
            sys.exit(0)
            break
    for opt in options[:]:
        if opt[0] == '--python':
            print('Python ' + sys.version)
            sys.exit(0)
            break
    main(option)
