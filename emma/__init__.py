#!/usr/env/python
"""Equations for Money Management Application
        
Usage:
    emma [options]

Options:
    -a=amount, --amount=amount
    -l=pool, --pool=pool
    -b, --buy
    -c=commission, --commission=commission  [default: 9.75]
    -t=tax, --tax=tax                       [default: 0.25]
    -s=shares, --shares=shares
    -p=price, --price=price
    -m=market, --market=market              [default: ebr]
    -d=commodity, --commodity=commodity
    -u=account, --account=account           [default: binb00]
    --automatic
    --profile
    --install
    --uninstall
    -V, --version
    --python
"""
"""
See LICENSE file for copyright and license details.
"""
from docopt import docopt

__all__ = ['Emma']
__version__ = 'Emma 1.01'

import sys

from setup.setup import Setup
from decimal import Decimal
from modules.constant import *

def main(pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account, profile):
    """ Main driver. """
    ### Run the application ###
    #NOTE: the import statement loads the views and tables,
    #but when doing an install, they are not created yet.
    #So we skip loading this until we are sure we can start.
    from main.main import MainWrapper
    wrapper = MainWrapper(pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account)
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
    #parser = argparse.ArgumentParser(description="Equations for Money Management Application")
    args = docopt(__doc__, help=True, version=__version__)
    print(args)
   
    #TODO: add value checking here, so we don't enter wrong types etc.
    pool = Decimal(args['--pool']) if args['--pool'] else DEFAULT_DECIMAL
    amount = Decimal(args['--amount']) if args['--amount'] else DEFAULT_DECIMAL
    tax = Decimal(args['--tax']) if args['--tax'] else DEFAULT_DECIMAL
    commission = Decimal(args['--commission'])
    shares = Decimal(args['--shares']) if args['--shares'] else DEFAULT_DECIMAL
    price = Decimal(args['--price']) if args['--price'] else DEFAULT_DECIMAL
    buy = Decimal(args['--buy'])
    automatic = bool(args['--automatic'])
    profile = bool(args['--profile'])
    market = args['--market']
    commodity = args['--commodity']
    account = args['--account']
    
    if args['--install']:
        install()
        sys.exit(0)
    elif args['--uninstall']:
        uninstall()
        sys.exit(0)
    elif args['--python']:
        print('Python ' + sys.version)
        sys.exit(0)
    main(
        pool
        , amount
        , tax
        , commission
        , shares
        , price
        , buy
        , automatic
        , market
        , commodity
        , account
        , profile)
