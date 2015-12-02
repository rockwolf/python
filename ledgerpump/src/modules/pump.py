#!/usr/bin/env python

"""
    See LICENSE.txt file for copyright and license details.
"""

#from decimal import Decimal
#import sys
#from subprocess import call

class Pump():
    """
      Methods related to pumping ledger data to the database.
    """
  def __init__(self):
      """
          Init
      """
      pass
  
  def ledger_to_csv(self, a_file):
      """
          Export ledger data to csv.
      """
      # TODO: get output file (tmp)
      # TODO: export data (ledger command in config)
      pass
      
  def csv_to_db(self, a_csv):
     """
        Read csv-file and write the data to the database.
        The csv-file must be in the correct format.
        The database tables must exits.
      """
      # TODO: get database connection info from config
      # TODO: connect to database
      # TODO: check if csv is in correct format
      # TODO: write nice output somewhere?
      pass
