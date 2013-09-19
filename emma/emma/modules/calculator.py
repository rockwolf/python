#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from generic.modules.calculator_finance import *
from modules.constant import *
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
        # result
        self.result_general = {}
        self.result_buy = {}
        self.result_sell = {}
  
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
                print('test: shares =', self.shares)
            if self.price == Decimal(-1.0):
                print('test: ', self.amount)
                if self.buy:
                    self.price = calculate_price(
                        Transaction.BUY
                        , self.amount
                        , self.shares
                        , self.tax
                        , self.commission)
                else:
                    self.price = calculate_price(
                        Transaction.SELL
                        , self.amount
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
                        , self.commission)
                else:
                    self.amount = calculate_amount(
                        self.price
                        , self.shares
                        , Transaction.SELL
                        , self.tax
                        , self.commission)

            # Extra calculatable fields
            # GENERAL
            self.result_general["amount"] = self.amount
            self.result_general["tax"] = self.tax
            self.result_general["commission"] = self.commission
            self.result_general["amount_simple"] = calculate_amount_simple(self.shares, self.price)
            # BUY
            self.result_buy["cost_tax"] = cost_tax(Transaction.BUY, self.amount, self.commission, self.shares, self.price)
            self.result_buy["amount_with_tax"] = calculate_amount_with_tax(self.tax, self.shares, self.price)
            # SELL
            self.result_sell["cost_tax"] = cost_tax(Transaction.SELL, self.amount, self.commission, self.shares, self.price)
            self.result_sell["amount_with_tax"] = calculate_amount_with_tax(self.tax, self.shares, self.price)
        except Exception as ex:
            print('Error in calculate:', ex)

    def print_pretty(self):
        """
            Print the results with headers etc.
        """
        try:
            print('GENERAL')
            print('-------')
            print(self.result_general)
            if self.buy:
                print('BUY')
                print('-------')
                print(self.result_buy)
            else:
                print('SELL')
                print('-------')
                print(self.result_sell)
        except Exception as ex:
            print('Error in print_pretty():', ex)

    def print_gnucash(self):
        """
            Print statements to enter in gnucash.
        """
        try:
            headers = ['account', 'shares', 'price', 'debit', 'credit']
            if self.buy:
                print('BUY')
                print('-------')
                print(''.join(column.rjust(10) for header in headers))
                print(
                    'assets:stock:<market>.<commodity>,' +
                    str(self.shares) +
                    ',' +
                    str(self.price) +
                    ',' +
                    str(self.result_general["amount_simple"]) +
                    ','
                )
                print(
                    'expenses:commission:stock:<market>.<commodity>,,' + 
                    str(self.commission) +
                    ','
                )
                print(
                    'expenses:tax:stock:<market>.<commodity>,,' +
                    str(self.result_buy["cost_tax"])
                )
                print(
                    'assets:current_assets:stock:<bank account>,,,' +
                    str(self.amount)
                )
            else:
                print('SELL')
                print('-------')
                print(''.join(column.rjust(10) for header in headers))
                print(
                    'assets:stock:<market>.<commodity>,' +
                    str(self.shares) + 
                    ',' +
                    str(self.price) +
                    ',' +
                    str(self.result_general["amount_simple"]) +
                    ','
                )
                print(
                    'expenses:commission:stock:<market>.<commodity>,,' +
                    str(self.commission) +
                    ','
                )
                print(
                    'expenses:tax:stock:<market>.<commodity>,,' +
                    str(self.result_sell["cost_tax"])
                )
                print(
                    'assets:current_assets:stock:<bank account>,,,' +
                    str(self.amount)
                )
        except Exception as ex:
            print('Error in print_gnucash():', ex)
