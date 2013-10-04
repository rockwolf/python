#!/usr/env/python
"""
    Lisa: Less Interaction Saves Action

    Usage:
        lisa [options]

    Options:
        --import
        --export        [ledger|csv] [default: ledger]
        --install
        --uninstall
        --test
        -V, --version 
        --python
"""
"""
    See LICENSE file for copyright and license details.
"""
from docopt import docopt

__all__ = ['lisa']
__version__ = 'v2.1'

import sys

from setup.setup import Setup
from modules.constant import *

def main(option, export_type, testmode):
    """ Main driver. """
    ### Run the application ###
    #NOTE: the import statement loads the views and tables,
    #but when doing an install, they are not created yet.
    #So we skip loading this until we are sure we can start.
    from main import MainWrapper
    wrapper = MainWrapper()
    if testmode:
        print("test: unit_test")
        wrapper.unit_test()
        wrapper.exitstate = 1
    if (option == 'import'):
        wrapper.file_import()
        wrapper.exitstate = 1
    if (option == 'export'):
        wrapper.export(export_type)
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
    args = docopt(__doc__, help=True, version=__version__)
   
    option = ''
    export_type = ''
    testmode = False
    if args['--import']:
        option = 'import'
    elif args['--export']:
        option = 'export'
        if args['--export'] == Export.LEDGER:
            export_type = Export.LEDGER
        elif args['--export'] == Export.CSV:
            export_type = Export.CSV
        else:
            print("Error: wrong export type (" + 
                    args['--export'] +
                    "), falling back on the default (" +
                    Export.CSV +
                    ")!");
            export_type = Export.CSV
    elif args['--install']:
        install()
        sys.exit(0)
    elif args['--uninstall']:
        uninstall()
        sys.exit(0)
    elif args['--test']:
        testmode = True
    elif args['--python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(option, export_type, testmode)
