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
from constant import PlotDataRetrievalType, Extension, PlotType, ErrorMsg, Color


class Const():
    """
        Local constants, used in the class of this file.
    """
    EXPENSES = 'Expenses'
    INCOME = 'Income'
    PROFIT = 'Profit'
    BAR_WIDTH = 0.15
    TITLE_YEAR = 'Income vs. expenses - {}'
    TITLE_DETAIL = ('Income vs. expenses  - per month',
        ' for period from {} until {}')
    TITLE_NO_DETAIL = 'Income vs. expenses  - total for period from {} until {}'
    LABEL_Y_AXIS = 'Value (EUR)'
    
class Commands():
    """
        Ledger command strings.
    """
    FOR_PERIOD_TOTAL = 'ledger -f {0} --real -s -d ""T&l<=1"" --begin {1} --end {2} bal -Equity -^assets expenses income > {3}'
    FOR_PERIOD = 'ledger -f {0} --real -s -d ""T&l<=1"" --begin {1} --end {2} bal --period-sort --monthly -Equity -^assets expenses income > {3}'
    FOR_YEAR = 'ledger -f {0} --real -s -p {1} -d ""T&l<=1"" bal --period-sort --yearly -Equity -^assets expenses income > {2}'
    UNTIL_NOW = 'ledger -f {0} --real -s -d ""T&l<=1"" bal -Equity -^assets expenses income > {1}'

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

    def prepare_data(
        self,
        a_ledger_file,
        a_year,
        a_start_date,
        a_end_date,
        a_plot_sub_type=PlotDataRetrievalType.UNTIL_NOW):
        """
            Extract the data we want to plot from ledger and
            save it to dat-files.
        """
        try:
            import pdb; pdb.set_trace()
            l_file = '../{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extension.DAT)
            if a_plot_sub_type == PlotDataRetrievalType.FOR_PERIOD_TOTAL:
                call([
                    Commands.FOR_PERIOD_TOTAL.format(
                        a_ledger_file, a_start_date, a_end_date, l_file
                    )
                ])
            elif a_plot_sub_type == PlotDataRetrievalType.FOR_PERIOD:
                call([
                    Commands.FOR_PERIOD.format(
                        a_ledger_file, a_start_date, a_end_dat, l_file
                    )
                ])
            elif a_plot_sub_type == PlotDataRetrievalType.FOR_YEAR:
                call([
                    Commands.FOR_YEAR.format(
                        a_ledger_file, a_year, l_file
                    )
                ])
            elif a_plot_sub_type == PlotDataRetrievalType.UNTIL_NOW:
                call([
                    Commands.UNTIL_NOW.format(
                        a_ledger_file, l_file
                    )
                ])
        except Exception as ex:
            print ErrorMsg.CouldNotPrepareLedgerData.format(ex)

    def load_data(self):
        """
            Load data from the dat-files into memory.
        """
        l_data_array = open(self.dat_file, 'r').read().split('\n')
        i = 0
        for l_line in l_data_array:
            i += 1
            # skip the last 2 lines of the output
            if (len(l_line) > 1) and (i < len(l_data_array) - 2):
                self.x_array.append(
                    abs(
                        float(l_line.strip().split(' ')[0].strip())
                    )
                )
                self.y_array.append(i)

    def autolabel(self, a_rects, a_ax):
        """
          Automatic labels.
        """
        # attach some text labels
        for l_rect in a_rects:
            l_height = l_rect.get_height()
            a_ax.text(
                l_rect.get_x() + l_rect.get_width() / 2.,
                1.05 * l_height,
                '{}'.format(int(l_height)),
                ha='center',
                va='bottom')

    def plot_data(self, a_year, a_start_date, a_end_date, a_is_detail):
        """
            Plots the loaded data via MatplotLib.
        """
        l_N = 1
        l_income = self.x_array[0]
        l_expenses = self.x_array[1]

        l_ind = np.arange(l_N)  # the x locations for the groups
        l_width = Const.BAR_WIDTH       # the width of the bars
        l_fig, l_ax = plt.subplots()
        l_rects1 = l_ax.bar(l_ind, l_expenses, l_width, l_color=Const.RED)
        l_rects2 = l_ax.bar(l_ind + l_width, l_income, l_width,
            l_color=Const.GREEN)
        l_rects3 = l_ax.bar(l_ind + 2 * l_width,
            (l_expenses - l_income), l_width, l_color=Const.BLUE)
        # add some labels/text
        l_ax.set_ylabel(Const.LABEL_Y_AXIS)
        l_title = ''
        if a_year:
            l_title = Const.TITLE_YEAR.format(a_year)
        elif a_is_detail:
            l_title = Const.TITLE_DETAIL.format(a_start_date, a_end_date)
        elif not a_is_detail:
            Const.TITLE_NO_DETAIL.format(a_start_date, a_end_date)
        l_ax.set_title(l_title)
        l_ax.set_xticks(l_ind + l_width)
        #l_ax.set_xticklabels( ('2014') ) #TODO: use the year from the input?
        # But do we need this?
        l_ax.legend(
            (l_rects1[0], l_rects2[0], l_rects3[0]),
            (Const.Expenses, Const.Income, Const.Profit)
        )
        self.autolabel(l_rects1, l_ax)
        self.autolabel(l_rects2, l_ax)
        self.autolabel(l_rects3, l_ax)
        self.plt.show()

if __name__ == "__main__":
    
    #TODO: finish/correct this for testing purposes
    l_plot = PlotIncomeVsExpenses()
    l_plot.dat_file = sys.argv[1].strip()
    l_plot.prepare_data()
    l_plot.load_data()  # load x_array and y_array
    l_plot.plot_data()
    l_plot = None
