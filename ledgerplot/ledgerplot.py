#!/usr/bin/env python
"""
    Usage:
        ledgerplot [options]
    
    Options:
        --ledger FILE
        --income_vs_expenses [YEAR|STARTDATE ENDDATE]
        --total
        -V, --version
"""

"""
See LICENSE.txt file for copyright and license details.
"""

from docopt import docopt
import sys

from constant import *


__all__ = ['ledgerplot']
__version__ = 'v0.1'
    
    
def plot_income_vs_expenses(is_total):
    """
        Plot income  vs expenses.
    """
    from plot_income_vs_expenses import PlotIncomeVsExpenses
    plot = PlotIncomeVsExpenses()
    arglen = len(args['--income_vs_expenses'])
    print '-TEST- len(args[--income_vs_expenses]=%d'.format(arglen)
    if is_total and (arglen == 2):
        plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD_TOTAL)
    elif not is_total and (arglen == 2):
        plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD)
    elif arglen == 1:
        plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_YEAR)
    elif arglen == 0:
        plot.prepare_data(PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW)
    else:
        print 'Too many arguments.'
    plot.dat_file = DatFile.INCOME_VS_EXPENSES
    plot.load_data()
    plot.plot_data(year, start_date, end_date, total)
    plot = None
        
if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)
    
    if args['--ledger']:
        ledger_file = args['--ledger']
        print 'Using ledger file {}'.format(ledger_file)
        
    is_total = args['--total']
    print 'Total = {}'.format(is_total)
        
    if args['--income_vs_expenses']:
        plot_income_vs_expenses(is_total)
    sys.exit(0)
