#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

import sys
import argparse

from setup.setup import Setup

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
        wrapper.export(export_type)
        wrapper.exitstate = 1
    #TODO: add stuff for export to ledger format?
    wrapper.run() #run the main method for the program
      
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Equations for Money Management Application")
    parser.add_argument(
    	'-u',
        '--use',
        help='Money used on trade: <double>',
        default=0.0,
        action='store')
    parser.add_argument(
    	'-l',
        '--pool',
        help='Total pool available: <double>',
        default=0.0,
        action='store')
    #action='store_true')
    parser.add_argument(
    	'-c',
        '--commission',
        help='For a setup, though .',
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
        version='Emma 1.00',
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
    elif args['export']:
        option = 'export'
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
