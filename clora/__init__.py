#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

import sys
import argparse

def main(add, update_id, delete_id, show_inventory):
    """ Main driver. """
    ### Run the application ###
    from main.main import MainWrapper
    wrapper = MainWrapper()
    wrapper.run(add, update_id, delete_id, show_inventory)
      
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
    parser = argparse.ArgumentParser(description="CLOthing Rotation Application")
    parser.add_argument(
    	'-f',
        '--file',
        help='Database file to use: <path/to/file>',
        default='~/.config/clora',
        action='store')
    parser.add_argument(
        '-l',
        '--list',
        help='Show current wardrobe status',
        default=True,
        action='store_true')
    parser.add_argument(
        '-a',
        '--add',
        help='Add item to wardrobe',
        default=False,
        action='store_true')
    parser.add_argument(
        '-u',
        '--update',
        help='Update item from wardrobe: <id>',
        default=False,
        action='store_true')
    parser.add_argument(
        '-d',
        '--delete',
        help='Delete item from wardrobe: <id>',
        default=False,
        action='store_true')
    parser.add_argument(
        '--install',
        help='Installation.',
        default=False,
        action='store_true')
    parser.add_argument(
        '--uninstall',
        help='Uninstall.',
        default=False,
        action='store_true')
    parser.add_argument(
        '-V',
        '--version',
        help='Shows application version and usage.',
        default=False,
        version='Emma 1.00',
        action='version')
    parser.add_argument(
        '--python',
        help='Shows python version in use on the system.',
        default=False,
        action='store_true')
    args = vars(parser.parse_args())
   
    add = args['add']
    update_id = int(args['update'])
    delete_id = int(args['delete'])
    show_inventory = args['list']
    
    if args['install']:
        install()
        sys.exit(0)
    elif args['uninstall']:
        uninstall()
        sys.exit(0)
    elif args['python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(
        add
        , update_id
        , delete_id
        , show_inventory)
