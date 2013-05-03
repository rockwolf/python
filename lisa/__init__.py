#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""

from datetime import datetime

import sys
import getopt
import argparse

from setup.setup import Setup
from modules.constant import *

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
        if export_type == EXPORT_LEDGER:
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Less Interaction Saves Action")
    parser.add_argument(
        '--import',
        help='Import csv files from import directory specified in config.',
        default=False,
        action='store_true')
    parser.add_argument(
        '--export',
        help='Export to the given type. [csv|ledger]',
        default='',
        action='store')
    #action='store_true')
    parser.add_argument(
        '--install',
        help='Sets up the database, by executing the required sql scripts.',
        default=False,
        action='store_true')
    parser.add_argument(
        '--uninstall',
        help='Removes all records and tables from the database!',
        default=False,
        action='store_true')
    parser.add_argument(
        '-V',
        '--version',
        help='Shows application version.',
        default=False,
        version='Lisa 2.00',
        action='version')
    parser.add_argument(
        '--python',
        help='Shows python version in use on the system.',
        default=False,
        action='store_true')
    args = vars(parser.parse_args())
   
    option = ''
    export_type = ''
    if args['import']:
        option = 'import'
    elif args['export'] != '':
        option = 'export'
        print(args['export'])
        if args['export'] == EXPORT_LEDGER:
            export_type = EXPORT_LEDGER
        elif args['export'] == EXPORT_CSV:
            export_type = EXPORT_CSV
        else:
            print("Error: wrong export type (" + 
                    args['export'] +
                    "), falling back on the default (" +
                    EXPORT_CSV +
                    ")!");
            export_type = EXPORT_CSV
    elif args['install']:
        install()
        sys.exit(0)
    elif args['uninstall']:
        uninstall()
        sys.exit(0)
    elif args['python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(option, export_type)
