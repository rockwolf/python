#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""
import sys

from modules.config import ConfigParser
from main.controller import ControllerMain
from setup.setup import Setup
        
class MainWrapper():
    """
        Set system paths and run the app.
    """
    
    def __init__(self, pool, amount, tax, commission, shares, price, buy, automatic, market, commodity, account, risk, currency, exchange, estimate, export):
        """
            Set program params and python path and load the config.
        """
        self.exitstate = 0

        # Adjust system path so we can import from our
        # own module directories
        self.adjust_system_path()

        self.msghandler = __import__('generic.modules.messagehandler')

        # config
        self.config = ConfigParser()
        
        # variables
        self.pool = pool
        self.amount = amount
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
        self.currency = currency
        self.exchange = exchange
        self.estimate = estimate
        self.export = export

    def adjust_system_path(self):
        """
            Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('main')
        sys.path.append('database')
        sys.path.append('modules')
        sys.path.append('setup')
        sys.path.append('generic')

    def run(self, profile):
        """
            This is the main driver for the program.
        """
        if self.exitstate == 1:
            sys.exit(0)
        else:
            #run the controller
            ctl = ControllerMain(
                    self.config,
                    self.pool,
                    self.amount,
                    self.tax,
                    self.commission,
                    self.shares,
                    self.price,
                    self.buy,
                    self.automatic,
                    self.market,
                    self.commodity,
                    self.account,
                    self.risk,
                    self.currency,
                    self.exchange,
                    self.esetimate,
                    self.export)
            ctl.run(profile)
            ctl = None
