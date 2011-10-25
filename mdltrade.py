#! /usr/local/bin/python
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
from time import sleep
import sys
from mdlstock import Stock
from databaseaccess import DatabaseAccess
from decimal import Decimal
from datetime import datetime

class TradeJournal():
    """ Class with methods for a trade journal. """

    def __init__(self, config):
        """ Initializes the class."""
        self.config = config

    def parse_trades(self, fields):
        """ Gather and calculate trade information from the stock related fields. """
        fields_trades = {}
        
        try:
            if fields['object'] == 'buystocks' or fields['object'] == 'sellstocks':
                # trades

                # tid
                # sid
                # year
                # month
                # buy_price
                # sell_price
                # stoploss
                # shares_total
                # closed
                # win_flag
                # drawdown
                # date created and modified
                
                action = ''
                price = '0'
                shares = '0'
                name = fields['stock']
                market = fields['market']
                shares = fields['shares']
                price = fields['price']
                tax = fields['tax']
                commission = fields['commission']
                action = fields['object'] #buystocks/sellstocks
                fields_trades = {
                    'sid' : get_sid_from_name(), # TODO: create this function somewhere
                    'year' : datetime.strftime(fields['date'], '%Y'),
                    'month' : datetime.strftime(fields['date'], '%m'),
                    'name': name,
                    'market': market,
                    'action': action,
                    'shares': shares,
                    'price': price,
                    'tax': tax,
                    'commission': commission,
                }
            else:
                fields_stock = {}
        except Exception as ex:
            print("Error in parse_stocks: ", ex)
        finally:
            return fields_stock
    def process_lines(self, fields_db):
        """ Convert general financial information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_lines(fields_db)
        dba = None
