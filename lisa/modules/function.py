"""
    See LICENSE file for copyright and license details.
"""

"""
    A file with Lisa specific functions that can be used everywhere
"""

from modules.constant import INVESTMENT, TRADING_ACCOUNTS

def is_a_trade(account_to):
    """
        Function to determine if a line to process, is a trade.
    """
    result = False
    for value in TRADING_ACCOUNTS:
        if value.lower() in account_to:
            result = True
            break
    return result

def is_an_investment(account_to):
    """
        Function to determine if a line to process, is an investent (buy
        or sell of stock, that's not a trade).
    """
    # Check if it's an invenstment activity
    result = False
    for value in INVESTMENT:
        if value.lower() in account_to:
            result = True
            break
    # That is NOT a trade
    for value in TRADING_ACCOUNTS:
        if value.lower() in account_to:
            result = False
            break
    return result
    
def is_negative_amount(account_name):
    """
        Check if the amount we enter should be positive or negative.
        Rules:
        Debit all expenses and losses, credit all incomes and gains
        Debit all assets, credit all liabilities
        Debit the receiver, credit the giver
    """
    result = False
    for name in NEGATIVES:
        if name.lower() in account_name.lower():
            result = True
            break;
    return result

def deals_with_stocks(account_to):
    """
        See if we need to use rate, marketid and stockid.
    """
    #TODO: fix this function with the new way of working
    return (is_a_trade(account_to) or
            is_an_investment(account_to))

def is_a_table(key):
    """
        Used to ignore all dictionary entries that don't start with t_
    """
    return key.lower().startswith('t_')

def we_are_buying(account_to):
    """
        Are we buying?
    """
    #TODO: fix this
    result = True
