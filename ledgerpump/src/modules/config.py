#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

import configparser

class ConfigParser():
    """
      Class that contains values from the config file.
    """

    def __init__(self):
        """
          Initialise config class.
        """ 
        self.myconf = 'config/ledgerpump.rc'
        self.dbhost = ''
        self.dbname = ''
        self.dbuser = ''
        self.dbpass = ''
        self.cmd_ledger_to_csv = ''
        self.fmt_ledger_to_csv = ''
        self.cmd_ledger_bin = '/usr/local/bin/ledger'
        self.config()
 
    def config(self):
        """
          Retrieve config file values
        """
        config = configparser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
        self.cmd_ledger_to_csv = config.get('ledger', 'cmd_ledger_to_csv')[1:-1]
        self.fmt_ledger_to_csv = config.get('ledger', 'fmt_ledger_to_csv')[1:-1]
        self.cmd_ledger_bin = config.get('ledger', 'cmd_ledger_bin')[1:-1]
