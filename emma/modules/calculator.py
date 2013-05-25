#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.calculator_finance import *

class Calculator():
    """
        Calculator class
    """
   
    def __init__(self, pool, amount, tax, commission, shares, price, buy, market, commodity):
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
  
    def calculate(self):
        """
            Calculate all possible unknown values.
        """
        try:
           #TODO: determine what fields are given and calculate accordingly
           sp = calculate_amount_simple(self.price, self.shares)
        except:
            pass

    def print_pretty(self):
        """
            Print the results with headers etc.
        """
        try:
            pass
        except:
            pass
      
