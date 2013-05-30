#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from sqlalchemy import Table, MetaData, \
        Column, Integer, or_, and_
from sqlalchemy.types import VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime

from modules.constant import *
from meta import engine, Base
from database.mappings import *
from database.mappings_views import *

class DatabaseAccess():
    """
        Connecting to the database.
    """

    def __init__(self, config):
        """
            Initialize object.
        """
        try:
            self.config = config
            self.Session = sessionmaker(bind=engine)
            self.metadata = Base.metadata
            #self.map_tables()
            #self.map_views()
            self.tables = [x for x in self.metadata.tables.keys() if is_a_table(x) ]
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
   
    def config(self):
        """
            Retrieve config file values.
        """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
        
    def get_latest_drawdown_value(self):
        """
            Retrieve the drawdown value of the last record
            that was added.
        """
        pass
    
    def get_latest_drawdown_id(self):
        """
            Get the drawdown_id of the last record
            that was added.
        """
        pass
        
    def get_drawdown_value(self, drawdown_id):
        """
            Get the drawdown value for the given
            drawdown_id.
        """
        pass
