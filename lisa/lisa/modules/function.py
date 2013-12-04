"""
    See LICENSE file for copyright and license details.
"""

"""
    A file with Lisa specific functions that can be used everywhere
"""

from modules.constant import NEGATIVES
    
def is_negative_amount(account_from):
    """
        Check if the amount we enter should be positive or negative.
    """
    result = False
    # If asset in account_from
    for name in NEGATIVES:
        if name.lower() in account_from.lower():
            result = True
            break;
    return result

def deals_with_stocks(account_from, account_to):
    """
        See if we need to use rate, marketid and stockid.
    """
    return (is_a_trade(account_from, account_to) or
            is_an_investment(account_from, account_to))

def is_a_table(key):
    """
        Used to ignore all dictionary entries that don't start with t_
    """
    return key.lower().startswith('t_')

def we_are_buying(account_from, account_to):
    """
        Are we buying? (not buying == selling)
    """
    #TODO: find a better way to do this
    buy = False
    sell = False
    if (not buy) and (not sell):
        for value in ['whsi00']:
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
        Gets the last part of a <asaparator> seprated string.
    """
    partlist = astring.split(aseparator)
    return partlist[len(partlist) - 1]
