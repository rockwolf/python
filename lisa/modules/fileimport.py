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
import os
from decimal import Decimal
import csv

from database.databaseaccess import DatabaseAccess

class FileImport():
    """ Class with methods to import files. """

    def __init__(self, config):
        """ Initializes the class."""
        self.config = config

    def file_import(self):
        """ Parse textfiles and insert data in db. """
        try:
            dba = DatabaseAccess(self.config)
            i = 0 
            print('[{0}{1}]'.format('  0','%'), end = '')
            importdir = self.config.importdir
            print(importdir + ' -> ' + self.config.dbhost + '/' + self.config.dbname + ': ')
            for root, dirs, files in os.walk(importdir):
                try:
                    for filename in files:
                        source = open(os.path.join(importdir, root[len(importdir):], filename), 'r')
                        # assume first line is header
                        csv_ = csv.DictReader(source, delimiter=',')
                        for row in csv_:
                            #insert data in table
                            #source.name should be the filename = e.g. T_ACCOUNT
                            table = dba.loaded_objects[source.name]
                            table.insert().values(**row).execute()
                    
                        #for line in lines:
                            #TODO: call function to process the line.
                            #with source.name as the tablename.
                        #    print('test: adding to line.')
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
                    source.close()
            print('')
        except Exception as ex:
            print('')
            print("Error in file_import:", ex)
        finally:
            dba = None
