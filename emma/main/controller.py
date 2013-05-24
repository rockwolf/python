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
    
    def __init__(self, config, pool, amount, tax, commission, shares, price, buy, automatic, market, commodity):
        """ Initialize """
        # initialise special vars
        self.config = config #object
        # Decimal precision
        getcontext().prec = 4
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
            print('Not implemendet yet...')
        #TODO: needs market and commodity!
        #TODO: do the calculations + print the result
        calc = Calculator(
            self.pool,
            self.amount,
            self.tax,
            self.commission,
            self.shares,
            self.price,
            self.buy)
        
        if profile:
            print('Test: profile implemented yet.')

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
