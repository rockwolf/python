#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

from os.path import isfile
import shutil
import os, sys
from decimal import getcontext
from modules.config import ConfigParser
from modules.calculator import Calculator

class ControllerMain():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, config, pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account):
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

    # Methods
    ## General
    def run(self, profile):
        """
            Start the app.
        """
        #TODO: if automatic: get tax and commission from library
        print('<test>')
        print(self.pool)
        print(self.amount)
        print(self.tax)
        print(self.commission)
        print(self.shares)
        print(self.price)
        print(self.buy)
        print(self.automatic)
        print(self.market)
        print(self.commodity)
        print('test: account =', self.account)
        print('</test>')
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
            , self.account)
        calc.calculate()
        calc.print_pretty()
        self.print_separator()
        calc.print_gnucash()
        
        if profile:
            print('Profile not implemented yet.')

    def print_separator(self):
        """
            Print nice divider line.
        """
        print('-'*80)

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
