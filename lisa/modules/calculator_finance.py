"""
See LICENSE file for copyright and license details.
"""

"""
A file with Lisa specific financial calculations
"""

def calculate_stoploss(self, amount_buy_simple, shares_buy, tax_buy, commission_buy, i_risk, pool_at_start):
    """
        Calculates the stoploss.
    """
    #NOTE: amount_buy = with tax and everything included, amount_buy_simple = without tax and commission!
    #NOTE: ((risk/100 * pool_at_start - amount_buy_simple) - commission_buy)/(shares_buy * (tax_buy/100 - 1))
    #NOTE: ((R * P - A) - C) / (S * (T - 1))
    R = Decimal(i_risk) / Decimal(100.0)
    P = Decimal(pool_at_start)
    A = abs(Decimal(amount_buy_simple))
    S = Decimal(shares_buy)
    T = Decimal(tax_buy) / Decimal(100.0)
    C = Decimal(commission_buy)
    return ((R * P - A) - C) / (S * (T - 1))

def calculate_profit_loss(self, price_buy, shares_buy, price_sell, shares_sell):
    """
        Calculates the profit_loss.
    """
    #NOTE: amount_sell_simple - amount_buy_simple
    #NOTE: So - Bo
    Bo = Decimal(price_buy) * Decimal(shares_buy)
    So = Decimal(price_sell) * Decimal(shares_sell)
    return = So - Bo

def calculate_risk_input(self, i_pool, i_risk):
    """
        Calculates the risk based on total pool and input.
        Consider this the theoretical risk we want to take.
    """
    #NOTE: (i_risk/100.0) * pool_at_start
    #NOTE: R * Po
    R = Decimal(i_risk)/Decimal(100.0)
    Po = abs(Decimal(i_pool))
    return R * Po

def calculate_risk_initial(self, price_buy, shares_buy, stoploss):
    """
        Calculates the initial risk.
        This is the risk we will take if our stoploss is reached.
        This should be equal to the risk_input if everything was
        correctly calculated.
    """
    #NOTE: commission + tax = seperate = costs
    return (price_buy * shares_buy) - (stoploss * shares_buy)

def calculate_risk_actual(self, price_buy, shares_buy, price_sell, shares_sell, stoploss, risk_initial):
    """
        Calculates the risk we actually took,
        based on the data in TABLE_TRADE.
    """
    #NOTE: price_sell > stoploss = max risk was the initial risk
    if Ps < stoploss:
        result = (price_buy * shares_buy) - (price_sell * shares_sell)
    else:
        result = risk_initial
    return result

def calculate_cost_total(self, tax_buy, commission_buy, tax_sell, commission_sell):
    """
        Returns the total costs associated with the given trade.
    """
    return (tax_buy + commission_buy + tax_sell + commission_sell)

def calculate_commission(self):
    """
        Calculation for T_RATE.
    """
    #TODO: finish this function
    return DEFAULT_DECIMAL

def calculate_r_multiple(self, price_buy, price_sell, stoploss):
    """ 
        Function to calculate R-multiple.
    """
    return (price_sell - price_buy)/(price_buy - stoploss)
