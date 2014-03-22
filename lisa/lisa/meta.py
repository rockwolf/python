#!/usr/env/python
"""
    See LICENSE file for copyright and license details.
"""

from modules.config import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

config = ConfigParser()
engine = create_engine(
                'postgresql://'
                + config.dbuser
                + ':'
                + config.dbpass
                + '@'
                + config.dbhost
                + '/'
                + config.dbname,
                echo=False
            )
config = None
Base = declarative_base(engine)
