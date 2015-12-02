#!/usr/bin/env python

"""
    See LICENSE.txt file for copyright and license details.
"""

#from decimal import Decimal
import sys
from subprocess import call
from modules.config import ConfigParser

class Pump():
    """
      Methods related to pumping ledger data to the database.
    """
  def __init__(self, a_config):
      """
          Init
      """
      self.config = a_config
  
  def ledger_to_csv(self, a_file):
      """
          Export ledger data to csv.
      """
      # TODO: get output file (tmp)
      # TODO: export data (ledger command in config)
      l_csv = ''
      #l_csv = Tempfile.new('ledger')
      print "Dumping ledger [{0}] to file [{1}]...".format(a_file, l_csv)
      #system "#{ledger_bin_path} -f #{ledger_file} --format='#{ledger_format}' reg > #{file.path}"
      call([self.config.cmd_ledger_to_csv.format(self.config.cmd_ledger_bin, a_file, self.config.fmt_ledger_to_csv, l_csv)])
      #replaced_file = Tempfile.new('ledger')
      #replaced_file.write(file.read.gsub('\"', '""'))
      #replaced_file.flush
      print "Done."
      
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
