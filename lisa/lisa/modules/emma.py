#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.constant import *
from generic.modules.calculator_finance import *
from decimal import Decimal
from generic.modules.function import print_in_columns

class Emma():
    """
        Emma class
    """
   
    def __init__(self, pool, amount, tax, commission, shares, price, buy, market, commodity, account, risk, currency, exchange, estimate):
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
        self.risk = risk
        self.currency = currency
        self.exchange = exchange
        self.estimate = estimate
        # result
        self.result_general = {}
        self.result_buy = {}
        self.result_sell = {}
  
    def calculate(self):
        """
            Calculate all possible unknown values.
        """
        result = {}
        try:
            #Note: the order is important...
            # Input values
            if self.shares == Decimal(-1.0):
                # here, pool, risk, commission and tax and price should be given
                needed = []
                needed.append(self.pool)
                needed.append(self.risk)
                needed.append(self.commission)
                needed.append(self.tax)
                needed.append(self.price)
                if has_missing_parameter(needed):
                    raise Exception("Shares unknown, but parameter(s) missing for calculation.\n" \
                    "Please enter pool, risk, commission, tax and price info.")
                self.shares = calculate_shares_recommended(self.pool, self.risk, self.commission, self.tax, self.price)
            if self.price == Decimal(-1.0):
                # here, amount, shares, tax and commission should be given
                needed = []
                needed.append(self.amount)
                needed.append(self.shares)
                needed.append(self.tax)
                needed.append(self.commission)
                if has_missing_parameter(needed):
                    raise Exception("Price unknown, but parameter(s) missing for calculation.\n" \
                    "Please enter amount, shares, tax and commission info.")
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
                needed = []
                needed.append(self.account)
                needed.append(self.market)
                needed.append(self.commodity)
                needed.append(self.price)
                needed.append(self.shares)
                if has_missing_parameter(needed):
                    raise Exception("Commission unknown, but parameter(s) missing for calculation.\n" \
                    "Please enter account, market, commodity, price and shares info.")
                self.commission = calculate_commission(
                    self.account
                    , self.market
                    , self.commodity
                    , self.price
                    , self.shares)
            if self.amount == Decimal(-1.0):
                # here, price, shares, tax and commission should be given
                needed = []
                needed.append(self.price)
                needed.append(self.shares)
                needed.append(self.tax)
                needed.append(self.commission)
                if has_missing_parameter(needed):
                    raise Exception("Amount unknown, but parameter(s) missing for calculation.\n" \
                    "Please enter price, shares, tax and commission info.")
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
            # TEST INFO
            print self.amount
            print self.tax
            print self.commission
            print self.shares
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
            print 'Error in calculate:', ex
            
    def has_missing_parameter(self, parameters):
        """
            Returns a boolean that says if the parameters list has a value
            of DEFAULT_DECIMAL or not. True = a parameter is missing.
        """
        return DEFAULT_DECIMAL in parameters
