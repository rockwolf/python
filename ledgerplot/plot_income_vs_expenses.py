#!/usr/bin/env python

"""
    See LICENSE.txt file for copyright and license details.
"""

"""
    A bar plot with income and expense levels.
"""
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import sys
from subprocess import call
from constant import PlotRetrievalType, Extension, PlotType, ErrMsg, Color

class Const():
    """
        Local constants, used in the class of this file.
    """
    EXPENSES = 'Expenses'
    INCOME = 'Income'
    PROFIT = 'Profit'
    BAR_WIDTH = 0.15
    TITLE_YEAR = 'Income vs. expenses - {}'
    TITLE_DETAIL = 'Income vs. expenses  - per month for period from {} until {}'
    TITLE_NO_DETAIL = 'Income vs. expenses  - total for period from {} until {}'
    
class PlotIncomeVsExpenses():
    """
        Plot income vs expenses.
    """
    def __init__(self):
        """
            Init
        """
        self.x_array = []
        self.y_array = []
        self.profit = []
        self.dat_file = ''

    def prepare_data(self, a_ledger_file, a_year, a_start_date, a_end_date, a_plot_sub_type = PlotDataRetrievalType.ALL_DATA_UNTIL_NOW):
        """
            Extract the data we want to plot from ledger.
        """
        try:
            l_file = '{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extension.DAT)
            if plot_sub_type == PlotDataRetrievalType.ALL_DATA_FOR_GIVEN_PERIOD_TOTAL:
                call([
                    'ledger', '-f', a_ledger_file,
                    '--real', '-s', '-d', 'T&l<=1',
                    '--begin', a_start_date, '--end', a_end_date,
                    'bal', '-Equity', '-^assets', 'expenses', 'income', '>', l_file
                    ])
            elif plot_sub_type == PlotDataRetrievalType.ALL_DATA_FOR_GIVEN_PERIOD:
                call([
                    'ledger', '-f', a_ledger_file,
                    '--real', '-s', '-d', 'T&l<=1',
                    '--begin', a_start_date, '--end', a_end_date,
                    'bal', '--period-sort', '--monthly', '-Equity', '-^assets', 'expenses', 'income', '>', l_file
                    ])
            elif plot_sub_type == PlotDataRetrievalType.ALL_DATA_FOR_GIVEN_YEAR:
                call([
                    'ledger', '-f', a_ledger_file,
                    '--real', '-s', '-p', a_year, '-d', 'T&l<=1',
                    'bal', '--period-sort', '--yearly', '-Equity', '-^assets', 'expenses', 'income', '>', l_file
                    ])
            elif plot_sub_type == PlotDataRetrievalType.ALL_DATA_UNTIL_NOW:
                call([
                    'ledger', '-f', a_ledger_file,
                    '--real', '-s', '-d', 'T&l<=1',
                    'bal', '-Equity', '-^assets', 'expenses', 'income >', a_l_file
                    ])
        except Exception as ex:
            print ErrorMsg.CouldNotPrepareLedgerData.format(ex)
        
    def load_data(self):
        """
            Load data
        """
        l_data = open(self.dat_file, 'r').read()
        l_data_array = l_data.split('\n')
        i = 0
        for l_line in l_data_array:
            i += 1
            # skip the last 2 lines of the output
            if (len(l_line) > 1) and (i < len(l_data_array) - 2):
                self.x_array.append(abs(float(l_line.strip().split(' ')[0].strip())))
                self.y_array.append(i)
                
    def autolabel(self, a_rects):
        """
          Automatic labels.
        """
        # attach some text labels
        for l_rect in a_rects:
            l_height = l_rect.get_height()
            ax.text(
                l_rect.get_x() + l_rect.get_width() / 2.,
                1.05 * l_height,
                '{}'.format(int(l_height)),
                ha='center',
                va='bottom')
                    
    def plot_data(self, a_year, a_start_date, a_end_date, a_is_detail):
        """
            Plots the loaded data.
        """
        l_N = 1
        l_income = self.x_array[0]
        l_expenses = self.x_array[1]

        l_ind = np.arange(l_N)  # the x locations for the groups
        l_width = Const.BAR_WIDTH       # the width of the bars
        l_fig, l_ax = plt.subplots()
        l_rects1 = ax.bar(l_ind, l_expenses, l_width, l_color = Const.RED)
        l_rects2 = ax.bar(l_ind + l_width, l_income, l_width, l_color = Const.GREEN)
        l_rects3 = ax.bar(l_ind + 2 * l_width, (l_expenses - l_income), l_width, l_color = Const.BLUE)
        # add some labels/text
        ax.set_ylabel('Value (EUR)')
        l_title = ''
        if year:
            l_title = Const.TITLE_YEAR.format(year)
        elif a_is_detail:
            l_title = Const.TITLE_DETAIL.format(a_start_date, a_end_date)
        elif not a_is_detail:
            Const.TITLE_NO_DETAIL.format(a_start_date, a_end_date)
        ax.set_title(l_title)
        ax.set_xticks(l_ind + l_width)
        #ax.set_xticklabels( ('2014') ) #TODO: use the year from the input? But do we need this?
        ax.legend((l_rects1[0], l_rects2[0], l_rects3[0]), (Const.Expenses, Const.Income, Const.Profit))
        autolabel(l_rects1)
        autolabel(l_rects2)
        autolabel(l_rects3)
        plt.show()

if __name__ == "__main__":
    #TODO: finish/correct this for testing purposes
    l_plot = PlotIncomeVsExpenses()
    l_plot.dat_file = sys.argv[1].strip()
    l_plot.prepare_data()
    l_plot.load_data() # load x_array and y_array
    l_plot.plot_data()
    l_plot = None
