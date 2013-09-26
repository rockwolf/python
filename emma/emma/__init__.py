#!/usr/env/python
"""Equations for Money Management Application
        
Usage:
    emma [options]

Options:
    -a amount, --amount amount
    -l pool, --pool pool
    -b, --buy
    -c commission, --commission commission
    -t tax, --tax tax
    -s shares, --shares shares
    -p price, --price price
    -m market, --market market              [default: ebr]
    -d commodity, --commodity commodity
    -u account, --account account           [default: binb00]
    -r risk, --risk risk                    [default: 0.02]
    -u symbol, --currency symbol            [default: USD]
    -x rate, --exchange rate                [default: 1.0]
    --estimate
    --export
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
__version__ = 'Emma 1.02'

import sys

from setup.setup import Setup
from decimal import Decimal
from modules.constant import *

def main(pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account, profile, risk, currency, exchange, estimate, export):
    """ Main driver. """
    ### Run the application ###
    from main.main import MainWrapper
    wrapper = MainWrapper(pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account, risk, currency, exchange, estimate, export)
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
    args = docopt(__doc__, help=True, version=__version__)
   
    pool = Decimal(args['--pool']) if args['--pool'] else DEFAULT_DECIMAL
    amount = Decimal(args['--amount']) if args['--amount'] else DEFAULT_DECIMAL
    tax = Decimal(args['--tax'])/Decimal(100.0) if args['--tax'] else DEFAULT_DECIMAL
    commission = Decimal(args['--commission']) if args['--commission'] else DEFAULT_DECIMAL
    shares = Decimal(args['--shares']) if args['--shares'] else DEFAULT_DECIMAL
    price = Decimal(args['--price']) if args['--price'] else DEFAULT_DECIMAL
    buy = bool(args['--buy'])
    automatic = bool(args['--automatic'])
    profile = bool(args['--profile'])
    market = args['--market']
    commodity = args['--commodity']
    account = args['--account']
    risk = Decimal(args['--risk']) if args['--risk'] else Decimal(0.02)
    currency = args['--currency'] if args['--currency'] else DEFAULT_CURRENCY
    exchange = args['--exchange'] if args['--exchange'] else DEFAULT_DECIMAL
    estimate = args['--estimate']
    export = args['--export']
   
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
        , profile
        , risk
        , currency
        , exchange
        , estimate
        , export)
