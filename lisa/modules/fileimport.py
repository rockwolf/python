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
from decimal import Decimal
import csv

from modules.stock import Stock
from modules.trade import TradeJournal
from database.databaseaccess import DatabaseAccess

class FileImport():
    """ Class with methods to import files. """

    def __init__(self, config):
        """ Initializes the class."""
        self.config = config

    def file_import(self):
        """ Parse textfiles and insert data in db. """
        try:
            dba = DataBaseAccess(self.config)
            print(self.config.importfile + ' -> ' + self.config.dbhost + '/' + self.config.dbname + ': ')
            i = 0
            print('[{0}{1}]'.format('  0','%') , end = "")
            importdir = self.config.importdir
            for files in os.walk(importdir):
                for file_ in files:
                    source = open(file_, 'r')
                    # assume first line is header
                    csv_ = csv.DictReader(source, delimiter=';')
                    for row in header:
                        #insert data in table
                        #source.name should be the filename = e.g. T_ACCOUNT
                        #TODO: source.name is a string and not a table
                        #object (I think).
                        table = dba.loaded_objects[source.name]
                        table.insert().values(**row).execute()
                   
                    for line in lines:
                        #TODO: call function to process the line.
                        #with source.name as the tablename.
                        print('test: adding to line.')
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
                finally:
                    dba = None
                    source.close()
            print('')
        except Exception as ex:
            print('')
            print("Error while processing {0}:".format(source.name), ex)
