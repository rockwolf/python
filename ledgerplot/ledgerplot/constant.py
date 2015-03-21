#!/usr/bin/env python
"""
See LICENSE.txt file for copyright and license details.
"""


class PlotDataRetrievalType():
    """
        Types that describe different ways to
        get data for a plot.
    """
    ALL_DATA_UNTIL_NOW = 0
    ALL_DATA_FOR_GIVEN_YEAR = 1
    ALL_DATA_FOR_GIVEN_PERIOD = 2
    ALL_DATA_FOR_GIVEN_PERIOD_TOTAL = 3


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
