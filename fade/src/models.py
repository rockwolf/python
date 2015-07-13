#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""

from src import db
#from sqlalchemy.ext.declarative import declarative_base

#Base = db.declarative_base()
#metadata = Base.metadata

class T_ACCOUNT(db.Model):
    """
        T_ACCOUNT
    """
    account_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(4000), nullable=False, default='')
    description = db.Column(db.String(4000), nullable=False, default='')
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    date_modified = db.Column(db.DateTime, nullable=False, default='1900-01-01')

    def __repr__(self):
        return "<T_ACCOUNT('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.account_id, self.name, self.description,
            self.active, self.date_created, self.date_modified)


# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text
from sqlalchemy.orm import relationship


class TAccount(db.Model):
    __tablename__ = u't_account'

    account_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_account_account_id_seq'::regclass)"))
    name = db.Column(String(4000), nullable=False)
    description = db.Column(String(4000), nullable=False)
    is_active = db.Column(db.Integer, nullable=False, server_default=text("1"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TCfdGeneral(db.Model):
    __tablename__ = u't_cfd_general'

    cfd_general_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_cfd_general_cfd_general_id_seq'::regclass)"))
    name = db.Column(String(50), nullable=False)
    market_id = db.Column(ForeignKey(u't_market.market_id'), nullable=False, server_default=text("(-1)"))
    currency_id = db.Column(ForeignKey(u't_currency.currency_id'), nullable=False, server_default=text("1"))
    tick = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("1.0"))
    tick_value = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("1.0"))
    order_min = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("(-1.0)"))
    order_max = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("(-1.0)"))
    margin_day_proc = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("(-1.0)"))
    margin_night_proc = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("(-1.0)"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))

    currency = relationship(u'TCurrency')
    market = relationship(u'TMarket')


class TCommodity(db.Model):
    __tablename__ = u't_commodity'

    commodity_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_commodity_commodity_id_seq'::regclass)"))
    name = db.Column(String(50), nullable=False)
    description = db.Column(String(256), nullable=False, server_default=text("''::character varying"))
    commodity_type_id = db.Column(ForeignKey(u't_commodity_type.commodity_type_id'), nullable=False, server_default=text("1"))
    cfd_general_id = db.Column(ForeignKey(u't_cfd_general.cfd_general_id'), nullable=False, server_default=text("(-1)"))
    is_active = db.Column(db.Integer, nullable=False, server_default=text("1"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))

    cfd_general = relationship(u'TCfdGeneral')
    commodity_type = relationship(u'TCommodityType')


class TCommodityType(db.Model):
    __tablename__ = u't_commodity_type'

    commodity_type_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_commodity_type_commodity_type_id_seq'::regclass)"))
    name = db.Column(String(50), nullable=False)
    description = db.Column(String(256), nullable=False, server_default=text("''::character varying"))
    is_active = db.Column(db.Integer, nullable=False, server_default=text("1"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TCurrency(db.Model):
    __tablename__ = u't_currency'

    currency_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(String(3), nullable=False, server_default=text("''::character varying"))
    description = db.Column(String(256), nullable=False, server_default=text("''::character varying"))


class TCurrencyExchange(db.Model):
    __tablename__ = u't_currency_exchange'

    currency_exchange_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_currency_exchange_currency_exchange_id_seq'::regclass)"))
    currency_from_id = db.Column(ForeignKey(u't_currency.currency_id'), nullable=False, server_default=text("(-1)"))
    currency_to_id = db.Column(ForeignKey(u't_currency.currency_id'), nullable=False, server_default=text("(-1)"))
    exchange_rate = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))

    currency_from = relationship(u'TCurrency', primaryjoin='TCurrencyExchange.currency_from_id == TCurrency.currency_id')
    currency_to = relationship(u'TCurrency', primaryjoin='TCurrencyExchange.currency_to_id == TCurrency.currency_id')


class TDrawdown(db.Model):
    __tablename__ = u't_drawdown'

    drawdown_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_drawdown_drawdown_id_seq'::regclass)"))
    drawdown_current = db.Column(db.Integer, nullable=False, server_default=text("0"))
    drawdown_max = db.Column(db.Integer, nullable=False, server_default=text("0"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TMarket(db.Model):
    __tablename__ = u't_market'

    market_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(String(50), nullable=False, unique=True)
    name = db.Column(String(30), nullable=False)
    country = db.Column(String(3), nullable=False)
    is_active = db.Column(db.Integer, nullable=False, server_default=text("1"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TParameter(db.Model):
    __tablename__ = u't_parameter'

    parameter_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)
    value = db.Column(String(512), nullable=False)
    description = db.Column(String(256), nullable=False)


class TPool(db.Model):
    __tablename__ = u't_pool'

    pool_id = db.Column(u'pool_id', db.Integer, primary_key=True, nullable=False, server_default=text("nextval('t_pool_pool_id_seq'::regclass)"))
    account_id = db.Column(u'account_id', ForeignKey(u't_account.account_id'), nullable=False)
    total = db.Column(u'total', db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    invested = db.Column(u'invested', db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    cash = db.Column(u'cash', db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    is_active = db.Column(u'is_active', db.Integer, nullable=False, server_default=text("1"))
    date_created = db.Column(u'date_created', db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(u'date_modified', db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TRate(db.Model):
    __tablename__ = u't_rate'

    rate_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_rate_rate_id_seq'::regclass)"))
    commission = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    tax = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    automatic_flag = db.Column(db.Integer, nullable=False, server_default=text("(-1)"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TTrade(db.Model):
    __tablename__ = u't_trade'

    trade_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_trade_trade_id_seq'::regclass)"))
    trade_calculated_id = db.Column(ForeignKey(u't_trade_calculated.trade_calculated_id'), nullable=False, server_default=text("(-1)"))
    market_id = db.Column(db.Integer, nullable=False)
    commodity_id = db.Column(ForeignKey(u't_commodity.commodity_id'), nullable=False)
    date_buy = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    year_buy = db.Column(db.Integer, nullable=False, server_default=text("1900"))
    month_buy = db.Column(db.Integer, nullable=False, server_default=text("1"))
    day_buy = db.Column(db.Integer, nullable=False, server_default=text("1"))
    date_sell = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    year_sell = db.Column(db.Integer, nullable=False, server_default=text("1900"))
    month_sell = db.Column(db.Integer, nullable=False, server_default=text("1"))
    day_sell = db.Column(db.Integer, nullable=False, server_default=text("1"))
    is_long = db.Column(db.Integer, nullable=False, server_default=text("(-1)"))
    price_buy_orig = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    price_sell_orig = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    shares_buy = db.Column(db.Integer, nullable=False, server_default=text("0"))
    shares_sell = db.Column(db.Integer, nullable=False, server_default=text("0"))
    comment = db.Column(String(256), nullable=False, server_default=text("''::character varying"))
    currency_exchange_id_buy = db.Column(ForeignKey(u't_currency_exchange.currency_exchange_id'), nullable=False, server_default=text("(-1)"))
    currency_exchange_id_sell = db.Column(ForeignKey(u't_currency_exchange.currency_exchange_id'), nullable=False, server_default=text("(-1)"))
    rate_id_buy = db.Column(ForeignKey(u't_rate.rate_id'), nullable=False, server_default=text("(-1)"))
    rate_id_sell = db.Column(ForeignKey(u't_rate.rate_id'), nullable=False, server_default=text("(-1)"))
    risk_input_percent = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    is_winner = db.Column(db.Integer, nullable=False, server_default=text("(-1)"))
    drawdown_id = db.Column(ForeignKey(u't_drawdown.drawdown_id'), nullable=False, server_default=text("(-1)"))
    trade_pool_id = db.Column(ForeignKey(u't_trade_pool.trade_pool_id'), nullable=False, server_default=text("(-1)"))
    date_expiration = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    is_expired = db.Column(db.Integer, nullable=False, server_default=text("(-1)"))
    is_active = db.Column(db.Integer, nullable=False, server_default=text("1"))
    reconciled = db.Column(db.Integer, nullable=False, server_default=text("(-1)"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))

    commodity = relationship(u'TCommodity')
    t_currency_exchange = relationship(u'TCurrencyExchange', primaryjoin='TTrade.currency_exchange_id_buy == TCurrencyExchange.currency_exchange_id')
    t_currency_exchange1 = relationship(u'TCurrencyExchange', primaryjoin='TTrade.currency_exchange_id_sell == TCurrencyExchange.currency_exchange_id')
    drawdown = relationship(u'TDrawdown')
    t_rate_buy = relationship(u'TRate', primaryjoin='TTrade.rate_id_buy == TRate.rate_id')
    t_rate_sell = relationship(u'TRate', primaryjoin='TTrade.rate_id_sell == TRate.rate_id')
    trade_calculated = relationship(u'TTradeCalculated')
    trade_pool = relationship(u'TTradePool')


class TTradeCalculated(db.Model):
    __tablename__ = u't_trade_calculated'

    trade_calculated_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_trade_calculated_trade_calculated_id_seq'::regclass)"))
    price_buy = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    price_sell = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    amount_buy = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    amount_sell = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    amount_buy_simple = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    amount_sell_simple = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    risk_input = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    risk_initial = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    risk_initial_percent = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    risk_actual = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    risk_actual_percent = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    cost_total = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    cost_other = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    stoploss = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    stoploss_orig = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    profit_loss = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    profit_loss_orig = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    profit_loss_total = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    profit_loss_total_percent = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    r_multiple = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))


class TTradePool(db.Model):
    __tablename__ = u't_trade_pool'

    trade_pool_id = db.Column(db.Integer, primary_key=True, server_default=text("nextval('t_trade_pool_trade_pool_id_seq'::regclass)"))
    pool_at_start = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    pool_override = db.Column(db.Numeric(18, 6), nullable=False, server_default=text("0.0"))
    date_created = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


class TVersion(db.Model):
    __tablename__ = u't_version'

    version_id = db.Column(u'version_id', db.Integer, primary_key=True, nullable=False)
    version = db.Column(u'version', String(100), nullable=False, server_default=text("''::character varying"))
    version_info = db.Column(u'version_info', String(100), nullable=False, server_default=text("''::character varying"))
    date_created = db.Column(u'date_created', db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))
    date_modified = db.Column(u'date_modified', db.DateTime, nullable=False, server_default=text("'1900-01-01 00:00:00'::timestamp without time zone"))


#t_v_account = Table(
#    u'v_account', metadata,
#    db.Column(u'account_id', db.Integer),
#    db.Column(u'name', String(4000)),
#    db.Column(u'description', String(4000)),
#    db.Column(u'is_active', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_account_name = Table(
#    u'v_account_name', metadata,
#    db.Column(u'account_id', db.Integer),
#    db.Column(u'name', Text)
#)
#
#
#t_v_cfd_general = Table(
#    u'v_cfd_general', metadata,
#    db.Column(u'cfd_general_id', db.Integer),
#    db.Column(u'name', String(50)),
#    db.Column(u'market_id', db.Integer),
#    db.Column(u'currency_id', db.Integer),
#    db.Column(u'tick', db.Numeric(18, 6)),
#    db.Column(u'tick_value', db.Numeric(18, 6)),
#    db.Column(u'order_min', db.Numeric(18, 6)),
#    db.Column(u'order_max', db.Numeric(18, 6)),
#    db.Column(u'margin_day_proc', db.Numeric(18, 6)),
#    db.Column(u'margin_night_proc', db.Numeric(18, 6)),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_commodity = Table(
#    u'v_commodity', metadata,
#    db.Column(u'commodity_id', db.Integer),
#    db.Column(u'name', String(50)),
#    db.Column(u'description', String(256)),
#    db.Column(u'commodity_type_id', db.Integer),
#    db.Column(u'cfd_general_id', db.Integer),
#    db.Column(u'is_active', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_commodity_info = Table(
#    u'v_commodity_info', metadata,
#    db.Column(u'commodity_id', db.Integer),
#    db.Column(u'commodity_name', String(50)),
#    db.Column(u'commodity_description', String(256)),
#    db.Column(u'commodity_type', String(50)),
#    db.Column(u'commodity_type_description', String(256)),
#    db.Column(u'cfd_name', String(50)),
#    db.Column(u'market_id', db.Integer),
#    db.Column(u'market', String(30)),
#    db.Column(u'market_code', String(50)),
#    db.Column(u'market_country', String(3))
#)
#
#
#t_v_commodity_type = Table(
#    u'v_commodity_type', metadata,
#    db.Column(u'commodity_type_id', db.Integer),
#    db.Column(u'name', String(50)),
#    db.Column(u'description', String(256)),
#    db.Column(u'is_active', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_currency = Table(
#    u'v_currency', metadata,
#    db.Column(u'currency_id', db.Integer),
#    db.Column(u'code', String(3)),
#    db.Column(u'description', String(256))
#)
#
#
#t_v_currency_exchange = Table(
#    u'v_currency_exchange', metadata,
#    db.Column(u'currency_exchange_id', db.Integer),
#    db.Column(u'currency_from_id', db.Integer),
#    db.Column(u'currency_to_id', db.Integer),
#    db.Column(u'exchange_rate', db.Numeric(18, 6)),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_drawdown = Table(
#    u'v_drawdown', metadata,
#    db.Column(u'drawdown_id', db.Integer),
#    db.Column(u'drawdown_current', db.Integer),
#    db.Column(u'drawdown_max', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_expectancy = Table(
#    u'v_expectancy', metadata,
#    db.Column(u'?column?', db.Integer)
#)
#
#
#t_v_market = Table(
#    u'v_market', metadata,
#    db.Column(u'market_id', db.Integer),
#    db.Column(u'code', String(50)),
#    db.Column(u'name', String(30)),
#    db.Column(u'country', String(3)),
#    db.Column(u'is_active', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_parameter = Table(
#    u'v_parameter', metadata,
#    db.Column(u'parameter_id', db.Integer),
#    db.Column(u'name', String(50)),
#    db.Column(u'value', String(512)),
#    db.Column(u'description', String(256))
#)
#
#
#t_v_pool = Table(
#    u'v_pool', metadata,
#    db.Column(u'pool_id', db.Integer),
#    db.Column(u'account_id', db.Integer),
#    db.Column(u'total', db.Numeric(18, 6)),
#    db.Column(u'invested', db.Numeric(18, 6)),
#    db.Column(u'cash', db.Numeric(18, 6)),
#    db.Column(u'is_active', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_rate = Table(
#    u'v_rate', metadata,
#    db.Column(u'rate_id', db.Integer),
#    db.Column(u'commission', db.Numeric(18, 6)),
#    db.Column(u'tax', db.Numeric(18, 6)),
#    db.Column(u'automatic_flag', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_trade = Table(
#    u'v_trade', metadata,
#    db.Column(u'trade_id', db.Integer),
#    db.Column(u'trade_calculated_id', db.Integer),
#    db.Column(u'market_id', db.Integer),
#    db.Column(u'commodity_id', db.Integer),
#    db.Column(u'date_buy', db.DateTime),
#    db.Column(u'year_buy', db.Integer),
#    db.Column(u'month_buy', db.Integer),
#    db.Column(u'day_buy', db.Integer),
#    db.Column(u'date_sell', db.DateTime),
#    db.Column(u'year_sell', db.Integer),
#    db.Column(u'month_sell', db.Integer),
#    db.Column(u'day_sell', db.Integer),
#    db.Column(u'is_long', db.Integer),
#    db.Column(u'price_buy_orig', db.Numeric(18, 6)),
#    db.Column(u'price_sell_orig', db.Numeric(18, 6)),
#    db.Column(u'shares_buy', db.Integer),
#    db.Column(u'shares_sell', db.Integer),
#    db.Column(u'comment', String(256)),
#    db.Column(u'currency_exchange_id_buy', db.Integer),
#    db.Column(u'currency_exchange_id_sell', db.Integer),
#    db.Column(u'rate_id_buy', db.Integer),
#    db.Column(u'rate_id_sell', db.Integer),
#    db.Column(u'risk_input_percent', db.Numeric(18, 6)),
#    db.Column(u'is_winner', db.Integer),
#    db.Column(u'drawdown_id', db.Integer),
#    db.Column(u'trade_pool_id', db.Integer),
#    db.Column(u'date_expiration', db.DateTime),
#    db.Column(u'is_expired', db.Integer),
#    db.Column(u'is_active', db.Integer),
#    db.Column(u'reconciled', db.Integer),
#    db.Column(u'date_created', db.DateTime),
#    db.Column(u'date_modified', db.DateTime)
#)
#
#
#t_v_trade_journal = Table(
#    u'v_trade_journal', metadata,
#    db.Column(u'trade_id', db.Integer)
#)
