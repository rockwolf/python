#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.calculator_finance import *

class Calculator():
    """
        Calculator class
    """
   
    def __init__(self, pool, amount, tax, commission, shares, price, buy, market, commodity, self.account):
        """
            Initialize
        """
        self.pool = pool
        self.amount = amount
        self.tax = tax
        self.commission = commission
        self.shares = shares
        self.price = price
        self.buy = buy
        self.market = market
        self.account = account
  
    def calculate(self):
        """
            Calculate all possible unknown values.
        """
        try:
            #Note: the order is important...
            # Input values
            if self.shares == Decimal(-1.0):
                self.shares = calculate_shares_recommended()
            if self.price == Decimal(-1.0):
                self.price = calculate_price(
                    self.amount
                    , self.shares
                    , self.tax
                    , self.commission)
                print('price =', self.price)
            if self.commission == Decimal(-1.0):
                self.commission = calculate_commission(
                    self.account
                    , self.market
                    , self.commodity
                    , self.price
                    , self.shares)
            if self.amount == decimal(-1.0):
                self.amount = calculate_amount(...) #TODO: finish this, but I'm first going to add it to the library.
            # Extra calculatable fields
            #TODO: calculate stoploss etc.
        except Exception as ex:
            print('Error in calculate:', ex)

    def print_pretty(self):
        """
            Print the results with headers etc.
        """
        try:
            pass
        except:
            pass
      
