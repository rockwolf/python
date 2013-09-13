#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

import configparser

class ConfigParser():
    """ Class that contains values from the config file. """

    def __init__(self):
        """ Initialise config class. """ 
        self.myconf = 'config/lisa.rc'
        self.dbhost = ''
        self.dbname = ''
        self.dbuser = ''
        self.dbpass = ''
        self.importdir = ''
        self.exportdir = ''
        self.logfile = ''
        self.default_tax = ''
        self.default_risk = ''
        self.default_currency_from = ''
        self.default_currency_to = ''
        self.default_exchange_rate = ''
        self.default_account_from = ''
        self.default_account_to = ''
        self.config()
 
    def config(self):
        """ Retrieve config file values """
        config = configparser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
        self.importdir = config.get('data', 'importdir')[1:-1]
        self.exportdir = config.get('data', 'exportdir')[1:-1]
        self.default_tax = config.get('data', 'default_tax')[1:-1]
        self.default_risk = config.get('data', 'default_risk')[1:-1]
        self.default_currency_from = config.get('data', 'default_currency_from')[1:-1]
        self.default_currency_to = config.get('data', 'default_currency_to')[1:-1]
        self.default_exchange_rate = config.get('data', 'default_exchange_rate')[1:-1]
        self.default_account_from = config.get('data', 'default_account_from')[1:-1]
        self.default_account_to = config.get('data', 'default_account_to')[1:-1]
        self.logfile = config.get('logging', 'logfile')[1:-1]
