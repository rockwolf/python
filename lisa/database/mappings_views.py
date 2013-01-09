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
from sqlalchemy import Column, Integer
from meta import Base

class V_FINANCE(Base):
    """ V_FINANCE """
    __tablename__ = VIEW_FINANCE
    __table_args__ = {'autoload':True}
    #TODO: figure out how to specify that finance_id can be used
    #as a primary key

class V_INVESTMENT(Base):
    """ V_INVESTMENT """
    __tablename__ = VIEW_INVESTMENT
    __table_args__ = {'autoload':True}

class V_STOCK_NAME(Base):
    """ V_STOCK_NAME """
    __tablename__ = VIEW_STOCK_NAME
    __table_args__ = {'autoload':True}

class V_MARKET(Base):
    """ V_MARKET """
    __tablename__ = VIEW_MARKET
    __table_args__ = {'autoload':True}

class V_CATEGORY(Base):
    """ V_CATEGORY """
    __tablename__ = VIEW_CATEGORY
    __table_args__ = {'autoload':True}

class V_MARGIN(Base):
    """ V_MARGIN """
    __tablename__ = VIEW_MARGIN
    __table_args__ = {'autoload':True}

class V_MARGIN_TYPE(Base):
    """ V_MARGIN_TYPE """
    __tablename__ = VIEW_MARGIN_TYPE
    __table_args__ = {'autoload':True}

class V_SUBCATEGORY(Base):
    """ V_SUBCATEGORY """
    __tablename__ = VIEW_SUBCATEGORY
    __table_args__ = {'autoload':True}

class V_ACCOUNT(Base):
    """ V_ACCOUNT """
    __tablename__ = VIEW_ACCOUNT
    __table_args__ = {'autoload':True}

class V_CURRENCY(Base):
    """ V_CURRENCY """
    __tablename__ = VIEW_CURRENCY
    __table_args__ = {'autoload':True}

class V_CURRENCY_EXCHANGE(Base):
    """ V_CURRENCY_EXCHANGE """
    __tablename__ = VIEW_CURRENCY_EXCHANGE
    __table_args__ = {'autoload':True}

class V_FORMULA(Base):
    """ V_FORMULA """
    __tablename__ = VIEW_FORMULA
    __table_args__ = {'autoload':True}

class V_TRADE(Base):
    """ V_TRADE """
    __tablename__ = VIEW_TRADE
    __table_args__ = {'autoload':True}

class V_RATE(Base):
    """ V_RATE """
    __tablename__ = VIEW_RATE
    __table_args__ = {'autoload':True}

class V_DRAWDOWN(Base):
    """ V_DRAWDOWN """
    __tablename__ = VIEW_DRAWDOWN
    __table_args__ = {'autoload':True}

class V_PARAMETER(Base):
    """ V_PARAMETER """
    __tablename__ = VIEW_PARAMETER
    __table_args__ = {'autoload':True}
