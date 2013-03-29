"""
See LICENSE file for copyright and license details.
"""

"""
A file with Lisa specific financial calculations
"""

from ctypes import *

lib = cdll.LoadLibrary('modules/lib-calculator_finance.so')

def calculate_stoploss(self, amount_buy_simple, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start):
    """
        Calculates the stoploss.
    """
    #TODO: use the below for all calls
    return lib.CalcStoploss(amount_buy_simple, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start)

def calculate_risk_input(self, i_pool, i_risk):
    """
        Calculates the risk based on total pool and input.
        Consider this the theoretical risk we want to take.
    """
    return lib.CalcRiskInput(i_pool, i_risk)

def calculate_risk_initial(self, price_buy, shares_buy, stoploss):
    """
        Calculates the initial risk.
        This is the risk we will take if our stoploss is reached.
        This should be equal to the risk_input if everything was
        correctly calculated.
    """
    return lib.CalcRiskInitial(price_buy, shares_buy, stoploss)

def calculate_risk_actual(self, price_buy, shares_buy, price_sell, shares_sell, stoploss, risk_initial):
    """
        Calculates the risk we actually took,
        based on the data in TABLE_TRADE.
    """
    return lib.CalcRiskActual(price_buy, shares_buy, price_sell, shares_sell, stoploss, risk_initial)

def calculate_r_multiple(self, price_buy, price_sell, stoploss):
    """ 
        Function to calculate R-multiple.
    """
    return lib.CalcRMultiple(price_buy, price_sell, stoploss)

def calculate_cost_total(self, tax_buy, commission_buy, tax_sell, commission_sell):
    """
        Returns the total costs associated with the given trade.
    """
    return lib.CalcCostTotal(tax_buy, commission_buy, tax_sell, commission_sell)

def calculate_amount_simple(self, price, shares):
    """
        Calculates the amount without tax and commission.
    """
    return lib.CalcAmountSimple(price, shares)

def cost_transaction(self, transaction, price, shares, tax, commission):
    """
        Cost of transaction (tax and commission)
    """
    return lib.CostTransaction(transaction, price, shares, tax, commission)

def calculate_profit_loss(self, amount_sell_simple, amount_buy_simple, total_cost):
    """
        Calculates the profit_loss.
    """
    return lib.CalcProfitLoss(amount_sell_simple, amount_buy_simple, total_cost)

def calculate_cost_other(self, total_cost, profit_loss):
    """
        Calculates others costs based on the difference that remains.
    """
    return lib.CalcCostOther(total_cost, profit_loss)

def calculate_commission(self, account, market, stockname, price, shares):
    """
        Calculation for T_RATE.
    """
    return lib.CalcCommission(account, market, stockname, price, shares)
