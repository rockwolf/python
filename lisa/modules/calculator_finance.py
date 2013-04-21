"""
See LICENSE file for copyright and license details.
"""

"""
A file with Lisa specific financial calculations
"""

from ctypes import *

lib = cdll.LoadLibrary('modules/lib-calculator_finance.so')

# interface to the library 
api = {
        'test': (c_double, [c_double], ())
      }

# initialise the interface
for afunc in api:
    f = getattr(lib, afunc)
    f.restype, f.argtype, test = api[afunc]

def library_test():
    """
        Test if the library works, should return double the given value.
    """
    print('TESTING THE LIBRARY: 3.0 ->', lib.test(c_double(3.0)))

def calculate_stoploss(price_buy, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start):
    """
        Calculates the stoploss.
    """
    return lib.calcStoploss(
            c_double(price_buy)
            , c_int(shares_buy)
            , c_double(tax_buy)
            , c_double(commission_buy)
            , c_double(i_risk)
            , c_double(pool_at_start))

def calculate_risk_input(i_pool, i_risk):
    """
        Calculates the risk based on total pool and input.
        Consider this the theoretical risk we want to take.
    """
    return lib.calcRiskInput(
            c_double(i_pool)
            , c_double(i_risk))

def calculate_risk_initial(price_buy, shares_buy, stoploss):
    """
        Calculates the initial risk.
        This is the risk we will take if our stoploss is reached.
        This should be equal to the risk_input if everything was
        correctly calculated.
    """
    return lib.calcRiskInitial(
            c_double(price_buy)
            , c_double(shares_buy)
            , c_double(stoploss))

def calculate_risk_actual(price_buy, shares_buy, price_sell, shares_sell, stoploss, risk_initial):
    """
        Calculates the risk we actually took,
        based on the data in TABLE_TRADE.
    """
    return lib.calcRiskActual(
            c_double(price_buy)
            , c_int(shares_buy)
            , c_double(price_sell)
            , c_double(shares_sell)
            , c_double(stoploss)
            , c_double(risk_initial))

def calculate_r_multiple(price_buy, price_sell, stoploss):
    """ 
        Function to calculate R-multiple.
    """
    return lib.calcRMultiple(
            c_double(price_buy)
            , c_double(price_sell)
            , c_double(stoploss))

def calculate_cost_total(tax_buy, commission_buy, tax_sell, commission_sell):
    """
        Returns the total costs associated with the given trade.
    """
    return lib.calcCostTotal(
            c_double(tax_buy)
            , c_double(commission_buy)
            , c_double(tax_sell)
            , c_double(commission_sell))

def calculate_amount_simple(price, shares):
    """
        Calculates the amount without tax and commission.
    """
    return lib.calcAmountSimple(
            c_double(price)
            , c_int(shares))

def cost_transaction(transaction, price, shares, tax, commission):
    """
        Cost of transaction (tax and commission)
    """
    return lib.costTransaction(
            c_double(transaction)
            , c_double(price)
            , c_int(shares)
            , c_double(tax)
            , c_double(commission))

def calculate_profit_loss(amount_sell_simple, amount_buy_simple, total_cost):
    """
        Calculates the profit_loss.
    """
    return lib.calcProfitLoss(
            c_double(amount_sell_simple)
            , c_double(amount_buy_simple)
            , c_double(total_cost))

def calculate_cost_other(total_cost, profit_loss):
    """
        Calculates others costs based on the difference that remains.
    """
    return lib.calcCostOther(
            c_double(total_cost)
            , c_double(profit_loss))

def calculate_commission(account, market, stockname, price, shares):
    """
        Calculation for T_RATE.
    """
    return lib.calcCommission(
            c_string(account)
            , c_string(market)
            , c_string(stockname)
            , c_double(price)
            , c_int(shares))
