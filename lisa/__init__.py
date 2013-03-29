#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""

from datetime import datetime

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
    #TODO: add stuff for export to ledger format?
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
