"""
    See LICENSE file for copyright and license details.
"""

"""
    A file with Lisa specific functions that can be used everywhere
"""

from modules.constant import NEGATIVES, TRADING_ACCOUNTS

def is_a_trading_account(account):
    """
        Check if the given account is a broker (used for trading).
    """
    return (account in TRADING_ACCOUNTS)
    
def is_negative_amount(account_from):
    """
        Check if the amount we enter should be positive or negative.
    """
    result = False
    # Note: the below translates to:
    # if 'asset' in account_from
    for name in NEGATIVES:
        if name.upper() in account_from.upper():
            result = True
            break;
    return result

def deals_with_commodities(account_from, account_to = ''):
    """
        Check if we are using commoditie-related text in 
        one of the account names.
    """
    test1 = ':commodities'
    test2 = ':cfd'
    return ((test1 in account_from or test1 in  account_to) or (test2 in account_from or test2 in account_to))

def is_a_table(key):
    """
        Used to ignore all dictionary entries that don't start with T_
    """
    return key.upper().startswith('T_')

def we_are_buying(account_from, account_to):
    """
        Are we buying? (not buying == selling)
    """
    buy = False
    sell = False
    for value in TRADING_ACCOUNTS:
        if (value.lower() in account_from):
            buy = True
            sell = False
        elif (value.lower() in account_to):
            buy = False
            sell = True
    return buy

def combine_sets(a_set):
    """
        Combine sets into a list.
        input: [{'test1', 'test2'}, {'test2'}]
        output: ['test1', 'test2']
    """
    combined = set()
    for item in a_set:
        combined = combined | item
    return list(combined)
    
def get_last_part(astring, aseparator):
    """
        Gets the last part of an <asaparator> seprated string.
    """
    partlist = astring.split(aseparator)
    return partlist[len(partlist) - 1]
