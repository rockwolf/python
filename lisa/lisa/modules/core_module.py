#!/usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

from database.databaseaccess import DatabaseAccess
from modules.constant import *


class CoreModule():
    """
        All core modules used in Lisa, will inherit from this one.
        This allows for common code to be defined only once.
    """

    def __init__(self, config):
        """
            Initializes the class.
        """
        self.config = config
 
    def write_to_database(self, statements):
        """
            Call to write the statements to the database.
        """
        try:
            dba = DatabaseAccess(self.config)
            dba.write_to_database(statements)
        except Exception as ex:
            print Error.WRITE_TO_DATABASE_CORE, ex
        finally:
            dba = None
