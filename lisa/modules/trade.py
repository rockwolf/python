#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

from datetime import datetime
from database.databaseaccess import DatabaseAccess

class Trade():
    """
        Trade class.
    """

    def __init__(self, config):
        """
            Initializes the class.
        """
        self.config = config
