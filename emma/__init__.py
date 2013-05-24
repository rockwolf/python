#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

import sys
import argparse

from setup.setup import Setup

def main(use, pool, tax, commission, shares, price, buy, automatic, profile):
    """ Main driver. """
    ### Run the application ###
    #NOTE: the import statement loads the views and tables,
    #but when doing an install, they are not created yet.
    #So we skip loading this until we are sure we can start.
    from main.main import MainWrapper
    wrapper = MainWrapper(use, pool, tax, commission, shares, price, buy, automatic)
    wrapper.run(profile) #run the main method for the program
      
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
        '-b',
        '--buy',
        help='Are we buying? Or selling?',
        default=True,
        action='store_true')
    parser.add_argument(
    	'-c',
        '--commission',
        help='Commission',
        default=False,
        action='store')
    parser.add_argument(
        '-t',
        '--tax',
        help='Tax amount to use: <double>',
        default=0.0025,
        action='store')
    parser.add_argument(
        '-s,
        '--shares',
        help='Tax amount to use: <double>',
        default=1,
        action='store')
    parser.add_argument(
        '-p,
        '--price
        help='Price: <double>',
        default=0.0
        action='store')
    parser.add_argument(
        '-a',
        '--automatic',
        help='Override tax/commission values with the values from the library!',
        default=False,
        action='store_true')
    #TODO: a setting for each profile with "<double>;<double>;<double>" as values?
    parser.add_argument(
        '--profile',
        help='Show profile information.',
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
   
    #TODO: add value checking here, so we don't enter wrong types etc.
    use = args['use']
    pool = args['pool']
    tax = args['tax']
    commission = args['commission']
    shares = args['shares']
    price = args['price']
    buy = args['buy']
    automatic = args['automatic']
    profile = args['profile']
    
    if args['install']:
        install()
        sys.exit(0)
    elif args['uninstall']:
        uninstall()
        sys.exit(0)
    elif args['python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(use, pool, tax, commission, shares, price, buy, automatic, profile)
