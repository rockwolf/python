"""
    See LICENSE file for copyright and license details.
"""

"""
    A file with Lisa specific functions that can be used everywhere
"""

from modules.constant import INVESTMENT, TRADING_ACCOUNTS, NEGATIVES, BETTING_ACCOUNTS, INVESTING_ACCOUNTS

def is_a_trade(account_from, account_to):
    """
        Function to determine if a line to process, is a trade.
    """
    result = False
    for value in TRADING_ACCOUNTS:
        if (value.lower() in account_from) \
            or (value.lower() in account_to):
            result = True
            break
    return result

def is_an_investment(account_from, account_to):
    """
        Function to determine if a line to process, is an investent (buy
        or sell of stock, that's not a trade).
    """
    # Check if it's an invenstment activity
    result = False
    for value in INVESTMENT:
        if (value.lower() in account_from) \
            or (value.lower() in account_to):
            result = True
            break
    # That is NOT a trade
    # NOTE: having the same trading and investing account is not allowed!
    for value in TRADING_ACCOUNTS:
        if (value.lower() in account_from) \
            or (value.lower() in account_to):
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

def deals_with_stocks(account_from, account_to):
    """
        See if we need to use rate, marketid and stockid.
    """
    return (is_a_trade(account_from, account_to) or
            is_an_investment(account_from, account_to))
            
def is_a_bet(account_from, account_to):
    """
        See if we are dealing with a betting transaction.
    """
    result = False
    for value in BETTING_ACCOUNTS:
        if (value.lower() in account_from) \
            or (value.lower() in account_to):
            result = True
            break
    return result

def is_a_table(key):
    """
        Used to ignore all dictionary entries that don't start with t_
    """
    return key.lower().startswith('t_')

def we_are_buying(account_from, account_to):
    """
        Are we buying? (not buying == selling)
    """
    for value in INVESTING_ACCOUNTS:
        if (value.lower() in account_from):
            buy = True
            sell = False
        elif (value.lower() in account_to):
            buy = False
            sell = True
    if (not buy) and (not sell):
        for value in TRADING_ACCOUNTS:
            if (value.lower() in account_from):
                buy = True
                sell = False
            elif (value.lower() in account_to):
                buy = False
                sell = True
    return buy
