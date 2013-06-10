#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""

from modules.constant import *
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from meta import Base

class T_FINANCE(Base):
    """ T_FINANCE """
    __tablename__ = Table.FINANCE
    #__table_args__ = {'autoload':True}
    #NOTE: autoload gives less control and I don't know
    #how to make session.add_all() to work with it.
    finance_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    account_id = Column(Integer)
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

    def __init__(self, finance_id, date, year, month, day, account_id,
            amount, comment, stock_name_id, shares, price, tax,
            commission, active, rate_id, currency_exchange_id, date_created, date_modified):
        self.finance_id = finance_id
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.account_id = account_id
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
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.finance_id, self.date, self.year, self.month, self.day, self.account_id,
            self.amount, self.comment, self.stock_name_id, self.shares, self.price,
            self.tax, self.commission, self.active, self.rate_id,
            self.currency_exchange_id, self.date_created, self.date_modified)

class T_INVESTMENT(Base):
    """ T_INVESTMENT """
    __tablename__ = Table.INVESTMENT
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
    risk_input = Column(Numeric(18,6))
    risk_initial = Column(Numeric(18,6))
    risk_initial_percent = Column(Numeric(18,6))
    risk_actual = Column(Numeric(18,6))
    risk_actual_percent = Column(Numeric(18,6))
    cost_total = Column(Numeric(18,6))
    cost_other = Column(Numeric(18,6))
    amount_buy_simple = Column(Numeric(18,6))
    amount_sell_simple = Column(Numeric(18,6))
    stoploss = Column(Numeric(18,6))
    profit_loss = Column(Numeric(18,6))
    profit_loss_percent = Column(Numeric(18,6))
    r_multiple = Column(Numeric(18,6))
    win_flag = Column(Integer)
    id_buy = Column(Integer)
    id_sell = Column(Integer)
    currency_exchange_id = Column(Integer)
    drawdown_id = Column(Integer)
    pool_at_start = Column(Numeric(18,6))
    date_expiration = Column(DateTime)
    expired_flag = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)   

    def __init__(self, trade_id, market_id, stock_name_id, date_buy, year_buy, month_buy,
            day_buy, date_sell, year_sell, month_sell, day_sell, long_flag,
            price_buy, price_sell, shares_buy, shares_sell, commission_buy,
            commission_sell, tax_buy, tax_sell, risk_input, risk_input_percent, risk_initial,
            risk_initial_percent, risk_actual, risk_actual_percent, cost_total, cost_other, 
            amount_buy_simple, amount_sell_simple, stoploss, profit_loss, profit_loss_percent, r_multiple,
            win_flag, id_buy, id_sell,
            currency_exchange_id, drawdown_id, pool_at_start, date_expiration,
            expired_flag, active, date_created, date_modified):
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
        self.risk_input = risk_input
        self.risk_input_percent = risk_input_percent
        self.risk_initial = risk_initial 
        self.risk_initial_percent = risk_initial_percent 
        self.risk_actual = risk_actual 
        self.risk_actual_percent = risk_actual_percent
        self.cost_total = cost_total
        self.cost_other = cost_other
        self.amount_buy_simple = amount_buy_simple
        self.amount_sell_simple = amount_sell_simple
        self.stoploss = stoploss
        self.profit_loss = profit_loss
        self.profit_loss_percent = profit_loss_percent
        self.r_multiple = r_multiple
        self.win_flag = win_flag
        self.id_buy = id_buy
        self.id_sell = id_sell
        self.currency_exchange_id = currency_exchange_id
        self.drawdown_id = drawdown_id
        self.pool_at_start = pool_at_start
        self.date_expiration = date_expiration
        self.expired_flag = expired_flag
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_INVESTMENT('%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.trade_id,
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
                        self.risk_input,
                        self.risk_input_percent,
                        self.risk_initial,
                        self.risk_initial_percent,
                        self.risk_actual,
                        self.risk_actual_percent,
                        self.cost_total,
                        self.cost_other,
                        self.amount_buy_simple,
                        self.amount_sell_simple,
                        self.stoploss,
                        self.profit_loss,
                        self.profit_loss_percent,
                        self.r_multiple,
                        self.win_flag,
                        self.id_buy,
                        self.id_sell,
                        self.currency_exchange_id,
                        self.drawdown_id,
                        self.pool_at_start,
                        self.expiration_date,
                        self.expired_flag,
                        self.active,
                        self.date_created,
                        self.date_modified)

class T_STOCK_NAME(Base):
    """ T_STOCK_NAME """
    __tablename__ = Table.STOCK_NAME
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
    __tablename__ = Table.MARKET
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
        return "<T_MARKET('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.market_id, self.code, self.name, self.country, self.active, self.date_created, self.date_modified)

class T_MARGIN(Base):
    """ T_MARGIN """
    __tablename__ = Table.MARGIN
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
    __tablename__ = Table.MARGIN_TYPE
    #__table_args__ = {'autoload':True}
    margin_type_id = Column(Integer, primary_key=True)
    margin_type = Column(String(50))

    def __init__(self, margin_type_id, margin_type):
        self.margin_type_id = margin_type_id
        self.margin_type = margin_type

    def __repr__(self):
        return "<T_MARGIN_TYPE('%s', '%s')>" % (self.margin_type_id, self.margin_type)

class T_ACCOUNT(Base):
    """ T_ACCOUNT """
    __tablename__ = Table.ACCOUNT
    #__table_args__ = {'autoload':True}
    account_id = Column(Integer, primary_key=True)
    name = Column(String(6))
    description = Column(String(64))
    parent_id = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, account_id, name, description, parent_id, active, date_created, date_modified):
        self.account_id = account_id
        self.name = name
        self.description = description
        self.parent_id = parent_id
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_ACCOUNT('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.account_id, self.name,
                self.description, self.parent_id, self.active, self.date_created, self.date_modified)

class T_CURRENCY(Base):
    """ T_CURRENCY """
    __tablename__ = Table.CURRENCY
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
    __tablename__ = Table.CURRENCY_EXCHANGE
    #__table_args__ = {'autoload':True}
    currency_exchange_id = Column(Integer, primary_key=True)
    currency_from_id = Column(Integer)
    currency_to_id = Column(Integer)
    exchange_rate = Column(Numeric(18,6))
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, currency_exchange_id, currency_from_id,
            currency_to_id, exchange_rate, date_created, date_modified):
        self.currency_exchange_id = currency_exchange_id
        self.currency_from_id = currency_from_id
        self.currency_to_id = currency_to_id
        self.exchange_rate = exchange_rate
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_CURRENCY_EXCHANGE('%s', '%s', '%s', '%s', '%s')>" % (
                self.currency_exchange_id,
                self.currency_from_id,
                self.currency_to_id,
                self.exchange_rate,
                self.date_created,
                self.date_modified)

class T_FORMULA(Base):
    """ T_FORMULA """
    __tablename__ = Table.FORMULA
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
    __tablename__ = Table.TRADE
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
    risk_input = Column(Numeric(18,6))
    risk_input_percent = Column(Numeric(18,6))
    risk_initial = Column(Numeric(18,6))
    risk_initial_percent = Column(Numeric(18,6))
    risk_actual = Column(Numeric(18,6))
    risk_actual_percent = Column(Numeric(18,6))
    cost_total = Column(Numeric(18,6))
    cost_other = Column(Numeric(18,6))
    amount_buy_simple = Column(Numeric(18,6))
    amount_sell_simple = Column(Numeric(18,6))
    stoploss = Column(Numeric(18,6))
    profit_loss = Column(Numeric(18,6))
    profit_loss_percent = Column(Numeric(18,6))
    r_multiple = Column(Numeric(18,6))
    win_flag = Column(Integer)
    id_buy = Column(Integer)
    id_sell = Column(Integer)
    currency_exchange_id = Column(Integer)
    drawdown_id = Column(Integer)
    pool_at_start = Column(Numeric(18,6))
    date_expiration = Column(DateTime)
    expired_flag = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)   

    def __init__(self, trade_id, market_id, stock_name_id, date_buy, year_buy, month_buy,
            day_buy, date_sell, year_sell, month_sell, day_sell, long_flag,
            price_buy, price_sell, shares_buy, shares_sell, commission_buy,
            commission_sell, tax_buy, tax_sell, risk_input, risk_input_percent, risk_initial,
            risk_initial_percent, risk_actual, risk_actual_percent, cost_total, cost_other,
            amount_buy_simple, amount_sell_simple, stoploss, profit_loss, profit_loss_percent, r_multiple,
            win_flag, id_buy, id_sell,
            currency_exchange_id, drawdown_id, pool_at_start, date_expiration,
            expired_flag, active, date_created, date_modified):
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
        self.risk_input = risk_input
        self.risk_input_percent = risk_input_percent
        self.risk_initial = risk_initial 
        self.risk_initial_percent = risk_initial_percent 
        self.risk_actual = risk_actual 
        self.risk_actual_percent = risk_actual_percent
        self.cost_total = cost_total
        self.cost_other = cost_other
        self.amount_buy_simple = amount_buy_simple
        self.amount_sell_simple = amount_sell_simple
        self.stoploss = stoploss
        self.profit_loss = profit_loss
        self.profit_loss_percent = profit_loss_percent
        self.r_multiple = r_multiple
        self.win_flag = win_flag
        self.id_buy = id_buy
        self.id_sell = id_sell
        self.currency_exchange_id = currency_exchange_id
        self.drawdown_id = drawdown_id
        self.pool_at_start = pool_at_start
        self.date_expiration = date_expiration
        self.expired_flag = expired_flag
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_TRADE('%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.trade_id,
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
                        self.risk_input,
                        self.risk_input_percent,
                        self.risk_initial,
                        self.risk_initial_percent,
                        self.risk_actual,
                        self.risk_actual_percent,
                        self.cost_total,
                        self.cost_other,
                        self.amount_buy_simple,
                        self.amount_sell_simple,
                        self.stoploss,
                        self.profit_loss,
                        self.profit_loss_percent,
                        self.r_multiple,
                        self.win_flag,
                        self.id_buy,
                        self.id_sell,
                        self.currency_exchange_id,
                        self.drawdown_id,
                        self.pool_at_start,
                        self.date_expiration,
                        self.expired_flag,
                        self.active,
                        self.date_created,
                        self.date_modified)

class T_RATE(Base):
    """ T_RATE """
    __tablename__ = Table.RATE
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
    automatic_flag = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, rate_id, calculated, calculated_percent,
            on_shares, on_commission, on_ordersize, on_other, commission, tax,
            formula_id, automatic_flag, date_created, date_modified):
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
        self.automatic_flag = automatic_flag
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_RATE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s')>" % (self.rate_id,
                        self.calculated, self.calculated_percent, self.on_shares,
                        self.on_commission, self.on_ordersize, self.on_other,
                        self.commission, self.tax, self.formula_id,
                        self.automatic_flag, self.date_created, self.date_modified)

class T_DRAWDOWN(Base):
    """ T_DRAWDOWN """
    __tablename__ = Table.DRAWDOWN
    #__table_args__ = {'autoload':True}
    drawdown_id = Column(Integer, primary_key=True)
    drawdown_current = Column(Integer)
    drawdown_max = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, drawdown_id, drawdown_current, drawdown_max,
            date_created,date_modified):
        self.drawdown_id = drawdown_id
        self.drawdown_current = drawdown_current
        self.drawdown_max = drawdown_max
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_DRAWDOWN('%s', '%s', '%s', '%s', '%s')>" % (
                self.drawdown_id,
                self.drawdown_current,
                self.drawdown_max,
                self.date_created,
                self.date_modified)

class T_PARAMETER(Base):
    """ T_PARAMETER """
    __tablename__ = Table.PARAMETER
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

class T_POOL(Base):
    """ T_POOL """
    __tablename__ = Table.POOL
    #__table_args__ = {'autoload':True}
    pool_id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    total = Column(Numeric(18,6))
    invested = Column(Numeric(18,6))
    cash = Column(Numeric(18,6))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, pool_id, account_id, total, invested, cash, active, date_created, date_modified):
        self.pool_id = pool_id
        self.account_id = account_id
        self.total = total
        self.invested = invested
        self.cash = cash
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_POOL('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
                self.pool_id ,
                self.account_id,
                self.total,
                self.invested,
                self.cash,
                self.active,
                self.date_created,
                self.date_modified)
