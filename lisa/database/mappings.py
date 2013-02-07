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
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from meta import Base

class T_FINANCE(Base):
    """ T_FINANCE """
    __tablename__ = TABLE_FINANCE
    #__table_args__ = {'autoload':True}
    #TODO: finish this code for all classes...
    #NOTE: autoload gives less control and I don't know
    #how to make session.add_all() to work with it.
    finance_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    account_id = Column(Integer)
    category_id = Column(Integer)
    subcategory_id = Column(Integer)
    amount = Column(Numeric(18,6))
    comment = Column(String(256))
    stock_name_id = Column(Integer)
    shares = Column(Integer)
    price = Column(Numeric(18,6))
    tax = Column(Numeric(18,6))
    commission = Column(Numeric(18,6))
    active = Column(Integer)
    rate_id = Column(Integer)
    currency_exchange_id = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime) 

    def __init__(self, finance_id, date, year, month, day, account_id, category_id,
            subcategory_id, amount, comment, stock_name_id, shares, price, tax,
            commission, active, rate_id, currency_exchange_id, date_created, date_modified):
        self.finance_id = finance_id
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.account_id = account_id
        self.category_id = category_id
        self.subcategory_id = subcategory_id
        self.amount = amount
        self.comment = comment
        self.stock_name_id = stock_name_id
        self.shares = shares
        self.price = price
        self.tax = tax
        self.commission = commission
        self.active = active
        self.rate_id = rate_id
        self.currency_exchange_id = currency_exchange_id
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s')>" % (
            self.finance_id, self.date, self.year, self.month, self.day, self.account_id,
            self.category_id, self.subcategory_id, self.amount, self.comment,
            self.stock_name_id, self.shares, self.price, self.tax,
            self.commission, self.active, self.rate_id,
            self.currency_exchange_id, self.date_created, self.date_modified)

class T_INVESTMENT(Base):
    """ T_INVESTMENT """
    __tablename__ = TABLE_INVESTMENT
    #__table_args__ = {'autoload':True}
    investment_id = Column(Integer, primary_key=True)
    stock_name_id = Column(Integer)
    action = Column(String(50))
    price = Column(Numeric(18,6))
    shares = Column(Integer)
    tax = Column(Numeric(18,6))
    commission = Column(Numeric(18,6))
    historical = Column(Numeric(18,6))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)
    risk = Column(Numeric(18,6))

    def __init__(self, investment_id, stock_name_id, action, price, shares, tax,
            commission, historical, active, date_created, date_modified, risk):
        self.investment_id = investment_id
        self.stock_name_id = stock_name_id
        self.action = action
        self.price = price
        self.shares = shares
        self.tax = tax
        self.commission = commission
        self.historical = historical
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified
        self.risk = risk

    def __repr__(self):
        return "<T_STOCK('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.investment_id, self.stock_name_id, self.action, self.price, self.shares, self.tax, self.commission, self.historical, self.active, self.date_created, self.date_modified, self.risk)

class T_STOCK_NAME(Base):
    """ T_STOCK_NAME """
    __tablename__ = TABLE_STOCK_NAME
    #__table_args__ = {'autoload':True}
    stock_name_id = Column(Integer, primary_key=True)
    name = Column(String(15))
    market_id = Column(Integer)
    description = Column(String(256))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, stock_name_id, name, market_id, description, active, date_created, date_modified):
        self.stock_name_id = stock_name_id
        self.name = name
        self.market_id = market_id
        self.description = description
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_STOCK_NAME('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.stock_name_id, self.name,
                self.market_id, self.description, active, self.date_created, self.date_modified)

class T_MARKET(Base):
    """ T_MARKET """
    __tablename__ = TABLE_MARKET
    #__table_args__ = {'autoload':True}
    market_id = Column(Integer, primary_key=True)
    code = Column(String(5))
    name = Column(String(30))
    country = Column(String(3))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, market_id, code, name, country, active, date_created, date_modified):
        self.market_id = market_id
        self.code = code
        self.name = name
        self.country = country
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_MARKET('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.market_id, self.code, self.name, self.country, self.active, self.date_created, self.date_modified)

class T_CATEGORY(Base):
    """ T_CATEGORY """
    __tablename__ = TABLE_CATEGORY
    #__table_args__ = {'autoload':True}
    category_id = Column(Integer, primary_key=True)
    name = Column(String(30))
    flg_income = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, category_id, name, flg_income, active, date_created, date_modified):
        self.category_id = category_id
        self.name = name
        self.flg_income = flg_income
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_CATEGORY('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.category_id,
                self.name, self.flg_income, self.active, self.date_created, self.date_modified)

class T_MARGIN(Base):
    """ T_MARGIN """
    __tablename__ = TABLE_MARGIN
    #__table_args__ = {'autoload':True}
    margin_id = Column(Integer, primary_key=True)
    margin_type_id = Column(Integer)
    description = Column(String(256))
    value = Column(Numeric(18,6))
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, margin_id, margin_type_id, description, value, date_created, date_modified):
        self.margin_id = margin_id
        self.margin_type_id = margin_type_id
        self.description = description
        self.value = value
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_MARGIN('%s', '%s', '%s', '%s' ,'%s', '%s')>" % (self.margin_id, self.margin_type_id,
                self.description, self.value, self.date_created, self.date_modified)

class T_MARGIN_TYPE(Base):
    """ T_MARGIN_TYPE """
    __tablename__ = TABLE_MARGIN_TYPE
    #__table_args__ = {'autoload':True}
    margin_type_id = Column(Integer, primary_key=True)
    margin_type = Column(String(50))

    def __init__(self, margin_type_id, margin_type):
        self.margin_type_id = margin_type_id
        self.margin_type = margin_type

    def __repr__(self):
        return "<T_MARGIN_TYPE('%s', '%s')>" % (self.margin_type_id, self.margin_type)

class T_SUBCATEGORY(Base):
    """ T_SUBCATEGORY """
    __tablename__ = TABLE_SUBCATEGORY
    #__table_args__ = {'autoload':True}
    subcategory_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, subcategory_id, name, active, date_created, date_modified):
        self.subcategory_id = subcategory_id
        self.name = name
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_SUBCATEGORY('%s', '%s', '%s', '%s', '%s')>" % (self.subcategory_id, self.name,
                self.active, self.date_created, self.date_modified)

class T_ACCOUNT(Base):
    """ T_ACCOUNT """
    __tablename__ = TABLE_ACCOUNT
    #__table_args__ = {'autoload':True}
    account_id = Column(Integer, primary_key=True)
    name = Column(String(6))
    description = Column(String(256))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, account_id, name, description, active, date_created, date_modified):
        self.account_id = account_id
        self.name = name
        self.description = description
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_ACCOUNT('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.account_id, self.name,
                self.description, self.active, self.date_created, self.date_modified)

class T_CURRENCY(Base):
    """ T_CURRENCY """
    __tablename__ = TABLE_CURRENCY
    #__table_args__ = {'autoload':True}
    currency_id = Column(Integer, primary_key=True)
    code = Column(String(3))
    description = Column(String(256))

    def __init__(self, currency_id, code, description):
        self.currency_id = currency_id
        self.code = code
        self.description = description

    def __repr__(self):
        return "<T_CURRENCY('%s', '%s', '%s')>" % (self.currency_id, self.code, self.description)

class T_CURRENCY_EXCHANGE(Base):
    """ T_CURRENCY_EXCHANGE """
    __tablename__ = TABLE_CURRENCY_EXCHANGE
    #__table_args__ = {'autoload':True}
    currency_exchange_id = Column(Integer, primary_key=True)
    from_currency_id = Column(Integer)
    to_currency_id = Column(Integer)
    exchange_rate = Column(Numeric(18,6))
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, currency_exchange_id, from_currency_id,
            to_currency_id, exchange_rate, date_created, date_modified):
        self.currency_exchange_id = currency_exchange_id
        self.from_currency_id = from_currency_id
        self.to_currency_id = to_currency_id
        self.exchange_rate = exchange_rate
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_CURRENCY_EXCHANGE('%s', '%s', '%s', '%s', '%s')>" % (
                self.currency_exchange_id,
                self.from_currency_id,
                self.to_currency_id,
                self.exchange_rate,
                self.date_created,
                self.date_modified)

class T_FORMULA(Base):
    """ T_FORMULA """
    __tablename__ = TABLE_FORMULA
    #__table_args__ = {'autoload':True}
    formula_id = Column(Integer, primary_key=True)
    value = Column(String(512))
    description = Column(String(256))

    def __init__(self, formula_id, value, description):
        self.formula_id = formula_id
        self.value = value
        self.description = description

    def __repr__(self):
        return "<T_FORMULA('%s', '%s', '%s')>" % (self.formula_id,
                self.value, self.description)

class T_TRADE(Base):
    """ T_TRADE """
    __tablename__ = TABLE_TRADE
    #__table_args__ = {'autoload':True}
    trade_id = Column(Integer, primary_key=True)
    market_id = Column(Integer)
    stock_name_id = Column(Integer)
    date_buy = Column(DateTime)
    year_buy = Column(Integer)
    month_buy = Column(Integer)
    day_buy = Column(Integer)
    date_sell = Column(DateTime)
    year_sell = Column(Integer)
    month_sell = Column(Integer)
    day_sell = Column(Integer)
    long_flag = Column(Integer)
    price_buy = Column(Numeric(18,6))
    price_sell = Column(Numeric(18,6))
    shares_buy = Column(Integer)
    shares_sell = Column(Integer)
    commission_buy = Column(Numeric(18,6))
    commission_sell = Column(Numeric(18,6))
    tax_buy = Column(Numeric(18,6))
    tax_sell = Column(Numeric(18,6))
    risk = Column(Numeric(18,6))
    initial_risk = Column(Numeric(18,6))
    initial_risk_percent = Column(Numeric(18,6))
    stoploss = Column(Numeric(18,6))
    profit_loss = Column(Numeric(18,6))
    profit_loss_percent = Column(Numeric(18,6))
    r_multiple = Column(Numeric(18,6))
    win_flag = Column(Integer)
    at_work = Column(Numeric(18,6))
    id_buy = Column(Integer)
    id_sell = Column(Integer)
    currency_exchange_id = Column(Integer)
    drawdown_id = Column(Integer)
    pool_trading_at_start = Column(Numeric(18,6))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)   

    def __init__(self, trade_id, market_id, stock_name_id, date_buy, year_buy, month_buy,
            day_buy, date_sell, year_sell, month_sell, day_sell, long_flag,
            price_buy, price_sell, shares_buy, shares_sell, commission_buy,
            commission_sell, tax_buy, tax_sell, risk, initial_risk,
            initial_risk_percent, stoploss, profit_loss, profit_loss_percent, r_multiple,
            win_flag, at_work, id_buy, id_sell,
            currency_exchange_id, drawdown_id, pool_trading_at_start, active, date_created, date_modified):
        self.trade_id = trade_id
        self.market_id = market_id
        self.stock_name_id = stock_name_id
        self.date_buy = date_buy
        self.year_buy = year_buy
        self.month_buy = month_buy
        self.day_buy = day_buy
        self.date_sell = date_sell
        self.year_sell = year_sell
        self.month_sell = month_sell
        self.day_sell = day_sell
        self.long_flag = long_flag
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.shares_buy = shares_buy
        self.shares_sell = shares_sell
        self.commission_buy = commission_buy
        self.commission_sell = commission_sell
        self.tax_buy = tax_buy
        self.tax_sell = tax_sell
        self.risk = risk
        self.initial_risk = initial_risk
        self.initial_risk_percent = initial_risk_percent
        self.stoploss = stoploss
        self.profit_loss = profit_loss
        self.profit_loss_percent = profit_loss_percent
        self.r_multiple = r_multiple
        self.win_flag = win_flag
        self.at_work = at_work
        self.id_buy = id_buy
        self.id_sell = id_sell
        self.currency_exchange_id = currency_exchange_id
        self.drawdown_id = drawdown_id
        self.pool_trading_at_start = pool_trading_at_start
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_TRADE('%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s')>" % (self.trade_id,
                        self.market_id,
                        self.stock_name_id,
                        self.date_buy,
                        self.year_buy,
                        self.month_buy,
                        self.day_buy,
                        self.date_sell,
                        self.year_sell,
                        self.month_sell,
                        self.day_sell,
                        self.long_flag,
                        self.price_buy,
                        self.price_sell,
                        self.shares_buy,
                        self.shares_sell,
                        self.commission_buy,
                        self.commission_sell,
                        self.tax_buy,
                        self.tax_sell,
                        self.risk,
                        self.initial_risk,
                        self.initial_risk_percent,
                        self.stoploss,
                        self.profit_loss,
                        self.profit_loss_percent,
                        self.r_multiple,
                        self.win_flag,
                        self.at_work,
                        self.id_buy,
                        self.id_sell,
                        self.currency_exchange_id,
                        self.drawdown_id,
                        self.pool_trading_at_start,
                        self.active,
                        self.date_created,
                        self.date_modified)

class T_RATE(Base):
    """ T_RATE """
    __tablename__ = TABLE_RATE
    #__table_args__ = {'autoload':True}
    rate_id = Column(Integer, primary_key=True)
    calculated = Column(Numeric(18,6))
    calculated_percent = Column(Numeric(18,6))
    on_shares = Column(Numeric(18,6))
    on_commission = Column(Numeric(18,6))
    on_ordersize = Column(Numeric(18,6))
    on_other = Column(Numeric(18,6))
    commission = Column(Numeric(18,6))
    tax = Column(Numeric(18,6))
    formula_id = Column(Integer)
    manual_flag = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, rate_id, calculated, calculated_percent,
            on_shares, on_commission, on_ordersize, on_other, commission, tax,
            formula_id, manual_flag, date_created, date_modified):
        self.rate_id = rate_id
        self.calculated = calculated
        self.calculated_percent = calculated_percent
        self.on_shares = on_shares
        self.on_commission = on_commission
        self.on_ordersize = on_ordersize
        self.on_other = on_other
        self.commission = commission
        self.tax = tax
        self.formula_id = formula_id
        self.manual_flag = manual_flag
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_RATE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s')>" % (self.rate_id,
                        self.calculated, self.calculated_percent, self.on_shares,
                        self.on_commission, self.on_ordersize, self.on_other,
                        self.commission, self.tax, self.formula_id,
                        self.manual_flag, self.date_created, self.date_modified)

class T_DRAWDOWN(Base):
    """ T_DRAWDOWN """
    __tablename__ = TABLE_DRAWDOWN
    #__table_args__ = {'autoload':True}
    drawdown_id = Column(Integer, primary_key=True)
    value = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, drawdown_id, value, date_created, date_modified):
        self.drawdown_id = drawdown_id
        self.value = value
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_DRAWDOWN('%s', '%s', '%s', '%s')>" % (self.drawdown_id,
                self.value, self.date_created, self.date_modified)

class T_PARAMETER(Base):
    """ T_PARAMETER """
    __tablename__ = TABLE_PARAMETER
    #__table_args__ = {'autoload':True}
    parameter_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    value = Column(String(512))
    description = Column(String(256))

    def __init__(self, parameter_id, name, value, description):
        self.parameter_id = parameter_id
        self.name = name
        self.value = value
        self.description = description

    def __repr__(self):
        return "<T_PARAMETER('%s', '%s', '%s', '%s')>" % (self.parameter_id, self.name,
                self.value, self.description)
