#!/usr/env/python
"""
Author: Andy Nagels
Date: 2010-08-24
Lisa: Less Interaction Saves Action
A frontend for a database to store financial transactions in a convenient way.

Copyright (C) 2010 Andy Nagels

This file is part of Lisa.

Lisa is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lisa is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Lisa. If not, see <http://www.gnu.org/licenses/>.
					
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
                + config.dbname
                ,echo=False
            )
config = None
Base = declarative_base(engine)
