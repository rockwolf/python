#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
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
            importdir = self.config.importdir
            print importdir + ' -> ' + self.config.dbhost + '/' + self.config.dbname + ': '
            for root, dirs, files in os.walk(importdir):
                try:
                    for filename in files:
                        print 'Importing table', filename + ':' #, end = ' ' # end code from python3
                        source = open(os.path.join(importdir, root[len(importdir):], filename), 'r')
                        # assume first line is header
                        csv_ = csv.DictReader(source, delimiter=',')
                        i = 0 
                        for row in csv_:
                            #insert data in table
                            #source.name should be the filename = e.g. T_ACCOUNT
                            table = dba.loaded_objects[filename]
                            table.insert().values(**row).execute()
                            i = i + 1
                        sys.stdout.flush()
                        sleep(0.001)
                        print str(i), 'rows imported...' #, end = ' ' # end code from python3
                        print '[OK]'
                except Exception as ex:
                    print '[Error!]'
                    print "Error in for loop: ", ex
                    break
                finally:
                    source.close()
            print ''
        except Exception as ex:
            print ''
            print "Error in file_import:", ex
        finally:
            dba = None
