"""
This file is part of Lisa.

Lisa is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lisa is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Lisa. If not, see <http://www.gnu.org/licenses/>.
"""

""" A file with Lisa specific functions that can be used everywhere """

def is_a_trade(category, subcategory):
    """ Function to determine if a line to process, is a trade. """
    return (category == 'trade.tx' or \
            category == 'trade.rx') \
            and (subcategory == 'buy' or \
            subcategory == 'sell')

def is_an_investment(category, subcategory):
    """ Function to determine if a line to process, is an investent (buy
    or sell of stock, that's not a trade). """
    return (category == 'invest.tx' or \
            category == 'invest.rx') \
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
    """ Are we buying or selling? """
    #TODO: what if subcat is something different as buy or sell?
    return if subcategory == 'buy': True else: False
