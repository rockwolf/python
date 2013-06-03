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
            # GENERAL
            result_general["amount"] = self.amount
            result_general["tax"] = self.tax
            result_general["commission"] = self.commission
            # BUY
            result_buy["cost_tax"] = cost_tax(Transaction.BUY, self.amount, self.commission, self.shares, self.price)
            result_buy["amount_tax_buy"] = calculate_amount_with_tax(Transaction.BUY, self.amount, self.commission, self.shares, self.price)
            # SELL
            result_sell["cost_tax_sell"] = cost_tax(Transaction.SELL, self.amount, self.commission, self.shares, self.price)
            result_sell["amount_tax_sell"] = calculate_amount_with_tax(Transaction.SELL, self.amount, self.commission, self.shares, self.price)
            print_pretty(result_dict)
        except Exception as ex:
            print('Error in calculate:', ex)

    def print_pretty(self, result_general, result_buy, result_sell):
        """
            Print the results with headers etc.
        """
        try:
            print('GENERAL')
            print('-------')
            print(result_general)
            print('BUY')
            print('-------')
            print(result_buy)
            print('SELL')
            print('-------')
            print(result_sell)
        except:
            print('Could not print the values...')
