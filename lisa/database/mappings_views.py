#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

from modules.constant import *
from sqlalchemy import Column, Integer, String
from meta import Base

class V_FINANCE(Base):
    """ V_FINANCE """
    __tablename__ = View.FINANCE
    __table_args__ = {'autoload':True}
    finance_id = Column('finance_id', Integer, primary_key=True)

class V_INVESTMENT(Base):
    """ V_INVESTMENT """
    __tablename__ = View.INVESTMENT
    __table_args__ = {'autoload':True}
    investment_id = Column('investment_id', Integer, primary_key=True)

class V_STOCK_NAME(Base):
    """ V_STOCK_NAME """
    __tablename__ = View.STOCK_NAME
    __table_args__ = {'autoload':True}
    stock_name_id = Column('stock_name_id', Integer, primary_key=True)

class V_MARKET(Base):
    """ V_MARKET """
    __tablename__ = View.MARKET
    __table_args__ = {'autoload':True}
    market_id = Column('market_id', Integer, primary_key=True)

class V_MARGIN(Base):
    """ V_MARGIN """
    __tablename__ = View.MARGIN
    __table_args__ = {'autoload':True}
    margin_id = Column('margin_id', Integer, primary_key=True)

class V_MARGIN_TYPE(Base):
    """ V_MARGIN_TYPE """
    __tablename__ = View.MARGIN_TYPE
    __table_args__ = {'autoload':True}
    margin_type_id = Column('margin_type_id', Integer, primary_key=True)

class V_ACCOUNT(Base):
    """ V_ACCOUNT """
    __tablename__ = View.ACCOUNT
    __table_args__ = {'autoload':True}
    account_id = Column('account_id', Integer, primary_key=True)

class V_CURRENCY(Base):
    """ V_CURRENCY """
    __tablename__ = View.CURRENCY
    __table_args__ = {'autoload':True}
    currency_id = Column('currency_id', Integer, primary_key=True)

class V_CURRENCY_EXCHANGE(Base):
    """ V_CURRENCY_EXCHANGE """
    __tablename__ = View.CURRENCY_EXCHANGE
    __table_args__ = {'autoload':True}
    currency_exchange_id = Column('currency_exchange_id', Integer, primary_key=True)

class V_FORMULA(Base):
    """ V_FORMULA """
    __tablename__ = View.FORMULA
    __table_args__ = {'autoload':True}
    formula_id = Column('formula_id', Integer, primary_key=True)

class V_TRADE(Base):
    """ V_TRADE """
    __tablename__ = View.TRADE
    __table_args__ = {'autoload':True}
    trade_id = Column('trade_id', Integer, primary_key=True)

class V_RATE(Base):
    """ V_RATE """
    __tablename__ = View.RATE
    __table_args__ = {'autoload':True}
    rate_id = Column('rate_id', Integer, primary_key=True)

class V_DRAWDOWN(Base):
    """ V_DRAWDOWN """
    __tablename__ = View.DRAWDOWN
    __table_args__ = {'autoload':True}
    drawdown_id = Column('drawdown_id', Integer, primary_key=True)

class V_PARAMETER(Base):
    """ V_PARAMETER """
    __tablename__ = View.PARAMETER
    __table_args__ = {'autoload':True}
    parameter_id = Column('parameter_id', Integer, primary_key=True)
 
class V_REP_CHECK_TOTAL(Base):
    """ V_REP_CHECK_TOTAL """
    __tablename__ = View.REP_CHECK_TOTAL
    __table_args__ = {'autoload':True}
    account_name = Column('account_name', String(6) , primary_key=True)

class V_POOL(Base):
    """ V_POOL """
    __tablename__ = View.POOL
    __table_args__ = {'autoload':True}
    pool_id = Column('pool_id', Integer, primary_key=True)

class V_ACCOUNT_NAME(Base):
    """ V_ACCOUNT_NAME """
    __tablename__ = View.ACCOUNT_NAME
    __table_args__ = {'autoload':True}
    pool_id = Column('account_id', Integer, primary_key=True)
    
class V_EXPECTANCY(Base):
    """ V_EXPECTANCY """
    __tablename__ = View.EXPECTANCY
    __table_args__ = {'autoload':True}
    expectancy = Column('expectancy', Decimal(18,6), primary_key=True)
