#! /usr/local/bin/python
"""
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
from modules.constant import *

class T_FINANCE(Base):
    """ T_FINANCE """
    __tablename__ = TABLE_FINANCE
    __table_args__ = {'autoload':True}

class T_INVESTMENT(Base):
    """ T_INVESTMENT """
    __tablename__ = TABLE_INVESTMENT
    __table_args__ = {'autoload':True}

class T_STOCK_NAME(Base):
    """ T_STOCK_NAME """
    __tablename__ = TABLE_STOCK_NAME
    __table_args__ = {'autoload':True}

class T_MARKET(Base):
    """ T_MARKET """
    __tablename__ = TABLE_MARKET
    __table_args__ = {'autoload':True}

class T_CATEGORY(Base):
    """ T_CATEGORY """
    __tablename__ = TABLE_CATEGORY
    __table_args__ = {'autoload':True}

class T_MARGIN(Base):
    """ T_MARGIN """
    __tablename__ = TABLE_MARGIN
    __table_args__ = {'autoload':True}

class T_MARGIN_TYPE(Base):
    """ T_MARGIN_TYPE """
    __tablename__ = TABLE_MARGIN_TYPE
    __table_args__ = {'autoload':True}

class T_SUBCATEGORY(Base):
    """ T_SUBCATEGORY """
    __tablename__ = TABLE_SUBCATEGORY
    __table_args__ = {'autoload':True}

class T_ACCOUNT(Base):
    """ T_ACCOUNT """
    __tablename__ = TABLE_ACCOUNT
    __table_args__ = {'autoload':True}

class T_CURRENCY(Base):
    """ T_CURRENCY """
    __tablename__ = TABLE_CURRENCY
    __table_args__ = {'autoload':True}

class T_CURRENCY_EXCHANGE(Base):
    """ T_CURRENCY_EXCHANGE """
    __tablename__ = TABLE_CURRENCY_EXCHANGE
    __table_args__ = {'autoload':True}

class T_FORMULA(Base):
    """ T_FORMULA """
    __tablename__ = TABLE_FORMULA
    __table_args__ = {'autoload':True}

class T_TRADE(Base):
    """ T_TRADE """
    __tablename__ = TABLE_TRADE
    __table_args__ = {'autoload':True}

class T_RATE(Base):
    """ T_RATE """
    __tablename__ = TABLE_RATE
    __table_args__ = {'autoload':True}

class T_DRAWDOWN(Base):
    """ T_DRAWDOWN """
    __tablename__ = TABLE_DRAWDOWN
    __table_args__ = {'autoload':True}

class T_PARAMETER(Base):
    """ T_PARAMETER """
    __tablename__ = TABLE_PARAMETER
    __table_args__ = {'autoload':True}
