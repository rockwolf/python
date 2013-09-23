#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.constant import *
from generic.modules.calculator_finance import *
from decimal import Decimal
from generic.modules.function import print_in_columns

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
        try:
            #Note: the order is important...
            # Input values
            if self.shares == Decimal(-1.0):
                # here, pool, risk, commission and tax and price should be given
                # TODO: check for these conditions
                self.shares = calculate_shares_recommended(self.pool, self.risk, self.commission, self.tax, self.price)
            if self.price == Decimal(-1.0):
                # here, amount, shares, tax and commission should be given
                # TODO: check for these conditions
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
            if self.commission == Decimal(-1.0):
                # here, account, market, commodity, price and shares should be given
                # TODO: check for these conditions
                self.commission = calculate_commission(
                    self.account
                    , self.market
                    , self.commodity
                    , self.price
                    , self.shares)
            if self.amount == Decimal(-1.0):
                # here, price, shares, tax and commission should be given
                # TODO: check for these conditions
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
            #TODO: Relevant error msg when none of those conditions are met.

            # Extra calculatable fields
            # TEST INFO
            print(self.amount)
            print(self.tax)
            print(self.commission)
            print(self.shares)
            # /TEST INFO
            # GENERAL - input
            self.result_general["amount"] = str(self.amount)
            self.result_general["tax"] = str(self.tax)
            self.result_general["commission"] = str(self.commission)
            # GENERAL - extra info
            self.result_general["amount_simple"] = str(calculate_amount_simple(self.shares, self.price))
            self.result_general["shares"] = str(calculate_shares_recommended(self.pool, self.risk, self.commission, self.tax, self.price))
            # BUY
            self.result_buy["cost_tax"] = str(cost_tax(Transaction.BUY, self.amount, self.commission, self.shares, self.price))
            self.result_buy["amount_with_tax"] = str(calculate_amount_with_tax(self.tax, self.shares, self.price))
            # SELL
            self.result_sell["cost_tax"] = str(cost_tax(Transaction.SELL, self.amount, self.commission, self.shares, self.price))
            self.result_sell["amount_with_tax"] = str(calculate_amount_with_tax(self.tax, self.shares, self.price))
        except Exception as ex:
            print('Error in calculate:', ex)

    def print_general(self):
        """
            Print the results with headers etc.
        """
        try:
            headers_general = [
                ["amount", "tax", "commission", "shares", "amount_simple"]
                , ['-'*len("amount"), '-'*len("tax"), '-'*len("commission"), '-'*len("shares"), '-'*len("amount_simple")]]
            headers_buy_sell = [
                ["cost_tax", "amount_with_tax"]
                , ['-'*len("cost_tax"), '-'*len("amount_with_tax")]]
            
            subheader = [["GENERAL"], ['-'*len("GENERAL")*2]]
            print_in_columns(subheader)
            print_in_columns(headers_general)
            print_in_columns(self.result_general.values())
            if self.buy:
                subheader = [["BUY"], ['-'*len("BUY")*2]]
                print_in_columns(subheader)
                print_in_columns(headers_buy_sell)
                print_in_columns(self.result_buy.values())
            else:
                subheader = [["SELL"], ['-'*len("SELL")*2]]
                print_in_columns(subheader)
                print_in_columns(headers_buy_sell)
                print_in_columns(self.result_sell.values())
        except Exception as ex:
            print('Error in print_results():', ex)

    def print_gnucash(self):
        """
            Print statements to enter in gnucash.
        """
        try:
            headers = [
                ['account', 'shares', 'price', 'debit', 'credit']
                , ['-'*len('account'), '-'*len('shares'), '-'*len('price'), '-'*len('debit'), '-'*len('credit')]]
            if self.buy:
                lines = []
                lines.append(["assets:stock:<market>.<commodity>", self.shares, self.price, "", self.result_general["amount_simple"]])
                lines.append(["expenses:commission:stock:<market>.<commodity>", "", "", self.commission])
                lines.append(["expenses:tax:stock:<market>.<commodity>", "", "", self.result_buy["cost_tax"]])
                lines.append(["assets:current_assets:stock:<bank account>", "", "", "", self.amount])
                subheader = [["BUY"], ['-'*len("BUY")*2]]
                print_in_columns(subheader)
                print_in_columns(headers)
                print_in_columns(lines)
            else:
                lines = []
                lines.append(["assets:stock:<market>.<commodity>", self.shares, self.price, self.result_general["amount_simple"], ""])
                lines.append(["expenses:commission:stock:<market>.<commodity>", "", "", self.commission, ""])
                lines.append(["expenses:tax:stock:<market>.<commodity>", "", "", "", self.result_sell["cost_tax"]])
                lines.append(["assets:current_assets:stock:<bank account>", "", "", "", self.amount])
                subheader = [["SELL"], ['-'*len("SELL")*2]]
                print_in_columns(subheader)
                print_in_columns(headers)
                print_in_columns(lines)
        except Exception as ex:
            print('Error in print_gnucash():', ex)
