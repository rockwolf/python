#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""

import sys
#import getopt
import argparse

#from modules.constant import *

def main(manual, limit):
    """ Main driver. """
    ### Run the application ###
    from main.main import MainWrapper
    wrapper = MainWrapper()
    wrapper.run(manual, limit) #run the main method for the program

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lisa INteractive Drawdown Application")
    parser.add_argument(
        '-m',
        '--manual',
        help='Specify a drawdown number manually.',
        default=False,
        action='store_true')
    parser.add_argument(
        '-l',
        '--limit',
        help='--limit <int>: limit list shown to the <int> last records.',
        default=0,
        action='store')
    parser.add_argument(
        '-V',
        '--version',
        help='Shows application version.',
        default=False,
        version='Linda 1.00',
        action='version')
    parser.add_argument(
        '--python',
        help='Shows python version in use on the system.',
        default=False,
        action='store_true')
    args = vars(parser.parse_args())
   
    manual = bool(args['manual'])
    limit = int(args['limit'])
    if args['python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(manual, limit)
