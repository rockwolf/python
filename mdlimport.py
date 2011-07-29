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

class FileImport():
    """ Class with methods to import files. """

    def __init__(self, config):
        """ Initializes the class."""
        self.config = config

    def file_import(self):
        """ Parse textfile and insert data in db. """
        try:
            source = open(self.config.importfile)
            lines = source.readlines()
            fields = {}
            fields_db = []
            
            print(self.config.importfile + ' -> ' + self.config.dbhost + '/' + self.config.dbname + ': ')
            
            i = 0
            print('[{0}{1}]'.format('  0','%') , end = "")
            for line in lines:
                try:
                    fields = line.strip().split(':')
                    fields_db.append({
                        'date':fields[0],
                        'account':fields[1], #Note: Get AID from T_ACCOUNT for final insert
                        'product':fields[2], #Note: Get PID from T_PRODUCT for final insert
                        'object':fields[3], #Note: Get OID from T_OBJECT for final insert
                        'amount':fields[4],
                        'comment':fields[5]
                        #.replace('\'','\\\'')
                    })
                    i = i + 1
                    percent = int(i/len(lines)*100)
                    percentlen = len(str(percent))-1

                    #[  1%]
                    #[123%]
                    #123456
                    print(6*'\b', end = "")

                    print('[{0}{1}]'.format((3-percentlen-1)*' ' + str(percent),'%') , end = "")
                    sleep(0.001)
                    sys.stdout.flush()
                except Exception as ex:
                    print("Error in for loop: ", ex)
                    break
            print('')
            self.process_lines(fields_db)
            self.process_comments(fields_db)
        except Exception as ex:
            print('')
            print("Error while processing {0}:".format(self.config.importfile), ex)
        finally:
            source.close()
            exit(1)
                
    def process_comments(self, fields_db):
        """ Processing lines of the input file. """
        # stocks
        fields_comment_stocks = []
        try:
            stock = Stock(self.config) 
            for field in fields_db:
                fields_comment_stocks.append(stock.parse_comment_stocks(field))
            cmnt = fields_comment_stocks
            if cmnt != {}:
                stock.process_stocks(fields_db, fields_comment_stocks)
        except Exception as ex:
            print("Error in process_comments: ", ex)
        finally:
            stock = None

    def process_lines(self, fields_db):
        """ Convert general financial information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_lines(fields_db)
        dba = None
