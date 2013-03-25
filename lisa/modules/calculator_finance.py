"""
See LICENSE file for copyright and license details.
"""

"""
A file with Lisa specific financial calculations
"""

from decimal import Decimal
from ctypes import *

lib = cdll.LoadLibary('./CalculatorFinance.so')

def calculate_stoploss(self, amount_buy_simple, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start):
    """
        Calculates the stoploss.
    """
    -- TODO: call the library functions
    func = '
    return 

def calculate_profit_loss(self, amount_buy, amount_sell):
    """
        Calculates the profit_loss.
    """
    return 

def calculate_risk_input(self, i_pool, i_risk):
    """
        Calculates the risk based on total pool and input.
        Consider this the theoretical risk we want to take.
    """
    return 

def calculate_risk_initial(self, price_buy, shares_buy, stoploss):
    """
        Calculates the initial risk.
        This is the risk we will take if our stoploss is reached.
        This should be equal to the risk_input if everything was
        correctly calculated.
    """
    return 

def calculate_risk_actual(self, price_buy, shares_buy, price_sell, shares_sell, stoploss, risk_initial):
    """
        Calculates the risk we actually took,
        based on the data in TABLE_TRADE.
    """
    return 

def calculate_cost_total(self, tax_buy, commission_buy, tax_sell, commission_sell):
    """
        Returns the total costs associated with the given trade.
    """
    return 

def calculate_commission(self):
    """
        Calculation for T_RATE.
    """
    return 

def calculate_r_multiple(self, price_buy, price_sell, stoploss):
    """ 
        Function to calculate R-multiple.
    """
    return 
