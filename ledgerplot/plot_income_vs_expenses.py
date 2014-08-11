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
        self.dat_file = ''

    def prepare_data(piveType = PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW):
        """
            Extract the data we want to plot from ledger.
        """
        try:
            if piveType = PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD_TOTAL:
                call(['sh', 'ledger -f $1 --real -s -d "T&l<=1" -b $2 -e $3 bal -Equity -^assets expenses income > income_vs_expenses.dat'])
            elif piveType = PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_PERIOD:
                call(['sh', 'ledger -f $1 --real -s -d "T&l<=1" --begin $2 --end $3 bal --period-sort --monthly -Equity -^assets expenses income > income_vs_expenses.dat'])
            elif piveType = PlotIncomeVsExpensesType.ALL_DATA_FOR_GIVEN_YEAR:
                call(['sh', 'ledger -f $1 --real -s -p $2 -d "T&l<=1" bal --period-sort --yearly -Equity -^assets expenses income > income_vs_expenses.dat'])
            elif piveType = PlotIncomeVsExpensesType.ALL_DATA_UNTIL_NOW:
                call(['sh', 'ledger -f $1 --real -s -d "T&l<=1" bal -Equity -^assets expenses income > income_vs_expenses.dat'])
        except:
            print 'Error: could not prepare the ledger data.'
        
    def load_data():
        """
            Load data
        """
        var_data = open(self.dat_file, 'r').read()
        var_data_array = var_data.split('\n')
        i = 0
        for line in var_data_array:
            i += 1
            # skip the last 2 lines of the output
            if (len(line)>1) and (i<len(var_data_array) - 2):
                x_array.append(abs(float(line.strip().split(' ')[0].strip())))
                y_array.append(i)
                
    def autolabel(rects):
        """
          Automatic labels.
        """
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
                    
    def plot_data():
        """
            Plots the loaded data.
        """
        #TODO: move the below to seperate functions.
        N = 1
        income = x_array[1] # ledger shows expenses first,
                            # so reverse to get income vs expenses.
        expenses = x_array[0]

        ind = np.arange(N)  # the x locations for the groups
        width = 0.15       # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind+width, expenses, width, color='r')
        rects2 = ax.bar(ind, income, width, color='g')

        # add some
        ax.set_ylabel('Value (EUR)')
        title_year = ''
        if len(sys.argv) > 2:
            title_year = ' - {}'.format(sys.argv[2].strip())
        ax.set_title('Income vs. expenses{}'.format(title_year))
        ax.set_xticks(ind+width)
        ax.set_xticklabels( ('2014') )

        ax.legend( (rects1[0], rects2[0]), ('Expenses', 'Income') )

    
        autolabel(rects1)
        autolabel(rects2)

        plt.show()

if __name__ == "__main__":
    plot = PlotIncomeVsExpenses()
    plot.dat_file = sys.argv[1].strip()
    plot.prepare_data()
    plot.load_data() # load x_array and y_array
    plot.plot_data()
    plot = None
