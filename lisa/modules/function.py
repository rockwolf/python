"""
    See LICENSE file for copyright and license details.
"""

"""
    A file with Lisa specific functions that can be used everywhere
"""

def is_a_trade(category, subcategory):
    """ Function to determine if a line to process, is a trade. """
    return (category == 'trade') \
            and (subcategory == 'buy' or \
            subcategory == 'sell')

def is_an_investment(category, subcategory):
    """ Function to determine if a line to process, is an investent (buy
    or sell of stock, that's not a trade). """
    return (category == 'invest') \
            and (subcategory == 'buy' or \
            subcategory == 'sell')

def deals_with_stocks(category, subcategory):
    """ See if we need to use rate, marketid and stockid. """
    return (is_a_trade(category, subcategory) or
            is_an_investment(category, subcategory))

def is_a_table(key):
    """ Used to ignore all dictionary entries that don't start with t_ """
    return key.lower()[0:2] == 't_'

def we_are_buying(subcategory):
    """ Are we buying? """
    return subcategory == 'buy'
