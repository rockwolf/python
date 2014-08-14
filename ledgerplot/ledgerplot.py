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
    
    
def plot_income_vs_expenses(ledger_file, year, start_date, end_date, is_total, arglen):
    """
        Plot income  vs expenses.
    """
    from plot_income_vs_expenses import PlotIncomeVsExpenses
    plot = PlotIncomeVsExpenses()
    arglen = len(arg_ive)
    print '-TEST- len(args[--income_vs_expenses]=%d'.format(arglen)
    if is_total and (arglen == 3):
        plot.prepare_data(ledger_file, year, start_date, end_date, PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD_TOTAL)
    elif not is_total and (arglen == 3):
        plot.prepare_data(ledger_file, year, start_date, end_date, PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD)
    elif arglen == 2:
        plot.prepare_data(ledger_file, year, start_date, end_date, PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_YEAR)
    elif arglen == 1:
        plot.prepare_data(ledger_file, year, start_date, end_date, PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW)
    else:
        print 'Too many arguments.'
    plot.dat_file = DatFile.INCOME_VS_EXPENSES
    plot.load_data()
    plot.plot_data(year, start_date, end_date, is_total)
    plot = None
        
if __name__ == "__main__":
    args = docopt(__doc__, help=True, version=__version__)
    
    if args['--ledger']:
        ledger_file = args['--ledger']
        print 'Using ledger file {}'.format(ledger_file)
        
    is_total = args['--total']
    print 'Total = {}'.format(is_total)
    
    arg_ive = args['--income_vs_expenses']
    arglen = len(arg_ive)
    year = arg_ive[0]
    start_date = arg_ive[1]
    end_date = arg_ive[2]

    if args['--income_vs_expenses']:
        plot_income_vs_expenses(ledger_file, year, start_date, end_date, is_total, arglen)
    sys.exit(0)
