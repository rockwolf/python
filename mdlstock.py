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

from databaseaccess import DatabaseAccess

class Stock():
    """ Class with methods regarding stocks. """
    
    def __init__(self, config):
        """ Initializes the class. """
        self.config = config

    def process_stocks(self, fields_db, fields_comment_db):
        """ Import stock information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_stocks(fields_db, fields_comment_db)
        dba = None

    def parse_comment_stocks(self, fields):
        """ Convert financial entries that abuse the comment field for stock functionality. """
        fields_comment = []
        fields_comment_db = {}
        
        try:
            if fields['object'] == 'buystocks' or fields['object'] == 'sellstocks':
                # stocks
                name = ''
                market = ''
                action = ''
                price = '0'
                quantity = '0'
                fields_comment = fields['comment'].split(',')
                name = str(fields_comment[0]).split('.')[1]
                market = fields_comment[0].split('.')[0]
                quantity = fields_comment[1]
                price = fields_comment[2]
                action = fields['object'] #buystocks/sellstocks
                #print 'test: action =' + action
                fields_comment_db = {
                    'name': name,
                    'market': market,
                    'action': action,
                    'price': price,
                    'quantity': quantity,
                }
            else:
                fields_comment_db = {}
        except Exception as ex:
            print("Error in parse_comment: ", ex)
        finally:
            return fields_comment_db
