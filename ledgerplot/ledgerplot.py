#!/usr/bin/env python
"""
    Usage:
        ledgerplot [options]
    
    Options:
        --ledger <ledger file>
        --income_vs_expenses [<year>|<start date> <end date> [total]]
        -V, --version
"""

"""
See LICENSE.txt file for copyright and license details.
"""

from docopt import docopt
import sys

from constant.py import *


__all__ = ['ledgerplot']
__version__ = 'v0.1'
    
if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)
    
    if args['--ledger']:
        ledger_file = args['--ledger']
        print 'Using ledger file %s'.format(ledger_file)
        
    if args['--income_vs_expenses']:
        from plot_income_vs_expenses import PlotIncomeVsExpenses
        plot = PlotIncomeVsExpenses()
        arglen = len(args['--income_vs_expenses'])
        print '-TEST- len(args[--income_vs_expenses]=%d'.format(arglen)
        if arglen = 3:
            plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD_TOTAL)
        elif arglen = 2:
            plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD)
        elif arglen = 1:
            plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_YEAR)
        elif arglen = 0:
            plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW)
        else:
            print 'Too many arguments.'
            
        plot = None
    sys.exit(0)
