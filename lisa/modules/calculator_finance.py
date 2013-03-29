"""
See LICENSE file for copyright and license details.
"""

"""
A file with Lisa specific financial calculations
"""

from ctypes import *

lib = cdll.LoadLibrary('modules/lib-calculator_finance.so')

api = {
    'calcStoploss': (c_double,    [c_double, c_int, c_double, c_double, c_double, c_double]),
    'calcRiskInput': (c_double,   [c_double, c_double]),
    'calcRiskInitial': (c_double, [c_double, c_int, c_double]),
    'calcRiskActual': (c_double,  [c_double, c_int, c_double, c_int, c_double, c_double]),
    'calcRMultiple': (c_double,   [c_double, c_double, c_double]),
    'calcCostTotal': (c_double,   [c_double, c_double, c_double, c_double]),
    'calcAmountSimple': (c_double,[c_double, c_int]),
    'costTransaction': (c_double, [c_string, c_double, c_int, c_double, c_double]),
    'calcProfitLoss': (c_double,  [c_double, c_double, c_double]),
    'calcCostOther': (c_double,   [c_double, c_double])
    }

def calculate_stoploss(self, amount_buy_simple, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start):
    """
        Calculates the stoploss.
    """
    # TODO: test if this works + see if it can be writen with less code.
    f = getattr(lib, api['calcStoploss'])
    f.restype, f.argtypes = api['calcStoploss']
    input, expected = (amount_buy_simple, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start)
    assert f(input) == expected
    return expected

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

def calculate_r_multiple(self, price_buy, price_sell, stoploss):
    """ 
        Function to calculate R-multiple.
    """
    return 

def calculate_cost_total(self, tax_buy, commission_buy, tax_sell, commission_sell):
    """
        Returns the total costs associated with the given trade.
    """
    return 

def calculate_amount_simple(self, price, shares):
    """
        Calculates the amount without tax and commission.
    """
    return

def cost_transaction(self, transaction, price, shares, tax, commission):
    """
        Cost of transaction (tax and commission)
    """
    return

def calculate_profit_loss(self, amount_sell_simple, amount_buy_simple, total_cost):
    """
        Calculates the profit_loss.
    """
    return 

def calculate_cost_other(self, total_cost, profit_loss):
    """
        Calculates others costs based on the difference that remains.
    """
    return

def calculate_commission(self):
    """
        Calculation for T_RATE.
    """
    #TODO: Put all the commission stuff in the CalculatorFinance.hs lib and link to it here.
    return 
