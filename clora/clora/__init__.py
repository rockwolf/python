#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

import sys
import argparse


def main(add, update_id, delete_id, show_inventory, inventory_file):
    """ Main driver. """
    ### Run the application ###
    from main import MainWrapper
    wrapper = MainWrapper()
    wrapper.run(add, update_id, delete_id, show_inventory, inventory_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLOthing Rotation Application")
    parser.add_argument(
        '-f',
        '--file',
        help='Database file to use: <path/to/file>',
        default='/home/rockwolf/.config/clora/inventory.md',
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
    inventory_file = args['file']

    if args['python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(
        add,
        update_id,
        delete_id,
        show_inventory,
        inventory_file)
