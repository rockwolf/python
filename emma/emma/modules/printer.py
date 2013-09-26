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
   
    def __init__(self):
        """
            Initialise
        """
        pass
    
    def print_general(self, result_general, result_buy, result_sell, export_file = ""):
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
            print_in_columns([result_general.values()])
            if self.buy:
                subheader = [["BUY"], ['-'*len("BUY")*2]]
                print_in_columns(subheader)
                print_in_columns(headers_buy_sell)
                print_in_columns([result_buy.values()])
            else:
                subheader = [["SELL"], ['-'*len("SELL")*2]]
                print_in_columns(subheader)
                print_in_columns(headers_buy_sell)
                print_in_columns([result_sell.values()])
        except Exception as ex:
            print('Error in print_results():', ex)

    def print_gnucash(self, result_general, result_buy, result_sell, export_file = ""):
        """
            Print statements to enter in gnucash.
        """
        try:
            headers = [
                ['account', 'shares', 'price', 'debit', 'credit']
                , ['-'*len('account'), '-'*len('shares'), '-'*len('price'), '-'*len('debit'), '-'*len('credit')]]
            if self.buy:
                lines = []
                lines.append(["assets:stock:<market>.<commodity>", self.shares, self.price, "", result_general["amount_simple"]])
                lines.append(["expenses:commission:stock:<market>.<commodity>", "", "", self.commission])
                lines.append(["expenses:tax:stock:<market>.<commodity>", "", "", result_buy["cost_tax"]])
                lines.append(["assets:current_assets:stock:<bank account>", "", "", "", self.amount])
                subheader = [["BUY"], ['-'*len("BUY")*2]]
                print_in_columns(subheader)
                print_in_columns(headers)
                print_in_columns(lines)
            else:
                lines = []
                lines.append(["assets:stock:<market>.<commodity>", self.shares, self.price, result_general["amount_simple"], ""])
                lines.append(["expenses:commission:stock:<market>.<commodity>", "", "", self.commission, ""])
                lines.append(["expenses:tax:stock:<market>.<commodity>", "", "", "", result_sell["cost_tax"]])
                lines.append(["assets:current_assets:stock:<bank account>", "", "", "", self.amount])
                subheader = [["SELL"], ['-'*len("SELL")*2]]
                print_in_columns(subheader)
                print_in_columns(headers)
                print_in_columns(lines)
        except Exception as ex:
            print('Error in print_gnucash():', ex)
