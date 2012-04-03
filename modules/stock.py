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

from database.databaseaccess import DatabaseAccess

class Stock():
    """ Class with methods regarding stocks. """
    
    def __init__(self, config):
        """ Initializes the class. """
        self.config = config

    def process_stocks(self, fields_db, fields_stock):
        """ Import stock information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_stocks(fields_db, fields_stock)
        dba = None

    def parse_stocks(self, fields):
        """ Gather the stock information from the stock related fields. """
        try:
            if fields['object'] == 'buystocks' or fields['object'] == 'sellstocks':
                # stocks
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
                #print 'test: action =' + action
                fields_stock= {
                    'name': name,
                    'market': market,
                    'action': action,
                    'shares': shares,
                    'price': price,
                    'tax': tax,
                    'commission': commission
                }
            else:
                fields_stock = {}
        except Exception as ex:
            print("Error in parse_stocks: ", ex)
        finally:
            return fields_stock
