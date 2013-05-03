#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""

import sys
#import getopt
import argparse

#from modules.constant import *

def main():
    """ Main driver. """
    ### Run the application ###
    from main.main import MainWrapper
    wrapper = MainWrapper()
    wrapper.run() #run the main method for the program

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lisa INteractive Drawdown Application")
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
   
    if args['python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main()
