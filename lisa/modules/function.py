"""
    See LICENSE file for copyright and license details.
"""

"""
    A file with Lisa specific functions that can be used everywhere
"""

def is_a_trade(account_name):
    """
        Function to determine if a line to process, is a trade.
    """
    return 'trading' in account_name.lower()

def is_an_investment(account_name):
    """
        Function to determine if a line to process, is an investent (buy
        or sell of stock, that's not a trade).
    """
    #TODO: This also counts for tax and/or commission? Only buy/sell is required?
    return 'investing' in account_name.lower()

def deals_with_stocks(account_name):
    """
        See if we need to use rate, marketid and stockid.
    """
    #TODO: fix this function with the new way of working
    return (is_a_trade(account_name) or
            is_an_investment(account_name))

def is_a_table(key):
    """
        Used to ignore all dictionary entries that don't start with t_
    """
    return key.lower()[0:2] == 't_'

def we_are_buying(account_name):
    """
        Are we buying?
    """
    #TODO: fix this function with the new way of working
    return subcategory == 'buy'

#def build_account_tree(account_list, delimiter):
#    """
#        Returns a set with all unique accounts:
#        Example: input = {'test1', 'test2:test2a:test2a1', 'test3:test3c'}
#        output: result = {'test1'
#            , 'test2'
#            , 'test2:test2a'
#            , 'test2:test2a:test2a1'
#            , 'test3'
#            , 'test3:test3c'}
#    """
#    result = set()
#    print('test123: ', account_list)
#    for longest_account in account_list:
#        result.add(delimiter_tree_values(longest_account, ':'))
#    return result
    
def build_account_tree(delimited_account):
    """
        Turns a <delimiter>-separated string into
        subelements in a tree.
        Example: input = "this:is:an:example"
        with delimiter = ':'
        output: result = {'this'
            , 'this:is'
            , 'this:is:an'
            , 'this:is:an:example'}
    """
    #TODO: remove last : ?
    result = set()
    for index, part in enumerate(delimited_account.split(':')):
        if index == 0:
            account = part
        else:
            account = account + ':' + part
        result.add(account)
    return result
