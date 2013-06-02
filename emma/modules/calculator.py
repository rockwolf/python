#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.calculator_finance import *
from decimal import Decimal

class Calculator():
    """
        Calculator class
    """
   
    def __init__(self, pool, amount, tax, commission, shares, price, buy, market, commodity, account):
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
        self.commodity = commodity
        self.account = account
  
    def calculate(self):
        """
            Calculate all possible unknown values.
        """
        print('Test: ', self.account)
        try:
            #Note: the order is important...
            # Input values
            if self.shares == Decimal(-1.0):
                self.shares = calculate_shares_recommended()
                print('test: shares =', shares)
            if self.price == Decimal(-1.0):
                print('test: ', self.amount)
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
            if self.amount == Decimal(-1.0):
                if self.buy:
                    self.amount = calculate_amount(
                        self.price
                        , self.shares
                        , Transaction.BUY
                        , self.tax
                        , self.commission) #TODO: finish this, but I'm first going to add it to the library.
                else:
                    self.amount = calculate_amount(
                        self.price
                        , self.shares
                        , Transaction.SELL
                        , self.tax
                        , self.commission) #TODO: finish this, but I'm first going to add it to the library.

            # Extra calculatable fields
            #TODO: calculate stoploss etc.
            cost_tax_buy = (self.amount - self.commission - self.shares * self.price)
            print('cost tax_buy =', cost_tax_buy)
            print('amount only_tax =', self.amount - self.commission)
            print('amount_simple =', self.price * self.shares)
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
      
