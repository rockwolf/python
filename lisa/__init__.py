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

def main(option, export_type):
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
        if export_type = EXPORT_LEDGER:
            #TODO: rename to csv_export + create ledger_export
            wrapper.file_export()
        else:
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
 --export : export all tables to csv files
 --import : disable constraints, import csv files and re-enable constraints.
 [-t <export-type>] : export type [csv|ledger] (csv = default)
 --version : displays version
 --python : displays Python version
All arguments are optional.'''.format(self.pprog))

if __name__ == "__main__":
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(
            sys.argv[1:], 'h', "t:", ['import', 'export=', 'install', 'uninstall', 'version', 'python'])
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
            if arg = EXPORT_LEDGER:
                export_type = EXPORT_LEDGER
            elif arg = EXPORT_CSV:
                export_type = EXPORT_CSV
            else:
                print("Error: wrong export type (",
                    arg + "), falling back on the default (",
                    EXPORT_CSV + ")!");
                export_type = EXPORT_CSV
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
    main(option, export_type)
