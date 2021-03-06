#!/usr/bin/env python
"""
    Usage:
        ledgerplot [options]
    
    Options:
        --ledger <FILE>
        --income_vs_expenses [<YEAR>]
        --start-date <STARTDATE>
        --end-date <ENDDATE>
        --detail
        -V, --version
"""

"""
See LICENSE.txt file for copyright and license details.
"""

from docopt import docopt
import sys

from constant import *


#__all__ = ['ledgerplot']
__version__ = 'v0.1'


def adjust_system_path():
    """
        Adjust the system path, so we can search in custom dirs for modules.
    """
    sys.path.append('modules')


def plot_income_vs_expenses(
    a_ledger_file,
    a_year,
    a_start_date,
    a_end_date,
    a_is_detail):
    """
        Plot income  vs expenses.
    """
    from income_vs_expenses import PlotIncomeVsExpenses

    plot = PlotIncomeVsExpenses()
    if not is_detail and start_date and end_date:
        plot.prepare_data(
            a_ledger_file,
            year,
            start_date,
            end_date,
            PlotDataRetrievalType.FOR_PERIOD_TOTAL
        )
    elif is_detail and start_date and end_date:
        plot.prepare_data(
            ledger_file,
            year,
            start_date,
            end_date,
            PlotDataRetrievalType.FOR_PERIOD
        )
    elif year and not (start_date and end_date):
        plot.prepare_data(
            ledger_file,
            year,
            start_date,
            end_date,
            PlotDataRetrievalType.FOR_YEAR
        )
    elif not year and not (start_date and end_date):
        plot.prepare_data(
            ledger_file,
            year,
            start_date,
            end_date,
            PlotDataRetrievalType.UNTIL_NOW
        )
    else:
        print 'Argument specification is wrong for {}.'.format(
            PlotType.INCOME_VS_EXPENSES
        )
        print """Correct combinations are:
            --income_vs_expenses
            --income_vs_expenses year
            --income_vs_expenses
                --start-date "YYYY-MM-DD" --end-date "YYYY-MM-DD"
            --income_vs_expenses
                --start-date "YYYY-MM-DD" --end-date "YYYY-MM-DD" --detail"""
        exit(1)
    plot.dat_file = '../{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extension.DAT)
    plot.load_data()
    plot.plot_data(year, start_date, end_date, is_detail)
    plot = None

if __name__ == "__main__":
    adjust_system_path()
    args = docopt(__doc__, help=True, version=__version__)

    year = None
    start_date = None
    end_date = None
    ledger_file = ''

    if args['--ledger']:
        ledger_file = args['--ledger']
        print 'Using ledger file {}'.format(ledger_file)

    is_detail = args['--detail']
    print 'Detail = {}'.format(is_detail)

    if args['--start-date']:
        start_date = args['--start-date']

    if args['--end-date']:
        end_date = args['--end-date']

    if args['--income_vs_expenses']:
        year = args['--income_vs_expenses']
        plot_income_vs_expenses(
            ledger_file,
            year,
            start_date,
            end_date,
            is_detail
        )
    else:
        # DEFAULT graph, when no options are given, beside the ledger file
        plot_income_vs_expenses(
            ledger_file,
            year,
            start_date,
            end_date,
            is_detail
        )
    sys.exit(0)
