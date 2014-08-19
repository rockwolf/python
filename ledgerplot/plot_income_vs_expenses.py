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
from constant import *

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

    def prepare_data(self, ledger_file, year, start_date, end_date, plot_sub_type = PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW):
        """
            Extract the data we want to plot from ledger.
        """
        try:
            if plot_sub_type == PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD_TOTAL:
                print '-TEST- test1'
                call(['sh', 'ledger -f {} --real -s -d "T&l<=1" --begin {} --end {} bal -Equity -^assets expenses income > {}'.format(
                    ledger_file, start_date, end_date), '{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extention.DAT)])
            elif plot_sub_type == PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD:
                print '-TEST- test2'
                call(['sh', 'ledger -f {} --real -s -d "T&l<=1" --begin {} --end {} bal --period-sort --monthly -Equity -^assets expenses income > {}'.format(
                    ledger_file, start_date, end_date), '{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extention.DAT)])
            elif plot_sub_type == PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_YEAR:
                print '-TEST- test3'
                call(['sh', 'ledger -f {} --real -s -p {} -d "T&l<=1" bal --period-sort --yearly -Equity -^assets expenses income > {}'.format(
                    ledger_file, year), '{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extention.DAT)])
            elif plot_sub_type == PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW:
                print '-TEST- test4'
                call(['sh', 'ledger -f {} --real -s -d "T&l<=1" bal -Equity -^assets expenses income > {}'.format(
                    ledger_file, '{}{}'.format(PlotType.INCOME_VS_EXPENSES, Extention.DAT))])
        except Exception as ex:
            print 'Error: could not prepare the ledger data: {}'.format(ex)
        
    def load_data(self):
        """
            Load data
        """
        var_data = open(self.dat_file, 'r').read()
        var_data_array = var_data.split('\n')
        i = 0
        for line in var_data_array:
            i += 1
            # skip the last 2 lines of the output
            if (len(line) > 1) and (i < len(var_data_array) - 2):
                self.x_array.append(abs(float(line.strip().split(' ')[0].strip())))
                self.y_array.append(i)
                
    def autolabel(self, rects):
        """
          Automatic labels.
        """
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2.,
                1.05 * height, '{}'.format(int(height)),
                ha='center',
                va='bottom')
                    
    def plot_data(self, year, start_date, end_date, is_detail):
        """
            Plots the loaded data.
        """
        N = 1
        income = self.x_array[0]
        expenses = self.x_array[1]

        ind = np.arange(N)  # the x locations for the groups
        width = 0.15       # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, expenses, width, color = 'r')
        rects2 = ax.bar(ind + width, income, width, color = 'g')
        rects3 = ax.bar(ind + 2 * width, (expenses - income), width, color = 'b')
        # add some labels/text
        ax.set_ylabel('Value (EUR)')
        title = ''
        if year:
            title = ' - {}'.format(year)
        elif is_detail:
            title = ' - per month for period from {} until {}'.format(start_date, end_date)
        elif not is_detail:
            ' - total for period from {} until {}'.format(start_date, end_date)
        ax.set_title('Income vs. expenses{}'.format(title))
        ax.set_xticks(ind+width)
        #ax.set_xticklabels( ('2014') ) #TODO: use the year from the input? But do we need this?
        ax.legend((rects1[0], rects2[0], rects3[0]), ('Expenses', 'Income', 'Profit'))
        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)
        plt.show()

if __name__ == "__main__":
    #TODO: finish/correct this for testing purposes
    plot = PlotIncomeVsExpenses()
    plot.dat_file = sys.argv[1].strip()
    plot.prepare_data()
    plot.load_data() # load x_array and y_array
    plot.plot_data()
    plot = None
