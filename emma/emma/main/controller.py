#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

from os.path import isfile
import shutil
import os
#from decimal import getcontext
from modules.calculator import Calculator
from generic.modules.function import print_separator, print_in_columns
from generic.modules.constant import Align

class ControllerMain():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, config, pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account, risk):
        """ Initialize """
        # initialise special vars
        self.config = config #object
        # Decimal precision
        #getcontext().prec = 28
        # Parameters
        self.pool = pool
        self.amount = amount #full amount (incl. tax + comm.)
        self.tax = tax
        self.commission = commission
        self.shares = shares
        self.price = price
        self.buy = buy
        self.automatic = automatic
        self.market = market
        self.commodity = commodity 
        self.account = account
        self.risk = risk

    # Methods
    ## General
    def run(self, profile):
        """
            Start the app.
        """
        #TODO: if automatic: get tax and commission from library
        if self.automatic:
            #self.tax = retrieve_tax...
            #self.commission = retrieve_commission
            print('WARNING: Automatic retrieval of commission and tax not implemendet yet!')
            print('         Please use the -c and -t switches.')
        calc = Calculator(
            self.pool
            , self.amount
            , self.tax
            , self.commission
            , self.shares
            , self.price
            , self.buy
            , self.market
            , self.commodity
            , self.account
            , self.risk)
        calc.calculate()
        
        header = [["GENERAL"]]
        print_in_columns(header, Align.LEFT)
        print_separator()
        calc.print_general()
        print('')
        header = [["GNUCASH"]]
        print_in_columns(header, Align.LEFT)
        print_separator()
        calc.print_gnucash()
        
        if profile:
            print('Profile not implemented yet.')

    def backup(self):
        """
            Make a backup of the output file.
        """
        #TODO: create export that will print a summary (of e.g. the profile) to txt.
        # remove old backup
        if isfile(self.config.backupfile):
            try:
                os.remove(self.config.backupfile)
                print(self.config.backupfile + ' removed.')
            #except IOError as strerror:
            except Exception as ex:
                print("Error: ", ex)
        # copy current to .bak
        if isfile(self.config.exportfile) and not isfile(self.config.backupfile):
            try:
                shutil.copy(self.config.exportfile, self.config.backupfile)
                print(self.config.backupfile + ' created.')
            except Exception as ex:
                print('Error: application fucked up while creating backup: ', ex)
        else:
            print('Error: backup file already exists.')
