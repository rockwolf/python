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
        self.risk = Decimal(0.02)
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
                self.shares = calculate_shares_recommended(self.pool, self.risk, self.commission, self.tax, self.price)
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
            # GENERAL - input
            self.result_general["amount"] = self.amount
            self.result_general["tax"] = self.tax
            self.result_general["commission"] = self.commission
            self.result_general["amount_simple"] = calculate_amount_simple(self.shares, self.price)
            # GENERAL - need to know
            self.result_general["shares"] = calculate_shares_recommended(self.pool, self.risk, self.commission, self.tax, self.price)
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
            headers_general = ["amount", "tax", "commission", "shares", "amount_simple"]
            headers_buy_sell = ["cost_tax", "amount_with_tax"]
            
            print('GENERAL')
            print('-------')
            print(''.join(header.rjust(len(header)+3) for header in headers_general))
            print(''.join(str(value).rjust(len(str(value))+3) for value in self.result_general.values()))
            if self.buy:
                print('BUY')
                print('-------')
                print(''.join('{:^30}'.format(header) for header in headers_buy_sell))
                print(''.join('{:^30}'.format(str(value)) for value in self.result_buy.values()))
            else:
                print('SELL')
                print('-------')
                print(''.join('{:^30}'.format(header) for header in headers_buy_sell))
                print(''.join('{:^30}'.format(str(value)) for value in self.result_sell.values()))
        except Exception as ex:
            print('Error in print_pretty():', ex)

    def print_gnucash(self):
        """
            Print statements to enter in gnucash.
        """
        try:
            headers = ['account', 'shares', 'price', 'debit', 'credit']
            if self.buy:
                line1 = ["assets:stock:<market>.<commodity>", self.shares, self.price, "", self.result_general["amount_simple"]]
                line2 = ["expenses:commission:stock:<market>.<commodity>", "", "", self.commission]
                line3 = ["expenses:tax:stock:<market>.<commodity>", "", "", self.result_buy["cost_tax"]]
                line4 = ["assets:current_assets:stock:<bank account>", "", "", "", self.amount]
                print('BUY')
                print('-------')
                print(''.join(header.center(len(header)+3) for header in headers))
                print('{:x^30}'.format(''.join(str(item) for item in line1)))
                print(''.join(str(item).center(len(str(item))+3) for item in line2))
                print(''.join(str(item).center(len(str(item))+3) for item in line3))
                print(''.join(str(item).center(len(str(item))+3) for item in line4))
            else:
                line1 = ["assets:stock:<market>.<commodity>", self.shares, self.price, self.result_general["amount_simple"], ""]
                line2 = ["expenses:commission:stock:<market>.<commodity>", "", "", self.commission, ""]
                line3 = ["expenses:tax:stock:<market>.<commodity>", "", "", "", self.result_sell["cost_tax"]]
                line4 = ["assets:current_assets:stock:<bank account>", "", "", "", self.amount]
                print('SELL')
                print('-------')
                print(''.join(header.center(len(header)+3) for header in headers))
                print(''.join(str(item).center(len(str(item))+3) for item in line1))
                print(''.join(str(item).center(len(str(item))+3) for item in line2))
                print(''.join(str(item).center(len(str(item))+3) for item in line3))
                print(''.join(str(item).center(len(str(item))+3) for item in line3))
        except Exception as ex:
            print('Error in print_gnucash():', ex)
