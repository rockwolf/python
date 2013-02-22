#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

from database.databaseaccess import DatabaseAccess

class Stock():
    """ Class with methods regarding stocks. """
    
    def __init__(self, config):
        """ Initializes the class. """
        self.config = config
        #TODO: delete this file!
