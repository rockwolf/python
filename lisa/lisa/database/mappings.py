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
    account_from_id = Column(Integer)
    account_to_id = Column(Integer)
    amount = Column(Numeric(18, 6))
    comment = Column(String(256))
    currency_exchange_id = Column(Integer)
    rate_id = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, finance_id, date, year, month, day, account_from_id,
            account_to_id, amount, comment, currency_exchange_id,
            rate_id, active, date_created, date_modified):
        self.finance_id = finance_id
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.account_from_id = account_from_id
        self.account_to_id = account_to_id
        self.amount = amount
        self.comment = comment
        self.currency_exchange_id = currency_exchange_id
        self.rate_id = rate_id
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.finance_id, self.date, self.year, self.month, self.day,
            self.account_from_id, self.account_to_id, self.amount,
            self.comment, self.active, self.rate_id,
            self.currency_exchange_id, self.date_created, self.date_modified)


class T_COMMODITY(Base):
    """ T_COMMODITY """
    __tablename__ = Table.COMMODITY
    #__table_args__ = {'autoload':True}
    commodity_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(256))
    commodity_type_id = Column(Integer)
    cfd_general_id = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, commodity_id, name, description,
        commodity_type_id, cfd_general_id,
        active, date_created, date_modified):
        self.commodity_id = commodity_id
        self.name = name
        self.description = description
        self.commodity_type_id = commodity_type_id
        self.cfd_general_id = cfd_general_id
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_COMMODITY('%s', \
        , '%s', '%s', '%s', '%s', '%s', '%s'\
        , '%s')>" % (self.commodity_id,
            self.name, self.description,
            self.commodity_type_id, self.cfd_general_id,
            self.active, self.date_created, self.date_modified)


class T_COMMODITY_TYPE(Base):
    """ T_COMMODITY_TYPE """
    __tablename__ = Table.COMMODITY_TYPE
    commodity_type_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(256))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, commodity_type_id, name, description,
        active, date_created, date_modified):
        self.commodity_type_id = commodity_type_id
        self.name = name
        self.description = description
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_COMMODITY_TYPE('%s', \
        , '%s', '%s', '%s', '%s', '%s')>" % (
            self.commodity_type_id, self.name,
            self.description, self.active,
            self.date_created, self.date_modified)


class T_CFD_GENERAL(Base):
    """ T_CFD_GENERAL """
    __tablename__ = Table.CFD_GENERAL
    cfd_general_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    market_id = Column(Integer)
    currency_id = Column(Integer)
    tick = Column(Numeric(18, 6))
    tick_value = Column(Numeric(18, 6))
    order_min = Column(Numeric(18, 6))
    order_max = Column(Numeric(18, 6))
    margin_day_proc = Column(Numeric(18, 6))
    margin_night_proc = Column(Numeric(18, 6))
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, cfd_general_id, name, market_id, description, active,
        currency_id, tick, tick_value, order_min, order_max, margin_day_proc,
        margin_night_proc, date_created, date_modified):
        self.cfd_general_id = cfd_general_id
        self.name = name
        self.market_id = market_id
        self.description = description
        self.active = active
        self.currency_id = currency_id
        self.tick = tick
        self.tick_value = tick_value
        self.order_min = order_min
        self.order_max = order_max
        self.margin_day_proc = margin_day_proc
        self.margin_night_proc = margin_night_proc
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_CFD_GENERAL('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s' '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.cfd_general_id,
                self.name, self.market_id, self.description, self.active,
                self.currency_id, self.tick, self.tick_value, self.order_min,
                self.order_max, self.margin_day_proc, self.margin_night_proc,
                self.date_created, self.date_modified)

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

    def __init__(self,
        market_id,
        code, name,
        country,
        active,
        date_created,
        date_modified):
        self.market_id = market_id
        self.code = code
        self.name = name
        self.country = country
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_MARKET('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.market_id, self.code, self.name, self.country,
            self.active, self.date_created, self.date_modified
        )


class T_ACCOUNT(Base):
    """ T_ACCOUNT """
    __tablename__ = Table.ACCOUNT
    #__table_args__ = {'autoload':True}
    account_id = Column(Integer, primary_key=True)
    name = Column(String(4000))
    description = Column(String(4000))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self,
        account_id,
        name,
        description,
        active,
        date_created,
        date_modified):
        self.account_id = account_id
        self.name = name
        self.description = description
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_ACCOUNT('%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.account_id, self.name, self.description,
            self.active, self.date_created, self.date_modified
        )


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
        return "<T_CURRENCY('%s', '%s', '%s')>" % (
            self.currency_id, self.code, self.description
        )


class T_CURRENCY_EXCHANGE(Base):
    """ T_CURRENCY_EXCHANGE """
    __tablename__ = Table.CURRENCY_EXCHANGE
    #__table_args__ = {'autoload':True}
    currency_exchange_id = Column(Integer, primary_key=True)
    currency_from_id = Column(Integer)
    currency_to_id = Column(Integer)
    exchange_rate = Column(Numeric(18, 6))
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


class T_TRADE(Base):
    """ T_TRADE """
    __tablename__ = Table.TRADE
    #__table_args__ = {'autoload':True}
    trade_id = Column(Integer, primary_key=True)
    market_id = Column(Integer)
    commodity_id = Column(Integer)
    date_buy = Column(DateTime)
    year_buy = Column(Integer)
    month_buy = Column(Integer)
    day_buy = Column(Integer)
    date_sell = Column(DateTime)
    year_sell = Column(Integer)
    month_sell = Column(Integer)
    day_sell = Column(Integer)
    long_flag = Column(Integer)
    price_buy = Column(Numeric(18, 6))
    price_buy_orig = Column(Numeric(18, 6))
    price_sell = Column(Numeric(18, 6))
    price_sell_orig = Column(Numeric(18, 6))
    shares_buy = Column(Integer)
    shares_sell = Column(Integer)
    commission_buy = Column(Numeric(18, 6))
    commission_sell = Column(Numeric(18, 6))
    tax_buy = Column(Numeric(18, 6))
    tax_sell = Column(Numeric(18, 6))
    amount_buy = Column(Numeric(18, 6))
    amount_sell = Column(Numeric(18, 6))
    amount_buy_simple = Column(Numeric(18, 6))
    amount_sell_simple = Column(Numeric(18, 6))
    risk_input = Column(Numeric(18, 6))
    risk_input_percent = Column(Numeric(18, 6))
    risk_initial = Column(Numeric(18, 6))
    risk_initial_percent = Column(Numeric(18, 6))
    risk_actual = Column(Numeric(18, 6))
    risk_actual_percent = Column(Numeric(18, 6))
    cost_total = Column(Numeric(18, 6))
    cost_other = Column(Numeric(18, 6))
    stoploss = Column(Numeric(18, 6))
    stoploss_orig = Column(Numeric(18, 6))
    profit_loss = Column(Numeric(18, 6))
    profit_loss_orig = Column(Numeric(18, 6))
    profit_loss_total = Column(Numeric(18, 6))
    profit_loss_total_percent = Column(Numeric(18, 6))
    r_multiple = Column(Numeric(18, 6))
    win_flag = Column(Integer)
    id_buy = Column(Integer)
    id_sell = Column(Integer)
    drawdown_id = Column(Integer)
    pool_at_start = Column(Numeric(18, 6))
    date_expiration = Column(DateTime)
    expired_flag = Column(Integer)
    spread = Column(Integer)
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self,
        trade_id,
        market_id,
        commodity_id,
        date_buy,
        year_buy,
        month_buy,
        day_buy,
        date_sell,
        year_sell,
        month_sell,
        day_sell,
        long_flag,
        price_buy,
        price_buy_orig,
        price_sell,
        price_sell_orig,
        shares_buy,
        shares_sell,
        commission_buy,
        commission_sell,
        tax_buy,
        tax_sell,
        amount_buy,
        amount_sell,
        amount_buy_simple,
        amount_sell_simple,
        risk_input,
        risk_input_percent,
        risk_initial,
        risk_initial_percent,
        risk_actual,
        risk_actual_percent,
        cost_total,
        cost_other,
        stoploss,
        stoploss_orig,
        profit_loss,
        profit_loss_orig,
        profit_loss_total,
        profit_loss_total_percent,
        r_multiple,
        win_flag,
        id_buy,
        id_sell,
        drawdown_id,
        pool_at_start,
        date_expiration,
        expired_flag,
        spread,
        active,
        date_created,
        date_modified):
        self.trade_id = trade_id
        self.market_id = market_id
        self.commodity_id = commodity_id
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
        self.price_buy_orig = price_buy_orig
        self.price_sell = price_sell
        self.price_sell_orig = price_sell_orig
        self.shares_buy = shares_buy
        self.shares_sell = shares_sell
        self.commission_buy = commission_buy
        self.commission_sell = commission_sell
        self.tax_buy = tax_buy
        self.tax_sell = tax_sell
        self.amount_buy = amount_buy
        self.amount_sell = amount_sell
        self.amount_buy_simple = amount_buy_simple
        self.amount_sell_simple = amount_sell_simple
        self.risk_input = risk_input
        self.risk_input_percent = risk_input_percent
        self.risk_initial = risk_initial
        self.risk_initial_percent = risk_initial_percent
        self.risk_actual = risk_actual
        self.risk_actual_percent = risk_actual_percent
        self.cost_total = cost_total
        self.cost_other = cost_other
        self.stoploss = stoploss
        self.stoploss_orig = stoploss_orig
        self.profit_loss = profit_loss
        self.profit_loss_orig = profit_loss_orig
        self.profit_loss_total = profit_loss_total
        self.profit_loss_total_percent = profit_loss_total_percent
        self.r_multiple = r_multiple
        self.win_flag = win_flag
        self.id_buy = id_buy
        self.id_sell = id_sell
        self.drawdown_id = drawdown_id
        self.pool_at_start = pool_at_start
        self.date_expiration = date_expiration
        self.expired_flag = expired_flag
        self.spread = spread
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_TRADE('%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
                self.trade_id,
                self.market_id,
                self.commodity_id,
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
                self.price_buy_orig,
                self.price_sell,
                self.price_sell_orig,
                self.shares_buy,
                self.shares_sell,
                self.commission_buy,
                self.commission_sell,
                self.tax_buy,
                self.tax_sell,
                self.amount_buy,
                self.amount_sell,
                self.amount_buy_simple,
                self.amount_sell_simple,
                self.risk_input,
                self.risk_input_percent,
                self.risk_initial,
                self.risk_initial_percent,
                self.risk_actual,
                self.risk_actual_percent,
                self.cost_total,
                self.cost_other,
                self.stoploss,
                self.stoploss_orig,
                self.profit_loss,
                self.profit_loss_orig,
                self.profit_loss_total,
                self.profit_loss_total_percent,
                self.r_multiple,
                self.win_flag,
                self.id_buy,
                self.id_sell,
                self.drawdown_id,
                self.pool_at_start,
                self.date_expiration,
                self.expired_flag,
                self.spread,
                self.active,
                self.date_created,
                self.date_modified)


class T_RATE(Base):
    """ T_RATE """
    __tablename__ = Table.RATE
    #__table_args__ = {'autoload':True}
    rate_id = Column(Integer, primary_key=True)
    commission = Column(Numeric(18, 6))
    tax = Column(Numeric(18, 6))
    automatic_flag = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, rate_id, commission, tax,
        automatic_flag, date_created, date_modified):
        self.rate_id = rate_id
        self.commission = commission
        self.tax = tax
        self.automatic_flag = automatic_flag
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_RATE('%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.rate_id, self.commission, self.tax,
            self.automatic_flag, self.date_created,
            self.date_modified)


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
            date_created, date_modified):
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
        return "<T_PARAMETER('%s', '%s', '%s', '%s')>" % (
            self.parameter_id, self.name, self.value, self.description
        )


class T_POOL(Base):
    """ T_POOL """
    __tablename__ = Table.POOL
    #__table_args__ = {'autoload':True}
    pool_id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    total = Column(Numeric(18, 6))
    invested = Column(Numeric(18, 6))
    cash = Column(Numeric(18, 6))
    active = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self,
        pool_id,
        account_id,
        total,
        invested,
        cash,
        active,
        date_created,
        date_modified):
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
                self.pool_id,
                self.account_id,
                self.total,
                self.invested,
                self.cash,
                self.active,
                self.date_created,
                self.date_modified)
