#!/usr/bin/env python
"""
See LICENSE.txt file for copyright and license details.
"""


class PlotDataRetrievalType():
    """
        Types that describe different ways to
        get data for a plot.
    """
    UNTIL_NOW = 0
    FOR_YEAR = 1
    FOR_PERIOD = 2
    FOR_PERIOD_TOTAL = 3


class Extension():
    """
        Filename extensions.
    """
    DAT = '.dat'


class PlotType():
    """
        Different plot type strings.
    """
    INCOME_VS_EXPENSES = 'income_vs_expenses'


class ErrorMsg():
    """
        Error messages.
    """
    CouldNotPrepareLedgerData = 'Error: could not prepare the ledger data: {}'


class Color():
    """
        Colors to be used in plots.
    """
    RED = 'r'
    GREEN = 'g'
    BLUE = 'b'
